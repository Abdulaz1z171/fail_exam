# 1.	Postgresql bazaga python yordamida ulaning . 
# Product nomli jadval yarating  (id,name,price, color,image) 


import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'temur_1336',
    database = 'n42',
    port = 5432
)

cur = conn.cursor()

def create_table():
    create_product_table  = '''
    CREATE TABLE IF NOT EXISTS products(
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(6,2) NOT NULL,
        color VARCHAR(100) NOT NULL,
        image VARCHAR(255) NOT NULL
    );
    
    '''
    cur.execute(create_product_table)
    conn.commit()


def insert_into():
    insert_to_products = '''INSERT INTO products(name,price,color,image)
    VALUES                 (%s,%s,%s,%s);'''
    name = input('Enter name! ')
    price = float(input('Enter price!'))
    color = input('Enter color ! ')
    image = input('Enter image! ')
    insert_params = (name,price,color,image)
    cur.execute(insert_to_products,insert_params)
    conn.commit()

def update_table():
    update_prodcuts_information = '''UPDATE products 
                                     SET name = %s,
                                         price = %s,
                                         color = %s,
                                         image = %s
                                     WHERE product_id = %s'''

    product_id = int(input('Product id! '))
    name = input('Enter name! ')
    price = float(input('Enter price!'))
    color = input('Enter color ! ')
    image = input('Enter image! ')
    update_params = (name,price,color,image,product_id)
    cur.execute(update_prodcuts_information,update_params)
    conn.commit()

def delete_from_table():
    delete_information_by_id = '''DELETE FROM products
                                  WHERE product_id = %s'''
    product_id = int(input('Enter id! '))

    cur.execute(delete_information_by_id,product_id)
    conn.commit()

def select_all():
    select_all_information_from_product = '''
    SELECT * FROM products;
    '''
    cur.execute(select_all_information_from_product)
    conn.commit()



#  3.	Alphabet nomli class yozing .class obyektlarini  iteratsiya qilish imkoni  
#  bo’lsin (iterator).  obyektni for sikli orqali iteratsiya 
# qilinsa 26 ta alifbo xarflari chiqsin
from typing import List


class Alphabet:
    def __init__(self,letters:List[str,]):
        self._letters = letters
        self._count = 0

    
    def __iter__(self):
        return self

    def __next__(self):
        if self._count < len(self._letters):
            result = self._letters[self._count]
            self._count += 1
            return result
        else:
            raise StopIteration


# alifbo = ['A','B','D','E','F','G','H','J','K','L','M','N','O',
# 'P','Q','R','S','T','U','V','X','Y','Z','SH','CH','NG']

# a1 = Alphabet(alifbo)
# for i in a1:
#     print(i)



# 4.	print_numbers va print_leters nomli funksiyalar yarating. 
# prit_numbers funksiyasi (1,5) gacha bo’lgan sonlarni ,
#  print_letters esa  ‘’ABCDE” belgilarni loop da bitta dan time sleep(1) qo’yib
#  ,parallel 2ta thread yarating.Ekranga parallel ravishda itemlar chiqsin
import time
import threading

def print_numbers():
    for i in range(5):
        print(f'numbers: {i}')
        time.sleep(1)

def print_letters():
    letters = 'ABSEDF'
    for i in range(0,len(letters)):
        print(f'Letters: {letters[i]}')
        time.sleep(1)

# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)


# thread1.start()
# thread2.start()

# thread1.join()
# thread1.join()



#  5.	Product nomli class yarating (1 – misoldagi Product ).
# Product classiga save() nomli object method yarating.
# Uni vazifasi object attributelari orqali bazaga saqlasin
# 

class Product:
    def __init__(self,name,price,color,image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        insert_information_to_table_by_save_function = '''
        INSERT INTO products(name,price,color,image)
        VALUES      (%s,%s,%s,%s);'''

        insert_params = (self.name,self.price,self.color,self.image)
        cur.execute(insert_information_to_table_by_save_function,insert_params)
        conn.commit()

# p1 = Product('urik',1233.45,'sariq','zur')
# p1.save()


#  
# 6.	DbConnect nomli ContextManager yarating. 
# Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)
# 

db_parameters = {
    'host' : 'localhost',
    'database' : 'n42',
    'user' : 'postgres',
    'password' : 'temur_1336',
    'port' : 5432
}

# DbConnect contex manager yaratamiz
class DbConnect:
    def __init__(self,db_parameters):
     
        self.db_parameters = db_parameters
        self.conn = psycopg2.connect(**db_parameters)
    
    def __enter__(self):
        
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self,exc_tb,exc_type,exc_val):
        if self.conn and not self.conn.closed:
            self.conn.commit()
            self.conn.close()

with DbConnect(db_parameters) as cur:
    select_query = '''
    SELECT * FROM products;
    '''
    cur.execute(select_query)

    for i in cur.fetchall():
        print(i)

    