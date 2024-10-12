import requests

url = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = requests.get(url)

if response.status_code == 200:
    comments = response.json()  # Chuyển đổi dữ liệu thành JSON

    print("Danh sách các bài post nổi bật (giới hạn 3 bài đầu):")
    for comment in comments[:3]:
        print(f"\nID: {comment['id']}")
        print(f"Tên: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Nội dung: {comment['body']}")
else:
    print("Không thể lấy dữ liệu từ API.")
