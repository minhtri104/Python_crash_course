class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Khởi tạo các thuộc tính mô tả xe"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2000

    def get_descriptive_name(self):
        """Trả về một tên mô tả, có dạng chuỗi"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """In ra thông báo về số dặm đã đi được"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Cập nhật số dặm đã đi được với giá trị cho trước
        Tránh việc lùi số dặm
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Tăng số dặm đã đi được với giá trị cho trước"""
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(25000)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
