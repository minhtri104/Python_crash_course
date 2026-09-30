# 1. So sánh bằng và không bằng với chuỗi
fruit = "apple"
print("Is fruit == 'apple'? I predict True.")
print(fruit == "apple")

print("Is fruit != 'apple'? I predict False.")
print(fruit != "apple")


# 2. Phép thử sử dụng hàm lower()
name = "John"
print("\nIs name.lower() == 'john'? I predict True.")
print(name.lower() == "john")

print("Is name.lower() == 'John'? I predict False.")
print(name.lower() == "John")


# 3. Phép thử số học
age = 20
print("\nIs age == 20? I predict True.")
print(age == 20)

print("Is age != 20? I predict False.")
print(age != 20)

print("Is age > 18? I predict True.")
print(age > 18)

print("Is age < 18? I predict False.")
print(age < 18)

print("Is age >= 20? I predict True.")
print(age >= 20)

print("Is age <= 19? I predict False.")
print(age <= 19)


# 4. Phép thử sử dụng từ khóa 'and' và 'or'
x = 15
y = 25
print("\nIs x > 10 and y > 20? I predict True.")
print(x > 10 and y > 20)

print("Is x > 10 and y < 20? I predict False.")
print(x > 10 and y < 20)

print("Is x > 20 or y > 20? I predict True.")
print(x > 20 or y > 20)

print("Is x > 20 or y < 20? I predict False.")
print(x > 20 or y < 20)


# 5. Kiểm tra phần tử có nằm trong danh sách (in)
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print("mushrooms" in requested_toppings)

print("Is 'pepperoni' in requested_toppings? I predict False.")
print("pepperoni" in requested_toppings)


# 6. Kiểm tra phần tử không nằm trong danh sách (not in)
banned_users = ["andrew", "carolina", "david"]
user = "marie"
print("\nIs 'marie' not in banned_users? I predict True.")
print(user not in banned_users)

print("Is 'andrew' not in banned_users? I predict False.")
print("andrew" not in banned_users)
