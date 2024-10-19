import numpy as np
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1
print("Array arr_zeros:", arr_zeros)
arr_h = np.arange(10, 25)
print("Array arr_h theo thứ tự đảo ngược:", arr_h[::-1])
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = arr_k[arr_k != 0]
print("Array arr_l với các phần tử khác 0:", arr_l)
arr_l = np.append(arr_l, [10, 20])
print("Array arr_l sau khi thêm phần tử 10 và 20:", arr_l)
arr_l = np.insert(arr_l, 5, 100)
print("Array arr_l sau khi thêm phần tử 100:", arr_l)
arr_l = np.delete(arr_l, [0, 1, 2])
print("Array arr_l sau khi xóa các phần tử tại vị trí index = 0, 1, 2:", arr_l)
