import numpy as np

# 1. Đọc dữ liệu từ file và tạo mảng 2D
baseball = np.loadtxt('baseball_2D.txt', delimiter=',')
print("Kiểu dữ liệu:", baseball.dtype)
print("Kích thước:", baseball.shape)

# 2. In giá trị dòng thứ 50
print("Dòng thứ 50:", baseball[49])

# 3. Tạo mảng với dữ liệu từ cột hai (cân nặng)
np_weight = baseball[:, 1]

# 4. Chiều cao của vận động viên thứ 124
print("Chiều cao vận động viên thứ 124:", baseball[123, 0])

# 5. Chiều cao trung bình và cân nặng trung bình
avg_height = np.mean(baseball[:, 0])
avg_weight = np.mean(np_weight)
print("Chiều cao trung bình:", avg_height)
print("Cân nặng trung bình:", avg_weight)

# 6. Nhận xét mối tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(baseball[:, 0], np_weight)[0, 1]
correlation_type = "tương quan thuận" if correlation > 0 else "tương quan nghịch" if correlation < 0 else "không có tương quan"
print("Mối tương quan:", correlation_type)
print("Hệ số tương quan:", correlation)




75,200
68,150
70,160
74,190
73,185
76,210
69,155
71,170
75,195
80,230