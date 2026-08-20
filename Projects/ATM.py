################  WELCOME TO MY ATM PROJECT  ##############
import json
import os
import datetime
import logging
from typing import *

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")


class ATM:
    DATA_FILE = "atm_data.json"

    def __init__(self):
        self.balance: float = 0.0
        self.pin: str = "1234"
        self.daily_limit: float = 5000.0
        self.today_withdrawn: float = 0.0
        self.last_reset_date: str = datetime.date.today().isoformat()
        self.transaction_history: List[Dict] = []
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r") as f:
                    data = json.load(f)
                self.balance = data.get("balance", 0.0)
                self.pin = data.get("pin", "1234")
                self.daily_limit = data.get("daily_limit", 5000.0)
                self.today_withdrawn = data.get("today_withdrawn", 0.0)
                self.last_reset_date = data.get("last_reset_date", datetime.date.today().isoformat())
                self.transaction_history = data.get("history", [])
                self._reset_daily_if_needed()
            except Exception as e:
                logging.error(f"خطا در بارگذاری داده: {e}")

    def _save_data(self):
        try:
            data = {
                "balance": self.balance,
                "pin": self.pin,
                "daily_limit": self.daily_limit,
                "today_withdrawn": self.today_withdrawn,
                "last_reset_date": self.last_reset_date,
                "history": self.transaction_history[-100:]
            }
            with open(self.DATA_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.error(f"خطا در ذخیره‌سازی داده: {e}")

    def _reset_daily_if_needed(self):
        today = datetime.date.today().isoformat()
        if self.last_reset_date != today:
            self.today_withdrawn = 0.0
            self.last_reset_date = today
            self._save_data()

    def _add_transaction(self, trans_type: str, amount: float, status: str = "Success"):
        self.transaction_history.append({
            "type": trans_type,
            "amount": amount,
            "status": status,
            "time": datetime.datetime.now().isoformat()
        })
        self._save_data()

    def authenticate(self) -> bool:
        for attempt in range(3):
            entered = input("Enter your 4-digit PIN: ").strip()
            if entered == self.pin:
                print("Authentication successful.\n")
                return True
            print(f" Incorrect PIN. {2 - attempt} attempts remaining.")
        print(" Too many failed attempts. Exiting...")
        return False

    def check_balance(self):
        print(f"\n Current Balance: ₹{self.balance:,.2f}")
        self._add_transaction("Balance Inquiry", 0.0)

    def deposit(self):
        try:
            amount_str = input("Enter deposit amount (₹): ").strip()
            if not amount_str:
                print(" Amount cannot be empty.")
                return
            amount = float(amount_str)
            if amount <= 0:
                print(" Amount must be positive.")
                return
            self.balance += amount
            print(f"₹{amount:,.2f} deposited successfully.")
            self._add_transaction("Deposit", amount)
        except ValueError:
            print(" Invalid amount. Please enter a number (e.g. 1500 or 1500.50).")

    def withdraw(self):
        self._reset_daily_if_needed()
        try:
            amount_str = input("Enter withdrawal amount (₹): ").strip()
            if not amount_str:
                print(" Amount cannot be empty.")
                return
            amount = float(amount_str)
            if amount <= 0:
                print(" Amount must be positive.")
                return

            if amount > self.balance:
                print(" Insufficient balance.")
                self._add_transaction("Withdraw", amount, "Failed - Insufficient Balance")
                return

            if self.today_withdrawn + amount > self.daily_limit:
                print(f" Daily withdrawal limit (₹{self.daily_limit:,.2f}) exceeded.")
                self._add_transaction("Withdraw", amount, "Failed - Daily Limit Exceeded")
                return

            confirm = input(f" Confirm withdrawal of ₹{amount:,.2f}? (y/n): ").strip().lower()
            if confirm == 'n':
                print(" Withdrawal cancelled.")
                self._add_transaction("Withdraw", amount, "Cancelled by user")
                return

            self.balance -= amount
            self.today_withdrawn += amount
            print(f" Please collect your ₹{amount:,.2f} cash.")
            self._add_transaction("Withdraw", amount)
        except ValueError:
            print(" Invalid amount. Please enter a number (e.g. 500 or 500.75).")

    def change_pin(self):
        old = input("Enter current PIN: ").strip()
        if old != self.pin:
            print(" Incorrect current PIN.")
            return
        new1 = input("Enter new 4-digit PIN: ").strip()
        if not new1.isdigit() or len(new1) != 4:
            print(" PIN must be exactly 4 digits (only numbers).")
            return
        new2 = input("Confirm new PIN: ").strip()
        if new1 != new2:
            print(" PINs do not match.")
            return
        self.pin = new1
        self._save_data()
        print(" PIN changed successfully.")

    def show_history(self):
        if not self.transaction_history:
            print("\n No transactions yet.")
            return
        print("\n Transaction History (last 50):")
        print("-" * 70)
        for t in self.transaction_history[-50:]:
            print(f"{t['time']} | {t['type']:15} | ₹{t['amount']:>12,.2f} | {t['status']}")
        print("-" * 70)

    def run(self):
        if not self.authenticate():
            return

        while True:
            print("\n" + "=" * 50)
            print("          ATM MAIN MENU")
            print("=" * 50)
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Change PIN")
            print("6. Exit")
            print("=" * 50)

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                self.change_pin()
            elif choice == "6":
                print("\n Thank you for using our ATM. Have a great day!")
                break
            else:
                print(" Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()