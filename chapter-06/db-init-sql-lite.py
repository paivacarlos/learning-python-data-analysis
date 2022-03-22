#Remover o banco da maquina local
import os
os.remove("db/school.db") if os.path.exists("db/school.db") else None

#Importando o modulo de acesso ao SQLite
import sqlite3

#Se o banco de dados não exister ele será criado neste momento
MyFirstDbCon = sqlite3.connect("db/school.db")
print(type(MyFirstDbCon))

#Criando um cursor que terá acesso a todas as linhas do arquivo
cur = MyFirstDbCon.cursor()
print(type(cur))

#Executando a instrução SQL para criar uma tabela
sql_create = "create table courses "\
             "(id integer primary key, "\
             "title varchar(100), "\
             "category varchar(140))"

#Executando a instrução no cursor
cur.execute(sql_create)
#print(type(sql_create))

#Executando outra instrução SQL para INSERIR registros
sql_insert = "insert into courses values(?, ?, ?)"

#dados
recset = [(1000, "Ciência de Dados", "Data Scince"),
          (1001, "Big Data Fundamentos", "Big Data"),
          (1002, "Python Fundamentos", "Análise de Dados")]

#Inserindo registros
for rec in recset:
    cur.execute(sql_insert, rec)

#grava os dados
MyFirstDbCon.commit()

#Criando outro comando SQL para SELECIONAR registros
sql_select = "select * from courses"

#seleciona e recupera os registros
cur.execute(sql_select)
data = cur.fetchall()

#mostrando os dados
for line in data:
    print("Course ID: %d, Title: %s, Category: %s \n" % line)

#gerando outros registros
recset2 = [(1003, "Gestão de dados com o MongoDB", "Big Data"),
           (1004, "R Fundamentos", "Análise de Dados")]

#inserindo registros
for rec2 in recset2:
    cur.execute(sql_insert, rec2)

#Gravando os dados no banco
MyFirstDbCon.commit()

#selecionando todos os registros
cur.execute(sql_select)

#recupera todos os registros
data2 = cur.fetchall()

#mostrando os dados
for line in data2:
    print("Course ID: %d, Title: %s, Category: %s \n" % line)

#fecha conexão com o banco de dados
MyFirstDbCon.close()