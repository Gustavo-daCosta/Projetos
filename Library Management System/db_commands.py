import sqlite3
from sqlite3 import Error


def DB_connection():
    caminho = "data/LibraryDB.db"
    con = sqlite3.connect(caminho)
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon = DB_connection()

def insert(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Register insert')
'''
nome = str(input('Digite o nome: '))
telefone = str(input('Digite o telefone: '))
email = str(input('Digite o email: '))

vsql = f"""INSERT INTO tb_contatos 
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES('{nome}', '{telefone}', '{email}')"""

inserir(vcon, vsql)
'''

def delete(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Register removed')

vsql = """DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"""

#deletar(vcon, vsql)

def update(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Register updated')

vsql = "UPDATE tb_contatos SET T_NOMECONTATO = 'Marcos', T_TELEFONECONTATO='(31)95976-4255', T_EMAILCONTATO='bruno@email.com.br' WHERE N_IDCONTATO = 2"
#atualizar(vcon, vsql)

def consult(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql = "SELECT * FROM tb_contatos"
vsql = "SELECT * FROM tb_contatos WHERE N_IDCONTATO = 3"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO = 'Marcos'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE 'Marcos'" 
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%' AND T_TELEFONECONTATO LIKE 'B%'"
vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%o%' OR T_TELEFONECONTATO LIKE '%no'"
# resposta = consult(vcon, vsql)