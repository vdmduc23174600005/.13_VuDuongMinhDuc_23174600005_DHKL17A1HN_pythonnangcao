import numpy as np
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 3, 4, 9, 8])
arr_e = np.intersect1d(arr_a, arr_b)
print("Array các phần tử xuất hiện ở cả arr_a và arr_b (arr_e):", arr_e)
arr_d = np.setdiff1d(arr_b, arr_a)
print("Array các phần tử chỉ xuất hiện ở arr_b (arr_d):", arr_d)
arr_c = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = arr_c[(arr_c >= 5) & (arr_c <= 10)]
print("Array arr_f chứa các phần tử có giá trị từ 5 đến 10:", arr_f)
