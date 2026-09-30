# Tạo một list rỗng để lưu trữ các alien.
aliens = []

# Khởi tạo 30 alien màu xanh lá.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# # Hiển thị 5 alien đầu tiên:
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# Hiển thị tổng số alien đã tạo.
print("Total number of aliens: " + str(len(aliens)))
