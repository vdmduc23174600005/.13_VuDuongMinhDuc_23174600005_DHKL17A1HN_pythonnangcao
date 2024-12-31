import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối cơ sở dữ liệu
def connect_db():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    return conn, cursor

# Hàm thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    amount = entry_amount.get()
    if name and price and amount:
        conn, cursor = connect_db()
        cursor.execute('INSERT INTO product (name, price, amount) VALUES (?, ?, ?)', (name, float(price), int(amount)))
        conn.commit()
        conn.close()
        update_listbox()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")

# Hàm cập nhật danh sách sản phẩm trong Listbox
def update_listbox():
    listbox.delete(0, tk.END)
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM product')
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]} | Tên: {row[1]} | Giá: {row[2]} | Số lượng: {row[3]}")
    conn.close()

# Hàm xóa sản phẩm
def delete_product():
    try:
        selected = listbox.get(listbox.curselection())
        product_id = selected.split(' ')[1]
        conn, cursor = connect_db()
        cursor.execute('DELETE FROM product WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        update_listbox()
    except:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm để xóa!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý Sản phẩm")

# Widgets
tk.Label(root, text="Tên sản phẩm").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Giá").grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

tk.Label(root, text="Số lượng").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Button(root, text="Thêm sản phẩm", command=add_product).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Xóa sản phẩm", command=delete_product).grid(row=4, column=0, columnspan=2)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=5, column=0, columnspan=2)

# Hiển thị danh sách ban đầu
update_listbox()

root.mainloop()