# Trò chơi đoán số bí mật
so_bi_mat = 7

print("CHÀO MỪNG BẠN ĐẾN VỚI TRÒ CHƠI ĐOÁN SỐ BÍ MẬT!")
print("Tôi đã chọn một số bí mật từ 1 đến 10. Hãy thử đoán xem nó là số nào!")

# Sử dụng vòng lặp để người chơi đoán đến khi đúng
while True:
    so_doan = int(input("Nhập số bạn đoán: "))

    if so_doan == so_bi_mat:
        print("🎉 Chúc mừng! Bạn đã đoán đúng số bí mật!")
        break  # Thoát khỏi vòng lặp khi đoán đúng
    elif so_doan < so_bi_mat:
        print("📉 Số bạn đoán quá thấp. Hãy thử lại!")
    elif so_doan > so_bi_mat:
        print("📈 Số bạn đoán quá cao. Hãy thử lại!")
    else:
        print("⚠️ Đầu vào không hợp lệ. Vui lòng nhập một số từ 1 đến 10.")
