"""A class that can be used to represent a electric car."""

from car import Car


class Battery:
    """Mô hình hóa pin của xe điện"""

    def __init__(self, battery_size=70):
        """Khởi tạo các thuộc tính của pin"""
        self.battery_size = battery_size

    def describe_battery(self):
        """In ra thông tin về pin của xe điện"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Hiên thị phạm vi di chuyển dựa trên dung lượng pin"""
        if self.battery_size == 70:
            driving_range = 240
        elif self.battery_size == 85:
            driving_range = 270
        else:
            driving_range = 0
        message = "This car can go approximately " + str(driving_range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """In ra thông tin về pin của xe điện"""
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """Mô phỏng việc đổ xăng cho xe điện"""
        print("This car doesn't need a gas tank!")
