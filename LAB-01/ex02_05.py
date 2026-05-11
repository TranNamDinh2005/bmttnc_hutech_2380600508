# Nhập dữ liệu từ bàn phím
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# Các thông số cố định
gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần

# Tính số giờ làm vượt chuẩn (dùng hàm max để nếu làm ít hơn 44h thì số giờ vượt là 0)
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập
# Lương = (Giờ chuẩn * Mức lương) + (Giờ vượt * Mức lương * 1.5)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

# In kết quả ra màn hình
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")