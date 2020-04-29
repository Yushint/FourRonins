class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(20) UNIQUE,
                             password_hash VARCHAR(128),
                             email VARCHAR(20),
                             is_admin INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password_hash, email, is_admin=False):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash, email, is_admin) 
                          VALUES (?,?,?,?)''',
                       (user_name, password_hash, email, int(is_admin)))
        cursor.close()
        self.connection.commit()

    def exists(self, user_name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ?", [user_name])
        row = cursor.fetchone()
        return (True, row[2], row[0]) if row else (False,)

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows


class DealersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS dealers 
                            (dealer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             name VARCHAR(20) UNIQUE,
                             address VARCHAR(128)
                        )''')
        cursor.close()
        self.connection.commit()

    def insert(self, name, address):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO dealers 
                          (name, address) 
                          VALUES (?,?)''',
                       (name, address))
        cursor.close()
        self.connection.commit()

    def exists(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers WHERE name = ?",
                       name)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get(self, dealer_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers WHERE dealer_id = ?", (str(dealer_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM dealers")
        rows = cursor.fetchall()
        return rows

    def delete(self, dealer_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM dealers WHERE dealer_id = ?''', (str(dealer_id)))
        cursor.close()
        self.connection.commit()


class CarsModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars 
                            (car_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             model VARCHAR(20),
                             price INTEGER,
                             power INTEGER,
                             color VARCHAR(20),
                             dealer INTEGER
                        )''')
        cursor.close()
        self.connection.commit()

    def insert(self, model, price, power, color, dealer):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO cars 
                          (model, price, power, color, dealer) 
                          VALUES (?,?,?,?,?)''',
                       (model, str(price), str(power), color, str(dealer)))
        cursor.close()
        self.connection.commit()

    def exists(self, model):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cars WHERE model = ?",
                       model)
        row = cursor.fetchone()
        return (True, row[0]) if row else (False,)

    def get(self, car_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cars WHERE car_id = ?", (str(car_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT model, price, car_id FROM cars")
        rows = cursor.fetchall()
        return rows

    def delete(self, car_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM cars WHERE car_id = ?''', (str(car_id)))
        cursor.close()
        self.connection.commit()

    def get_by_price(self, start_price, end_price):
        cursor = self.connection.cursor()
        cursor.execute("SELECT model, price, car_id FROM cars WHERE price >= ? AND price <= ?", (str(start_price), str(end_price)))
        row = cursor.fetchall()
        return row

    def get_by_dealer(self, dealer_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT model, price, car_id FROM cars WHERE dealer = ?", (str(dealer_id)))
        row = cursor.fetchall()
        return row