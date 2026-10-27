def show_magicians(magicians):
    """In tên các ảo thuật gia trong danh sách"""
    for magician in magicians:
        print(magician)


# 8-10 thêm hàm make_great()
def make_great(magicians):
    """Thêm  cụ từ 'the Great' vào tên từng ảo thuật gia trong danh sách"""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great."


# Danh sách các ảo thuật gia
magicians_list = ["Harry Houdini", "David Copperfield", "Penn Jillette", "Teller"]

# Hiển thị tên các ảo thuật gia
show_magicians(magicians_list)
