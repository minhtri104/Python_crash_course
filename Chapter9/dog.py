class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Khởi tạo thuộc tính tên và tuổi"""
        self.name = name
        self.age = age

    def sit(self):
        """Mô phỏng việc ra lệnh cho chú chó ngồi"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Mô phỏng việc ra lệnh cho chú chó lăn ra đất"""
        print(f"{self.name} rolled over!")
