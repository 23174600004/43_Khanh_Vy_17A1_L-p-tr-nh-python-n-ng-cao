import json

# Đối tượng Python
python_obj = {"name": "John", "age": 30, "city": "New York"}

# Chuyển đổi sang chuỗi JSON và in
json_str = json.dumps(python_obj)
print("Chuỗi JSON:", json_str)

# In ra các giá trị
print("Các giá trị:", python_obj.values())