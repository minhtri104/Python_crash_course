person_1 = {
    "first_name": "Trí",
    "last_name": "Nguyễn",
    "age": 21,
    "city": "Thành phố Hồ Chí Minh",
}

person_2 = {
    "first_name": "Linh",
    "last_name": "Trần",
    "age": 22,
    "city": "Đà Nẵng",
}

person_3 = {
    "first_name": "Nam",
    "last_name": "Lê",
    "age": 30,
    "city": "TP. Hồ Chí Minh",
}

people = [person_1, person_2, person_3]

for person in people:
    print(
        person["first_name"].title()
        + " "
        + person["last_name"].title()
        + " is "
        + str(person["age"])
        + " years old and lives in "
        + person["city"]
        + "."
    )
