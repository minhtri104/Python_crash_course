# in list số tuwef 1 đến 5
numbers = list(range(1, 6))
print(numbers)

# in list số chẵn từ 2 đến 10
even_number = list(range(2, 11, 2))
print(even_number)

# in list số lẻ từ 1 đến 9
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

# in list số 10 số bình phương đầu tiên vào 1 danh sách
# Bắt đầu với 1 danh sách rỗng
squares = []

# lặp qua các giá trị từ 1 đến 10
for value in range(1, 11):
    # tính bình phương của giá trị hiện tại và lưu vào biến square
    # thêm giá trị bình phương vào danh sách squares
    squares.append(value**2)
# in danh sách các số bình phương
print(squares)
