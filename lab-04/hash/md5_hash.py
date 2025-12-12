#Khong dung thu vien ngoai
import math
# Hàm xoay bit trái
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo các biến ban đầu (Standard Magic Numbers)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length = len(message) * 8
    message += b'\x80'
    
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
        
    message += original_length.to_bytes(8, 'little')

    # Bảng hằng số sine (K table)
    k = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
    
    # Số lượng dịch chuyển (Shift amounts)
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

    # Chia chuỗi thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        
        A, B, C, D = a, b, c, d
        
        # Vòng lặp chính của thuật toán MD5 (64 vòng)
        for j in range(64):
            if j < 16:
                f = (B & C) | ((~B) & D)
                g = j
            elif j < 32:
                f = (D & B) | ((~D) & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                f = C ^ (B | (~D))
                g = (7 * j) % 16
            
            temp = D
            D = C
            C = B
            B = (B + left_rotate((A + f + k[j] + words[g]) & 0xFFFFFFFF, s[j])) & 0xFFFFFFFF
            A = temp
            
        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF

    # Trả về chuỗi hex (Little Endian)
    return '{:08x}{:08x}{:08x}{:08x}'.format(
        int.from_bytes(a.to_bytes(4, 'little'), 'big'),
        int.from_bytes(b.to_bytes(4, 'little'), 'big'),
        int.from_bytes(c.to_bytes(4, 'little'), 'big'),
        int.from_bytes(d.to_bytes(4, 'little'), 'big')
    )

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash = md5(input_string.encode('utf-8'))
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")