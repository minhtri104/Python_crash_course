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
        print("Thông tin thêm:")
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


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can deleted post", "can ban user"]

    def show_privileges(self):
        """Liệt kê các quyền của quản trị viên"""
        print("Các quyền của quản trị viên: ")
        for privilege in self.privileges:
            print("- " + privilege.title())


class Admin(User):
    """Quản trị người dùng"""

    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = Privileges()


admin_user = Admin("Nguyen", "Van A", age=30, location="Hanoi")
admin_user.privileges.show_privileges()
