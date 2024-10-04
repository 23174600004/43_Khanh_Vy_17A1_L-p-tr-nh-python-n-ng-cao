from xml.dom import minidom

# Đọc và phân tích cú pháp file XML
doc = minidom.parse('students.xml')

# Lấy danh sách tất cả sinh viên
students = doc.getElementsByTagName('student')

# Duyệt qua từng sinh viên và in ra thông tin
for student in students:
    student_id = student.getElementsByTagName('student_id')[0].firstChild.data
    name = student.getElementsByTagName('name')[0].firstChild.data
    birth_year = student.getElementsByTagName('birth_year')[0].firstChild.data
    class_name = student.getElementsByTagName('class')[0].firstChild.data
    gender = student.getElementsByTagName('gender')[0].firstChild.data

    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Birth Year: {birth_year}")
    print(f"Class: {class_name}")
    print(f"Gender: {gender}")
    print("-" * 30)