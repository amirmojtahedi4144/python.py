class Medicine:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - قیمت: {self.price} تومان - موجودی: {self.quantity} عدد"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"کارمند: {self.name} - حقوق: {self.salary} تومان"


class DrugStore:
    def __init__(self):
        self.medicines = []
        self.sales_history = []
        self.employees = []

    def add_medicine(self, medicine:Medicine):
        self.medicines.append(medicine)

    def show_inventory(self):
        print("موجودی داروخانه:")
        for medicine in self.medicines:
            print(medicine)

    def sell_medicine(self, medicine_name, quantity, employee_name):
        for medicine in self.medicines:
            if medicine.name == medicine_name:
                if medicine.quantity >= quantity:
                    medicine.quantity -= quantity
                    total_price = medicine.price * quantity
                    self.sales_history.append((medicine_name, quantity, total_price, employee_name))
                    print(f"دارو {medicine_name} به تعداد {quantity} عدد فروخته شد. مجموع: {total_price} تومان.")
                    return
                else:
                    print(f"موجودی کافی نیست. موجودی فعلی: {medicine.quantity} عدد.")
                    return
        print("دارو یافت نشد.")

    def show_sales_history(self):
        print("تاریخچه خریدها:")
        for sale in self.sales_history:
            print(f"دارو: {sale[0]}, تعداد: {sale[1]}, مجموع: {sale[2]} تومان, فروشنده: {sale[3]}")

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print("کارکنان داروخانه:")
        for employee in self.employees:
            print(employee)


# مثال استفاده از کلاس‌ها
if __name__ == "__main__":
    store = DrugStore()

    # افزودن داروها به داروخانه
    store.add_medicine(Medicine("آسپرین", 5000, 20))
    store.add_medicine(Medicine("پاراستامول", 3000, 15))
    store.add_medicine(Medicine("ایبوپروفن", 7000, 10))

    # افزودن کارکنان به داروخانه
    store.add_employee(Employee("علی", 3000000))
    store.add_employee(Employee("سارا", 2500000))

    # نمایش موجودی داروخانه
    store.show_inventory()

    # فروش دارو
    store.sell_medicine("آسپرین", 5, "علی")
    store.sell_medicine("پاراستامول", 2, "سارا")

    # نمایش موجودی بعد از فروش
    store.show_inventory()

    # نمایش تاریخچه خریدها
    store.show_sales_history()

    # نمایش کارکنان داروخانه
    store.show_employees()