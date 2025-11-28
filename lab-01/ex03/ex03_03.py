def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhap danh sach so tu nguoi dung va xu ly chuoi
input_list = input("Nhập danh sách số, cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ List: ", my_tuple)  