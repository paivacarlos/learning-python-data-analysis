import sqlite3
import random
import time
import datetime

#criando a conexão
connectDb = sqlite3.connect('db/dsa.db')

#cursor
c = connectDb.cursor()

#funcao para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, value REAL)')

#funcao para inserir uma linha
def data_insert():
    c.execute("INSERT INTO products VALUES(10, '2018-05-02 14:32:11', 'Teclado', 90)")
    connectDb.commit()
    c.close()
    connectDb.close()

#utilizando variaveis para inserir dados
def data_insert_by_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_value = random.randrange(50, 100)
    c.execute("INSERT INTO products (date, prod_name, value) VALUES (?, ?, ?)", (new_date, new_prod_name, new_value))
    connectDb.commit()

#leitura de dados
def read_all_data():
    c.execute("SELECT * FROM products")
    for line in c.fetchall():
        print(line)

#leitura especifica de dados
def read_registers():
    c.execute("SELECT * FROM products WHERE value > 60.0")
    print("MORE THAN 60.0!")
    for line in c.fetchall():
        print(line)

#leitura de colunas especificas
def read_columns():
    c.execute("SELECT * FROM products")
    for line in c.fetchall():
        print(line[3])

#SELECT nos dados
read_all_data()

#Leitura ESPECIFICA de registros
read_registers()

#Leitura ESPECIFICA de cada COLUNA
read_columns()

#update
def update_data():
    c.execute("UPDATE products SET value = 70.00 WHERE value = 98.0")
    connectDb.commit()

#delete
def remove_data():
    c.execute("DELETE FROM products WHERE value = 55.0")
    connectDb.commit()

update_data()
#read_all_data()

remove_data()
read_all_data()

#fechando a conexão com o banco de dados
#c.close()
#connectDb.close()