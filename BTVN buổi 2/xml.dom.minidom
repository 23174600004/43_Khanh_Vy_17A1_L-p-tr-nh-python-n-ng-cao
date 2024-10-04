from xml.dom import minidom

# Đọc và phân tích cú pháp file XML
doc = minidom.parse('sample.xml')

# Lấy các phần tử trong file XML
catalog = doc.getElementsByTagName('catalog')[0]
books = doc.getElementsByTagName('book')

# Duyệt qua các phần tử 'book' và in ra thông tin
for book in books:
    author = book.getElementsByTagName('author')[0].firstChild.data
    title = book.getElementsByTagName('title')[0].firstChild.data
    genre = book.getElementsByTagName('genre')[0].firstChild.data
    price = book.getElementsByTagName('price')[0].firstChild.data
    publish_date = book.getElementsByTagName('publish_date')[0].firstChild.data
    description = book.getElementsByTagName('description')[0].firstChild.data

    print(f"Author: {author}")
    print(f"Title: {title}")
    print(f"Genre: {genre}")
    print(f"Price: {price}")
    print(f"Publish Date: {publish_date}")
    print(f"Description: {description}")
    print("-" * 30)
