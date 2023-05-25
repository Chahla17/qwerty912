import tkinter as tk
from tkinter import messagebox
from mysql.connector import connect
import datetime
app = tk.Tk()
app.title('dsadsadasdsadsadsadasdasda')
app.minsize(600,400)
for i in range(4):
    app.columnconfigure(i, weight=1)
    app.rowconfigure(i, weight=1)
full_name_label = tk.Label(app, text='ФИО Клиента')
full_name = tk.Entry(app, width=30)
full_name_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
full_name.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
status_label = tk.Label(app, text='status')
status = tk.Entry(app, width=30)
status_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
status.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
price_label = tk.Label(app, text='Цена')
price = tk.Entry(app, width=30)
price_label.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
price.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')
description_label = tk.Label(app, text='Описание')
description = tk.Entry(app, width=63)
description_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
description.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
def create_order():
    connection = connect(host = 'localhost', username='root', password='12345678', database='newschema')
    c = connection.cursor()
    query = "INSERT INTO orders(full_name,status,price,description,date_created) VALUES (%s,%s,%s,%s,%s)"
    date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values =(
        full_name.get(),
        status.get(),
        price.get(),
        description.get(),
        date_now
    )
    c.execute(query,values)
    connection.commit()
    c.close()
    connection.close()
    messagebox.showinfo('Уведомление','Выполнен')
def show_products():
    connection = connect(host='localhost', username='root', password='12345678', database='newschema')
    c = connection.cursor()
    query = 'SELECT * FROM products'
    c.execute(query)
    products = c.fetchall()
    products_str = 'Список товаров:\n\n'
    for product in products:
        product_name = product[0]
        product_price = product[3]
        products_str += f'{product_name} {product_price} руб.\n'
    messagebox.showinfo('Товары', products_str)
    c.close()
    connection.close()
show_products_button = tk.Button(app, text='Показать товары', width=30, height=5, command=show_products)
show_products_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
submit = tk.Button(app, text='Создать заказ', width=30, height=5, command=create_order)
submit.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
app.mainloop()
