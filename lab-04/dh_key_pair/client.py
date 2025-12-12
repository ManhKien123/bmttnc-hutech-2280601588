from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
# Import các thư viện hỗ trợ (theo tài liệu)
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    # Tạo private key cho client dựa trên tham số của server
    private_key = parameters.generate_private_key()
    # Tạo public key
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    # Tính toán shared secret bằng cách trao đổi khóa
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    try:
        # 1. Đọc Public Key của Server từ file
        with open("server_public_key.pem", "rb") as f:
            server_public_key = serialization.load_pem_public_key(f.read())
        
        # 2. Lấy tham số (p, g) từ Public Key của Server
        parameters = server_public_key.parameters()
        
        # 3. Tạo cặp khóa cho Client
        private_key, public_key = generate_client_key_pair(parameters)
        
        # 4. Tính toán Shared Secret
        # (Client dùng Private Key của mình + Public Key của Server)
        shared_secret = derive_shared_secret(private_key, server_public_key)
        
        print("Shared Secret:", shared_secret.hex())
        
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file 'server_public_key.pem'. Hãy chạy server.py trước.")

if __name__ == "__main__":
    main()