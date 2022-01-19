import sqlite3
from sqlite3 import Error
from os import system

def ConexaoBanco():
    caminho = "C:/Users/macie/OneDrive/Área de Trabalho/Projetos/Projetos com uso de API e Interface Grafica/Registration Form/registrationDB.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
conexao = ConexaoBanco()

# FUNÇÕES DE COMANDO DO BANCO DE DADOS

def inserir(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro inserido')

nome = int(input('Digite o nome: '))
telefone = str(input('Digite o telefone: '))
email = str(input('Digite o email: '))

vsql = f"""INSERT INTO registrationDB
            ("""






def NewAccount():
    print('NewAccount')

def LoginAccount():
    print('LoginAccount')

NewAccount()