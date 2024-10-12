import json

with open('thongkenvien.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

ten_cong_ty = data["Ten cong ty"]
dia_chi = data["Dia chi"]
nhan_vien = data["nhanVien"]

tong_so_nhan_vien = sum(dv["So nhan vien"] for dv in nhan_vien)

print(f"Tên công ty: {ten_cong_ty}")
print(f"Địa chỉ: {dia_chi}")
print(f"Tổng số nhân viên: {tong_so_nhan_vien}")
print("\n----- THỐNG KÊ NHÂN VIÊN -----")

for dv in nhan_vien:
    ten_don_vi = dv["Ten don vi"]
    so_nhan_vien = dv["So nhan vien"]
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"{ten_don_vi}: {so_nhan_vien} nhân viên, Tỷ lệ: {ty_le:.2f}%")
