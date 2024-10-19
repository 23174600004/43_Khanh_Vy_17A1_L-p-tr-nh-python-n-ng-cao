import numpy as np

# 1. Tạo array arr với kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Mảng arr 3x3 với giá trị True:\n", arr)

# 2. Tạo array arr_ID và chuyển thành 2D array
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape(3, 3)  # Chuyển thành mảng 2 chiều 3x3
print("Mảng arr_2D ban đầu:\n", arr_2D)

# Đổi cột 1 và cột 3
arr_2D[:, [1, 2]] = arr_2D[:, [2, 1]]
print("Mảng arr_2D sau khi đổi cột:\n", arr_2D)

# 3. Đổi dòng 1 và dòng 2
arr_2D[[1, 2]] = arr_2D[[2, 1]]
print("Mảng arr_2D sau khi đổi dòng:\n", arr_2D)

# 4. Đảo ngược các dòng
arr_2D_reversed_rows = arr_2D[::-1]
print("Mảng arr_2D sau khi đảo ngược dòng:\n", arr_2D_reversed_rows)

# 5. Đảo ngược các cột
arr_2D_reversed_columns = arr_2D[:, ::-1]
print("Mảng arr_2D sau khi đảo ngược cột:\n", arr_2D_reversed_columns)

# 6. Tạo arr_2D_null và kiểm tra giá trị null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9]])
print("Mảng arr_2D_null:\n", arr_2D_null)
print("Có giá trị null trong mảng không?", np.isnan(arr_2D_null).any())

# 7. Thay thế giá trị null bằng 0
arr_2D_null[np.isnan(arr_2D_null)] = 0
print("Mảng arr_2D_null sau khi thay thế giá trị null bằng 0:\n", arr_2D_null)