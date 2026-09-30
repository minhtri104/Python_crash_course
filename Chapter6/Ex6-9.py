favourite_places = {
    "An": ["Hà Nội", "Đà Nẵng", "Hồ Chí Minh"],
    "Bình": ["Hà Nội", "Hải Phòng", "Cần Thơ"],
    "Chi": ["Đà Nẵng", "Nha Trang", "Phú Quốc"],
}

for name, places in favourite_places.items():
    print("Địa điểm yêu thích của " + name.title() + " là: ")
    for place in places:
        print("\t" + place)
