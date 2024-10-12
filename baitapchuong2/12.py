import requests

# URL của API
url = "https://jsonplaceholder.typicode.com/posts"

# Gửi yêu cầu GET để lấy dữ liệu từ API
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    posts = response.json()  # Chuyển dữ liệu thành JSON

    # Hiển thị tổng số bài post
    print(f"Tổng số bài post: {len(posts)}")

    # Duyệt và in thông tin từng bài post
    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print("Không thể lấy dữ liệu từ API.")