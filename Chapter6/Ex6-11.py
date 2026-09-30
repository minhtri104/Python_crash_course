cities = {
    "tokyo": {
        "country": "nhật bản",
        "population": "37.4 triệu",
        "fact": "Là vùng đô thị đông dân nhất thế giới.",
    },
    "paris": {
        "country": "pháp",
        "population": "2.1 triệu",
        "fact": "Được mệnh danh là Kinh đô Ánh sáng.",
    },
    "ha noi": {
        "country": "việt nam",
        "population": "8.4 triệu",
        "fact": "Có lịch sử hơn 1000 năm tuổi văn hiến.",
    },
}

for city, city_info in cities.items():
    print(f"\nThành phố: {city.title()}")
    print(f"\tQuốc gia: {city_info['country'].title()}")
    print(f"\tDân số: {city_info['population']}")
    print(f"\tSự thật thú vị: {city_info['fact']}")
