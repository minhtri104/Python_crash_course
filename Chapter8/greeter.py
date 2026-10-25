def get_fommated_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nVui lòng cho tôi biết tên của bạn:")
    print("(nhập 'q' bất cứ lúc nào để thoát)")

    f_name = input("Tên (First name): ")
    if f_name.lower() == "q":
        break

    l_name = input("Họ (Last name): ")
    if l_name == "q":
        break

    formatted_name = get_fommated_name(f_name, l_name)
    print("\nXin chào, " + formatted_name + "!")
