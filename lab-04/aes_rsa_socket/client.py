from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import sys # Thêm sys để thoát chương trình sạch sẽ

# 1. Kết nối đến Server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# 2. Tạo khóa RSA client
client_key = RSA.generate(2048)

# 3. Trao đổi khóa
# Nhận Public Key của Server
server_public_key = RSA.import_key(client_socket.recv(2048))
# Gửi Public Key của Client cho Server
client_socket.send(client_key.publickey().export_key(format='PEM'))

# 4. Nhận và giải mã AES Key
encrypted_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)

# Hàm mã hóa
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Hàm giải mã
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

# Hàm chỉ làm nhiệm vụ NHẬN tin nhắn
def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            # Kiểm tra nếu server ngắt kết nối
            if not encrypted_message:
                print("\nServer disconnected.")
                client_socket.close()
                sys.exit() # Thoát chương trình
            
            decrypted_message = decrypt_message(aes_key, encrypted_message)
            # In ra dòng này để không bị đè lên dòng nhập liệu
            print(f"\nReceived: {decrypted_message}")
            print("Enter message (type 'exit' to quit): ", end="", flush=True)
            
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            break

# BẮT ĐẦU CHƯƠNG TRÌNH CHÍNH

# 1. Khởi chạy luồng nhận tin nhắn riêng biệt (Background Thread) [cite: 381]
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True # Giúp thread tự tắt khi chương trình chính tắt
receive_thread.start()

# 2. Luồng chính dùng để NHẬP và GỬI tin nhắn 
try:
    while True:
        message = input("Enter message (type 'exit' to quit): ")
        
        if message == "exit":
            # Gửi tin nhắn exit để server biết mà ngắt
            encrypted_message = encrypt_message(aes_key, message)
            client_socket.send(encrypted_message)
            break
            
        encrypted_message = encrypt_message(aes_key, message)
        client_socket.send(encrypted_message)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    client_socket.close()
    print("Connection closed.")