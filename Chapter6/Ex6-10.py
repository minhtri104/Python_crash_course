favorite_numbers = {
    "An": [7, 14],
    "Bình": [3, 9, 27],
    "Chi": [12],
    "Dũng": [42, 100],
}

for name, numbers in favorite_numbers.items():
    print("Số yêu thích của " + name.title() + " là: ")
    for number in numbers:
        print("\t" + str(number))
