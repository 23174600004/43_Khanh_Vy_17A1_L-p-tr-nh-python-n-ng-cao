from xml.dom import minidom

# Đọc và phân tích cú pháp file XML
doc = minidom.parse('company.xml')

# Lấy tên công ty
company_name = doc.getElementsByTagName('name')[0].firstChild.data

# Lấy thông tin giám đốc
director_name = doc.getElementsByTagName('director')[0].getElementsByTagName('name')[0].firstChild.data
director_email = doc.getElementsByTagName('director')[0].getElementsByTagName('email')[0].firstChild.data

# Lấy thông tin địa chỉ
street = doc.getElementsByTagName('address')[0].getElementsByTagName('street')[0].firstChild.data
city = doc.getElementsByTagName('address')[0].getElementsByTagName('city')[0].firstChild.data
postal_code = doc.getElementsByTagName('address')[0].getElementsByTagName('postal_code')[0].firstChild.data

# Lấy thông tin liên lạc
phone = doc.getElementsByTagName('phone')[0].firstChild.data
fax = doc.getElementsByTagName('fax')[0].firstChild.data

# Lấy mã số thuế
tax_id = doc.getElementsByTagName('tax_id')[0].firstChild.data

# In ra các thông tin đã lấy được
print(f"Company Name: {company_name}")
print(f"Director Name: {director_name}")
print(f"Director Email: {director_email}")
print(f"Address: {street}, {city}, Postal Code: {postal_code}")
print(f"Phone: {phone}, Fax: {fax}")
print(f"Tax ID: {tax_id}")