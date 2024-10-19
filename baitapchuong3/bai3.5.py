import numpy as np

# 1. Tạo numpy array arr_height từ list height
list_height = [71, 73, 69, 68, 74, 72, 70, 73, 72, 74]  # Dữ liệu ví dụ
arr_height = np.array(list_height)
print("Array chiều cao (inches):")
print(arr_height)

# 2. Tạo numpy array arr_weight từ list weight
list_weight = [195, 205, 175, 180, 210, 200, 185, 195, 205, 210]  # Dữ liệu ví dụ
arr_weight = np.array(list_weight)
print("Array cân nặng (pounds):")
print(arr_weight)

# 3. Chuyển chiều cao từ inch sang mét (1 inch = 0.0254 meters)
arr_height_m = arr_height * 0.0254
print("Array chiều cao (mét):")
print(arr_height_m)

# 4. Chuyển cân nặng từ pound sang kg (1 pound = 0.453592 kg)
arr_weight_kg = arr_weight * 0.453592
print("Array cân nặng (kg):")
print(arr_weight_kg)

# 5. Tính BMI của các cầu thủ (BMI = cân nặng (kg) / (chiều cao (m)^2))
arr_BMI = arr_weight_kg / (arr_height_m ** 2)
print("BMI của các cầu thủ:")
print(arr_BMI)

# 6. Tìm chiều cao và cân nặng trung bình của các cầu thủ
average_height = np.mean(arr_height)
average_weight = np.mean(arr_weight)
print("Chiều cao trung bình (inches):", average_height)
print("Cân nặng trung bình (pounds):", average_weight)

# 7. Tìm chiều cao và cân nặng lớn nhất của các cầu thủ
max_height = np.max(arr_height)
max_weight = np.max(arr_weight)
print("Chiều cao lớn nhất (inches):", max_height)
print("Cân nặng lớn nhất (pounds):", max_weight)

# 8. Tìm chiều cao và cân nặng nhỏ nhất của các cầu thủ
min_height = np.min(arr_height)
min_weight = np.min(arr_weight)
print("Chiều cao nhỏ nhất (inches):", min_height)
print("Cân nặng nhỏ nhất (pounds):", min_weight)

# 9. Lọc các cầu thủ có chiều cao nằm trong khoảng từ 70 đến 75 inches
players_in_range = (arr_height >= 70) & (arr_height <= 75)
print("Các cầu thủ có chiều cao từ 70 đến 75 inches:")
print(arr_height[players_in_range])

# 10. Lọc các cầu thủ có BMI lớn hơn 25
players_with_high_BMI = arr_BMI > 25
print("Các cầu thủ có BMI lớn hơn 25:")
print(arr_BMI[players_with_high_BMI])
