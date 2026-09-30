age = 12

if age < 4:
    price = 0       # ①
elif age < 18:
    price = 5       # ②
else:
    price = 10      # ③

# ④ Lệnh print không thụt lề, chạy sau khi chuỗi if-elif-else kết thúc
print(f"Your admission cost is ${price}.")