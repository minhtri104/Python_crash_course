class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, **user_info):
        """Khởi tạo các thuộc tính first_name và last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        """Tóm tắt thông tin người dùng"""
        print("\nHọ và tên: " + self.first_name + " " + self.last_name)
        print(f"Thông tin thêm:")
        for key, value in self.user_info.items():
            print(f"{key}: {value}")

    def greet_user(self):
        """Chào người dùng"""
        print("Xin chào, " + self.first_name + " " + self.last_name + "!")

    def increment_login_attempts(self):
        """Tăng số lần đăng nhập"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Đặt lại số lần đăng nhập về 0"""
        self.login_attempts = 0


user1 = User(
    "Minh Trí", "Nguyễn", Age=21, Hometown="Gia Lai", Email="trinm123@gmail.com"
)
user2 = User(
    "Minh Đức", "Nguyễn", Age=22, Hometown="Gia Lai", Email="ducn123.@gmail.com"
)
user3 = User(
    "Minh Khang", "Nguyễn", Age=23, Hometown="Gia Lai", Email="khangn123.@gmail.com"
)
# user1
user1.describe_user()
user1.greet_user()
# Sau khi đăng nhập
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Số lần đăng nhập: {user1.login_attempts}")
# Sau khi reset
user1.reset_login_attempts()
print(f"Số lần đăng nhập sau khi reset: {user1.login_attempts}")


# user2
user2.describe_user()
user2.greet_user()

# user3
user3.describe_user()
user3.greet_user()
