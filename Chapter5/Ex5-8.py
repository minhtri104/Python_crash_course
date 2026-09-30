current_users = ["trí", "hùng", "hải", "huy", "admin"]
new_users = ["Trí", "nam", "Minh", "Hải", "ADMIN"]

# Tạo một danh sách mới chứa tatats cả tên trong current_users duosi dạng chữ thường
# So sánh khong phân biệt chữ hoa chữ thường
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Tên {new_user} đã được sử dụng. Vui lòng chọn một tên khác.")
    else:
        print(f"Tên {new_user} còn available.")
