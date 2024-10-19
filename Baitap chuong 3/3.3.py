import numpy as np

arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])

arr_c = np.intersect1d(arr_a, arr_b)  # Phần tử xuất hiện ở cả arr_a và arr_b
arr_d = np.setdiff1d(arr_a, arr_b)    # Phần tử chỉ xuất hiện ở arr_a
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]  # Phần tử từ 5 đến 10 trong arr_e

print("arr_c:", arr_c)
print("arr_d:", arr_d)
print("arr_f:", arr_f)
