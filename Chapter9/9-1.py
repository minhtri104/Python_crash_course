class restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mô tả thông tin về nhà hàng"""
        print("\nRestaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """Mô phỏng việc mở cửa nhà hàng"""
        print(self.restaurant_name + " is open now!")


restaurant1 = restaurant("Bún chả Hương Liên", "Bún chả")
restaurant2 = restaurant("Bún đậu mắm tôm", "Bún đậu")
restaurant3 = restaurant("Bún bò Huế", "Bún bò")

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# restaurant.open_restaurant()
