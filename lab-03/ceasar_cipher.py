import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện click chuột cho hai nút bấm
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        
        # FIX: Sửa "plain_text" thành "plaintext" viết liền để không bị lỗi KeyError bên Server
        payload = {
            "plaintext": self.ui.txt_plain_text.toPlainText().strip(),
            "key": self.ui.txt_key.toPlainText().strip()
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)  # Debug dữ liệu API trả về

            if response.status_code == 200:
                try:
                    data = response.json()
                    # Lấy đúng key trả về từ phía API của bạn (nếu bên api.py trả về 'encrypted_message' thì đổi lại nhé)
                    encrypted_res = data.get("encrypted_text") or data.get("encrypted_message") or ""
                    self.ui.txt_cipher_text.setPlainText(encrypted_res)
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Encrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        
        # FIX: Sửa "cipher_text" thành "ciphertext" viết liền cho đồng bộ với phía Server
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText().strip(),
            "key": self.ui.txt_key.toPlainText().strip()
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)  # Debug dữ liệu API trả về

            if response.status_code == 200:
                try:
                    data = response.json()
                    # Lấy đúng key giải mã trả về từ API
                    decrypted_res = data.get("decrypted_text") or data.get("decrypted_message") or ""
                    self.ui.txt_plain_text.setPlainText(decrypted_res)
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())