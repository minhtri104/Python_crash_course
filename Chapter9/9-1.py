class restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mô tả thông tin về nhà hàng"""
        print("Restaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """Mô phỏng việc mở cửa nhà hàng"""
        print(self.restaurant_name + " is open now!")


restaurant = restaurant("Bún chả Hương Liên", "Bún chả")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
