import sqlite3

# Подключение к БД
connection = sqlite3.connect('not_telegram.db')

# Создание объекта курсора
cursor = connection.cursor()

# Создание таблицы Users
# id       - целочисло, первичный ключ
# username - текст (не пустой)
# email    - текст (не пустой)
# age      - целое число
# balance  - целое число (не пустой)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL, 
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Цикл заполняет БД 10-ю записями
# for i in range(1, 11):
#     cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

# Цикл обновляет balance у каждой 2-ой записи, начиная с 1-ой на 500
# for i in range(1, 11, 2):
#     cursor.execute(" UPDATE Users SET balance = ? WHERE username = ?", (500,f"User{i}"))

# Цикл удаляет 3-ю запись в таблице начиная с 1-ой
# for i in range(1, 11, 3):
#     cursor.execute(" DELETE FROM Users WHERE username = ?", (f"User{i}",))

# Выборка всех записей при помощи fetchall(), где возраст не равен 60
cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")


connection.commit()
connection.close()