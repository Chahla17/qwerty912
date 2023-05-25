import tkinter as tk

import mysql.connector
import tkinter.ttk as ttk
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="newschema"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, description, price, quantity FROM products")

result = mycursor.fetchall()

root = tk.Tk()
root.title("Список товаров")

tv = ttk.Treeview(root)
tv.pack()

tv['columns'] = ('Название', 'Описание', 'Количество', 'Цена')

# tv.column('Название', anchor=tk.CENTER, width=200)
tv.column('Название', anchor=tk.CENTER, width=200)
tv.column('Описание', anchor=tk.CENTER, width=200)
tv.column('Количество', anchor=tk.CENTER, width=100)
tv.column('Цена', anchor=tk.CENTER, width=100)

# tv.heading('Название', text='Название', anchor=tk.CENTER)
tv.heading('Название', text='Название', anchor=tk.CENTER)
tv.heading('Описание', text='Описание', anchor=tk.CENTER)
tv.heading('Количество', text='Количество', anchor=tk.CENTER)
tv.heading('Цена', text='Цена', anchor=tk.CENTER)

for row in result:
    tv.insert('', 'end', text='', values=row)


def add_product():
    name = entry_name.get()
    description = entry_description.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    sql = "INSERT INTO products (name, description, quantity, price) VALUES (%s, %s, %s, %s)"
    values = (name, description, quantity, price)
    mycursor.execute(sql, values)
    mydb.commit()

    tv.insert('', 'end', text='', values=(name, description, quantity, price))

    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

frame_add = tk.Frame(root)
frame_add.pack(pady=10)

label_name = tk.Label(frame_add, text='Название:')
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame_add)
entry_name.grid(row=0, column=1)

label_description = tk.Label(frame_add, text='Описание:')
label_description.grid(row=1, column=0)
entry_description = tk.Entry(frame_add)
entry_description.grid(row=1, column=1)

label_quantity = tk.Label(frame_add, text='Количество:')
label_quantity.grid(row=2, column=0)
entry_quantity = tk.Entry(frame_add)
entry_quantity.grid(row=2, column=1)

label_price = tk.Label(frame_add, text='Цена:')
label_price.grid(row=3, column=0)
entry_price = tk.Entry(frame_add)
entry_price.grid(row=3, column=1)

button_add = tk.Button(frame_add, text='Добавить товар', command=add_product)
button_add.grid(row=4, columnspan=2)
print(result)
root.mainloop()