{
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abe Giải Phóng - Hà Nội",
        "employees": [
            {"name": "Nguyễn Văn A", "unit": "Đơn vị AI"},
            {"name": "Trần Thị B", "unit": "Đơn vị A2"},
            {"name": "Phạm Văn C", "unit": "Đơn vị A3"},
            {"name": "Nguyễn Thị D", "unit": "Đơn vị AI"},
            {"name": "Lê Văn E", "unit": "Đơn vị A4"},
            {"name": "Phan Văn F", "unit": "Đơn vị A2"}
        ]
    }
}
import json
from collections import Counter

# Dữ liệu JSON
data = {
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abe Giải Phóng - Hà Nội",
        "employees": [
            {"name": "Nguyễn Văn A", "unit": "Đơn vị AI"},
            {"name": "Trần Thị B", "unit": "Đơn vị A2"},
            {"name": "Phạm Văn C", "unit": "Đơn vị A3"},
            {"name": "Nguyễn Thị D", "unit": "Đơn vị AI"},
            {"name": "Lê Văn E", "unit": "Đơn vị A4"},
            {"name": "Phan Văn F", "unit": "Đơn vị A2"}
        ]
    }
}

# Thống kê nhân viên
employees = data["company"]["employees"]
total = len(employees)
units = Counter(emp["unit"] for emp in employees)

# In thông tin công ty
print(f"Tên công ty: {data['company']['name']}\nĐịa chỉ: {data['company']['address']}\nTổng số nhân viên: {total}\n")
print("----- Thống kê nhân viên theo đơn vị --------")
for i, (unit, count) in enumerate(units.items(), 1):
    print(f"{i}/ Tên đơn vị: {unit}.\n- Số nhân viên: {count}\n- Tỷ lệ: {count / total * 100:.2f}%\n")
