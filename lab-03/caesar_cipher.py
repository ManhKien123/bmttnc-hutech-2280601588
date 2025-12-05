import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.encryptButton.clicked.connect(self.call_api_encrypt)
        self.ui.decryptButton.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "https://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plaintext": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.value()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption successful!")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
        def call_api_decrypt(self):
            url = "https://127.0.0.1:5000/api/caesar/decrypt"
            payload = {
                "ciphertext": self.ui.txt_cipher_text.toPlainText(),
                "key": self.ui.txt_key.value()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_plain_text.setText(data["decrypted_message"])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decryption successful!")
                    msg.exec_()
                else:
                    print("Error while calling API")
            except requests.exceptions.RequestException as e:
                print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MyApp()
    Window.show()
    sys.exit(app.exec_())