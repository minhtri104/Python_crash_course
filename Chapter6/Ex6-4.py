glossary = {
    "variable": "Vùng không gian bộ nhớ dùng để lưu trữ giá trị dữ liệu.",
    "list": "Cấu trúc dữ liệu dùng để lưu trữ một tập hợp các phần tử theo thứ tự.",
    "string": "Một chuỗi các ký tự được đặt trong cặp dấu ngoặc đơn hoặc ngoặc kép.",
    "dictionary": "Tập hợp các cặp khóa - giá trị dùng để liên kết dữ liệu có quan hệ với nhau.",
    "loop": "Cấu trúc điều khiển dùng để lặp lại một khối lệnh nhiều lần.",
    "statement": "Một câu lệnh thực thi một hành động trong chương trình.",
    "key": "Thành phần chỉ số định danh trong dictionary dùng để truy xuất giá trị.",
    "value": "Dữ liệu được liên kết với một khóa cụ thể trong dictionary.",
    "boolean": "Kiểu dữ liệu logic chỉ nhận một trong hai giá trị: True hoặc False.",
    "method": "Một hàm được gắn liền và thực thi trên một đối tượng cụ thể.",
}

for word, definition in glossary.items():
    print(f"{word.title()}:\n\t{definition}\n")
