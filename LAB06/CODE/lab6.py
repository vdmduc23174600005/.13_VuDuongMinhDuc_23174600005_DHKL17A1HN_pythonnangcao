import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối database
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Tạo bảng
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')
conn.commit()

# Hàm thêm sản phẩm
def add_product():
    name = entry_name.get()
    if name:
        cursor.execute('INSERT INTO Product (name) VALUES (?)', (name,))
        conn.commit()
        update_listbox()
        entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên sản phẩm!")

# Hàm xóa sản phẩm
def delete_product():
    try:
        selected_item = listbox.get(listbox.curselection())
        product_id = selected_item.split(' - ')[0]
        cursor.execute('DELETE FROM Product WHERE id = ?', (product_id,))
        conn.commit()
        update_listbox()
    except:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để xóa!")

# Cập nhật Listbox
def update_listbox():
    listbox.delete(0, tk.END)
    cursor.execute('SELECT * FROM Product')
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")

# Giao diện
root = tk.Tk()
root.title("Quản lý Sản phẩm")

tk.Label(root, text="Tên sản phẩm").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Button(root, text="Thêm", command=add_product).grid(row=1, column=0)
tk.Button(root, text="Xóa", command=delete_product).grid(row=1, column=1)

listbox = tk.Listbox(root)
listbox.grid(row=2, column=0, columnspan=2)

update_listbox()
root.mainloop()