import sqlite3

# Kết nối với cơ sở dữ liệu
conn = sqlite3.connect('product.db')
cursor = conn.cursor()

# Tạo bảng
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    )
''')
conn.commit()
conn.close()