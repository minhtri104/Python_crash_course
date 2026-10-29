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


restaurant = Restaurant("Bánh xèo tôm-thịt", "Bánh xèo")
restaurant1 = Restaurant("Bún chả Hương Liên", "Bún chả")
restaurant2 = Restaurant("Bún đậu mắm tôm", "Bún đậu")
restaurant3 = Restaurant("Bún bò Huế", "Bún bò")

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# restaurant.open_restaurant()
