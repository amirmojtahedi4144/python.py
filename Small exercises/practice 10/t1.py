class Car:
    def __init__(self, make, model, year, fuel_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity * 0.5
        self.is_running = False
        self.odometer = 0
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} روشن شد.")
        else:
            print(f"{self.make} {self.model} از قبل روشن است.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.make} {self.model} خاموش شد.")
        else:
            print(f"{self.make} {self.model} از قبل خاموش است.")
    def drive(self, distance):
        if self.is_running:
            fuel_needed = distance * 0.1
            if self.current_fuel >= fuel_needed:
                self.current_fuel -= fuel_needed
                self.odometer += distance
                print(f"{self.make} {self.model} مسافت {distance} کیلومتر را طی کرد. مصرف سوخت: {fuel_needed:.2f} لیتر.")
                print(f"مقدار بنزین باقی‌مانده: {self.current_fuel:.2f} لیتر.")
            else:
                print("سوخت کافی برای طی این مسافت وجود ندارد!")
        else:
            print(f"{self.make} {self.model} باید روشن باشد تا بتواند رانندگی کند.")
    def refuel(self, amount):
        if amount > 0:
            if self.current_fuel + amount <= self.fuel_capacity:
                self.current_fuel += amount
                print(f"{amount} لیتر سوخت اضافه شد. مقدار فعلی بنزین: {self.current_fuel:.2f} لیتر.")
            else:
                added = self.fuel_capacity - self.current_fuel
                self.current_fuel = self.fuel_capacity
                print(f"باک پر شد. {added:.2f} لیتر سوخت اضافه شد. مقدار فعلی بنزین: {self.current_fuel:.2f} لیتر.")
        else:
            print("مقدار سوخت باید مثبت باشد.")
    def get_info(self):
        status = "روشن" if self.is_running else "خاموش"
        return (f"اطلاعات خودرو:\n"
                f"  - سازنده: {self.make}\n"
                f"  - مدل: {self.model}\n"
                f"  - سال ساخت: {self.year}\n"
                f"  - وضعیت موتور: {status}\n"
                f"  - میزان بنزین: {self.current_fuel:.2f}/{self.fuel_capacity} لیتر\n"
                f"  - مسافت طی شده: {self.odometer} کیلومتر")
class IranianCar(Car):
    def __init__(self, make, model, year, fuel_capacity, has_cng=False):
        super().__init__(make, model, year, fuel_capacity)
        self.has_cng = has_cng
        self.current_cng = fuel_capacity * 0.3 if has_cng else 0
    def switch_fuel_type(self):
        if self.has_cng:
            print("در حال تغییر نوع سوخت...")
        else:
            print(f"{self.make} {self.model} سیستم سوخت دوگانه ندارد.")
    def get_info(self):
        base_info = super().get_info()
        cng_info = f"  - میزان CNG: {self.current_cng:.2f}/(ظرفیت CNG)"
        if self.has_cng:
            return f"{base_info}\n{cng_info}"
        else:
            return base_info
class ForeignCar(Car):
    def __init__(self, make, model, year, fuel_capacity, is_hybrid=False, battery_charge=100):
        super().__init__(make, model, year, fuel_capacity)
        self.is_hybrid = is_hybrid
        self.battery_charge = battery_charge if is_hybrid else 0
    def drive(self, distance):
        if self.is_running:
            if self.is_hybrid:
                fuel_needed = distance * 0.08
                battery_drain = distance * 0.02
                if self.current_fuel >= fuel_needed and self.battery_charge >= battery_drain:
                    self.current_fuel -= fuel_needed
                    self.battery_charge -= battery_drain
                    self.odometer += distance
                    print(f"خودروی هیبریدی {self.make} {self.model} مسافت {distance} کیلومتر را طی کرد.")
                    print(f"مصرف سوخت: {fuel_needed:.2f} لیتر، مصرف باتری: {battery_drain:.2f}%.")
                    print(f"مقدار بنزین باقی‌مانده: {self.current_fuel:.2f} لیتر، شارژ باتری: {self.battery_charge:.2f}%.")
                else:
                    print("سوخت یا شارژ باتری کافی برای طی این مسافت وجود ندارد!")
            else:
                super().drive(distance)
        else:
            print(f"{self.make} {self.model} باید روشن باشد تا بتواند رانندگی کند.")
    def charge_battery(self, percentage):
        if self.is_hybrid:
            if 0 < percentage <= 100:
                if self.battery_charge + percentage <= 100:
                    self.battery_charge += percentage
                    print(f"باتری به میزان {percentage}% شارژ شد. شارژ فعلی: {self.battery_charge}%.")
                else:
                    added_charge = 100 - self.battery_charge
                    self.battery_charge = 100
                    print(f"باتری کامل شارژ شد. {added_charge}% اضافه شد. شارژ فعلی: {self.battery_charge}%.")
            else:
                print("درصد شارژ باید بین 1 تا 100 باشد.")
        else:
            print(f"{self.make} {self.model} هیبریدی نیست و باتری ندارد.")
    def get_info(self):
        base_info = super().get_info()
        hybrid_info = f"  - هیبریدی: بله\n  - شارژ باتری: {self.battery_charge:.2f}%" if self.is_hybrid else "  - هیبریدی: خیر"
        return f"{base_info}\n{hybrid_info}"
pride = IranianCar("سايپا", "پراید", 1399, 45)
print(pride.get_info())
pride.start_engine()
pride.drive(100)
pride.refuel(20)
pride.switch_fuel_type()
print("\n" + "="*30 + "\n")
prius = ForeignCar("تویوتا", "پریوس", 2020, 45)
print(prius.get_info())
prius.start_engine()
prius.drive(150)
prius.charge_battery(50)
prius.stop_engine()
print("\n" + "="*30 + "\n")
bmw = ForeignCar("بی ام و", "X5", 2022, 70)
print(bmw.get_info())
bmw.start_engine()
bmw.drive(200)
print(f"مسافت طی شده توسط BMW: {bmw.odometer} کیلومتر")