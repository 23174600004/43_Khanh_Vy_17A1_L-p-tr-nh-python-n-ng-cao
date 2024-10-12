


# Lấy dữ liệu từ API
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

# Hiển thị danh sách các bài post
def display_posts(posts):
    print(f"Tổng số bài post: {len(posts)}")
    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)

# Thực thi chương trình
posts = fetch_posts()
if posts:
    display_posts(posts)

import urllib.request
import json

# Lấy dữ liệu từ API
url = "https://jsonplaceholder.typicode.com/posts"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
posts = json.loads(data)

# Hiển thị thông tin bài post
print(f"Tổng số bài post: {len(posts)}")
for post in posts:
    print(f"UserID: {post['userId']}, ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}\n{'-' * 40}")