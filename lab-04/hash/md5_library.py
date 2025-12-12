import hashlib

def calculate_md5(input_string):
    # Khởi tạo đối tượng MD5
    md5_hash = hashlib.md5()
    # Cập nhật dữ liệu cần băm (phải encode sang bytes)
    md5_hash.update(input_string.encode('utf-8'))
    # Trả về chuỗi hex
    return md5_hash.hexdigest()

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash = calculate_md5(input_string)
    print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))