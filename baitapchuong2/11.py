import json
import datetime

def ghi_giao_dich(data, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)  # Đọc dữ liệu cũ nếu có
    except FileNotFoundError:
        existing_data = []  # Nếu file chưa tồn tại, tạo danh sách rỗng

    existing_data.append(data)  # Thêm giao dịch mới vào dữ liệu cũ

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)  # Ghi lại file JSON

while True:
    giao_dich = input("Nhập nội dung giao dịch: ")
    thoi_gian = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    data = {
        'Thoi gian': thoi_gian,
        'Noi dung giao dich': giao_dich
    }
    
    ghi_giao_dich(data, 'giao_dich.json')

    tiep_tuc = input("Bạn có muốn ghi thêm giao dịch nữa không? (1: Có, 0: Không): ")
    if tiep_tuc == '0':
        break

print("Giao dịch đã được lưu thành công.")  