#Remover o banco da maquina local
import os
os.remove("db/dsa.db") if os.path.exists("db/dsa.db") else None

import sqlite3

#criando a conexão com o banco
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

#criando uma tabela
create_table()

#inserindo dados
data_insert()