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

#gerando valores e inserindo na tabela
for i in range(10):
    data_insert_by_var()
    time.sleep(1)

#fechando a conexão com o banco de dados
c.close()
connectDb.close()