from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    # Tạo các tham số Diffie-Hellman (p và g)
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    # Tạo private key cho server từ tham số
    private_key = parameters.generate_private_key()
    # Tạo public key từ private key
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # 1. Tạo tham số chung
    parameters = generate_dh_parameters()
    
    # 2. Tạo cặp khóa cho Server
    private_key, public_key = generate_server_key_pair(parameters)
    
    # 3. Lưu Server Public Key vào file để Client đọc
    # Lưu ý: Trong thực tế, key này sẽ được gửi qua socket
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    print("Server: Đã tạo khóa và lưu 'server_public_key.pem' thành công.")
    # Giữ tham số private_key để tính toán shared key sau này (nếu cần mở rộng)

if __name__ == "__main__":
    main()