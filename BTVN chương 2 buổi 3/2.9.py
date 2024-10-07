import json

# Sắp xếp từ điển theo khóa
python_dict = {"name": "John", "age": 30, "city": "New York"}
sorted_dict = dict(sorted(python_dict.items()))

# Chuyển đổi sang chuỗi JSON và in với thụt lề 4
print(json.dumps(sorted_dict, indent=4))