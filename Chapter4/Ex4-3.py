"""
# 4-3 in từ 1 đến 20
for number in range(1, 21):
    print(number)
# 4-4 in từ 1 đến 1000000
for number in range(1, 1000001):
    print(number)
"""

# 4-5 Tính tổng một triệu số
# S = (n*(a+b))/2
# n = (b-a+1)
# numbers = list(range(1, 1000001))

# print("Số nhỏ nhất:", min(numbers))
# print("Số lớn nhất:", max(numbers))
# print("Tổng từ 1 đến 1,000,000:", sum(numbers))

# 4-6 In các số lẻ từ 1 đến 20
# numbers = list(range(1, 21, 2))
# print(numbers)

# 4-7 bội số của 3
# threes = list(range(3, 31, 3))
# print(threes)

# 4-8, 4-9 Số lập phương
# cubes = [value**3 for value in range(1, 11)]
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)
