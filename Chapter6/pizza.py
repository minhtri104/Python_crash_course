# Lưu trữ thông tin về một chiếc pizza đang được đặt.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# Tóm tắt đơn hàng.
print(
    "You ordered a " + pizza["crust"] + "-crust pizza " + "with the following toppings:"
)

for topping in pizza["toppings"]:
    print("\t" + topping)
