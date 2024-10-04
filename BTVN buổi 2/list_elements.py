from xml.dom import minidom

# Đọc và phân tích cú pháp file XML
doc = minidom.parse('sample.xml')

# Lấy danh sách tất cả các phần tử trong file XML
elements = doc.getElementsByTagName('*')  # Dùng '*' để lấy tất cả các phần tử

# In ra tên của từng phần tử
print("List of elements in the XML:")
for element in elements:
    print(element.tagName)