def dao_nguoc_list(lst):
    return lst[::-1]

# Nhap danh sach so tu nguoi dung va xu ly chuoi
input_list = input("Nhập danh sách số, cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))

# Su dung ham va in ket qua
list_dao_nguoc = dao_nguoc_list(numbers)
print("List đảo ngược là:", list_dao_nguoc)