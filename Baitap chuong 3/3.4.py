import numpy as np

# 1. Tạo mảng toàn 0 và cập nhật phần tử thứ 5 là 1
arr_zeros = np.zeros(10, int)
arr_zeros[5] = 1
print("arr_zeros:", arr_zeros)

# 2. Tạo mảng từ 10 đến 24 và in ngược
arr_h = np.arange(10, 25)
print("arr_h đảo ngược:", arr_h[::-1])

# 3. Tạo mảng chỉ chứa các phần tử khác 0
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print("arr_1:", arr_1)

# 4. Thêm 10 và 20 vào cuối mảng
arr_1 = np.append(arr_1, [10, 20])
print("arr_1 sau khi thêm 10, 20:", arr_1)

# 5. Thêm 100 vào vị trí thứ 5
arr_1 = np.insert(arr_1, 5, 100)
print("arr_1 sau khi thêm 100:", arr_1)

# 6. Xóa các phần tử ở vị trí 0, 1, 2
arr_1 = np.delete(arr_1, [0, 1, 2])
print("arr_1 sau khi xóa:", arr_1)