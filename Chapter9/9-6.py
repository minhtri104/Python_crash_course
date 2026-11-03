class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Mô tả thông tin về nhà hàng"""
        print("\nRestaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """Mô phỏng việc mở cửa nhà hàng"""
        print(self.restaurant_name + " is open now!")

    def set_number_served(self, number):
        """Đặt số lượng khách hàng đã phục vụ"""
        self.number_served = number

    def increment_number_served(self, number):
        """Tăng số lượng khách hàng đã phục vụ"""
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "blueberry", "matcha"]

    def display_flavors(self):
        """Hiển thị các hương vị kem"""
        print("Các hương vị kem có sẵn:")
        for flavor in self.flavors:
            print("- " + flavor.title())


ice_cream_stand = IceCreamStand("Kem Ngon", "Kem")
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()
