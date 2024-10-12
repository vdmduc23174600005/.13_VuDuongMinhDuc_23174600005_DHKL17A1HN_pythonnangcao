import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # Chuyển dữ liệu thành JSON

    print(f"Tổng số bài post: {len(posts)}")

    for post in posts:
        print(f"UserID: {post['userId']}, ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print("Không thể lấy dữ liệu từ API.")
