# Khai báo danh sách các nhà ảo thuật
magicians = ["alice", "david", "carolina"]

# Định nghĩa vòng lặp for
for magician in magicians:
    # in ra tên của từng nhà ảo thuật
    print(magician.title() + ", màn ảo thuật thật tuyệt vời!")
    print(
        "Tôi không thể chờ đợi để xem màn trình diễn tiếp theo của bạn,"
        + magician.title()
        + ".\n"
    )
print("Cảm ơn tất cả các nhà ảo thuật đã trình diễn hôm nay!")
