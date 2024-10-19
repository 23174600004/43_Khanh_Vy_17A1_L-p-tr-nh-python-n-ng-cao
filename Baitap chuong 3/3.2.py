import numpy as np

# Tạo numpy array với giá trị từ 0 đến 9
arr = np.arange(10)

# Hiển thị các phần tử có trong arr
print("Array arr:", arr)

# Hiển thị kiểu dữ liệu của arr
print("Kiểu dữ liệu của arr:", arr.dtype)

# Hiển thị kích thước của arr
print("Kích thước của arr:", arr.shape)


# Tạo array các phần tử lẻ
arr_odd = arr[arr % 2 != 0]

# Tạo array các phần tử chẵn
arr_even = arr[arr % 2 == 0]

# Hiển thị arr_odd và arr_even
print("Các phần tử lẻ trong arr:", arr_odd)
print("Các phần tử chẵn trong arr:", arr_even)

# Tạo array arr_update_1 với phần tử chẵn giữ nguyên, phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)

# Hiển thị arr_update_1
print("arr_update_1 với các phần tử lẻ thay bằng 100:", arr_update_1)