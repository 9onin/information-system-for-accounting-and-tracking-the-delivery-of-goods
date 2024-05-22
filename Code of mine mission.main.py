
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Добро пожаловать в информационную систему учета и отслеживания доставки товаров!'

if __name__ == '__main__':
    app.run(debug=True)
import sqlite3

conn = sqlite3.connect('delivery.db')
c = conn.cursor()

# Создание таблицы для хранения заказов
c.execute('''CREATE TABLE orders
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              order_number TEXT,
              status TEXT,
              estimated_delivery_date TEXT)''')

# Внесение тестовых данных
c.execute("INSERT INTO orders (order_number, status, estimated_delivery_date) VALUES ('1', 'В пути', '2022-10-10')")
c.execute("INSERT INTO orders (order_number, status, estimated_delivery_date) VALUES ('2', 'Доставлено', '2022-09-30')")

conn.commit()
conn.close()
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/orders')
def get_orders():
    conn = sqlite3.connect('delivery.db')
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    
    orders = c.fetchall()

    conn.close()
    
    return render_template('orders.html', orders=orders)


