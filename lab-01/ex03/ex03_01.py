def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhap danh sach so tu nguoi dung va xu ly chuoi
input_list = input("Nhập danh sách số, cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))

# Su dung ham va in ket qua
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", tong_chan)