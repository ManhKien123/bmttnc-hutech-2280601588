def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhap danh sach so tu nguoi dung
input_string = input("Nhập danh sách số, cách nhau bằng dấu cách: ")
word_list = input_string.split()

# Su dung ham va in ket qua
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử:", so_lan_xuat_hien)