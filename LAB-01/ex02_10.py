# Sửa lại thành không dấu hoàn toàn
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
# Đảm bảo tên ở đây giống hệt tên ở trên dòng 1
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))