import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:') # Cria o banco de dados em memória
        print(f'Banco de dados criado com sucesso!')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE usuarios (
                            id INTEGER PRIMARY KEY,
                            email TEXT NOT NULL UNIQUE,
                            senha TEXT NOT NULL);''')
        print("Tabela usuarios criada com sucesso")
    except sqlite3.Error as e:
        print(e)

def insert_user(conn, email, senha):
    sql = '''INSERT INTO usuarios(email,senha) VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (email, senha))
    conn.commit()
    return cur.lastrowid

def main():
    database = "estacionamento.db"

    conn = create_connection()
    if conn is not None:
        create_table(conn)
        # Inserindo alguns usuários para teste
        insert_user(conn, 'alexcs@outlook.com.br', '123')
        insert_user(conn, 'admin@example.com', 'admin123')
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()




    #area do banco de dados cadastro


    import sqlite3
import os

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('estacionamento.db')
        print(f'Banco de dados criado com sucesso!')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE usuarios (
                            id INTEGER PRIMARY KEY,
                            nome TEXT NOT NULL,
                            nascimento DATE NOT NULL,
                            rg TEXT NOT NULL UNIQUE,
                            endereco TEXT NOT NULL,
                            cidade TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            foto_pessoa BLOB NOT NULL,
                            foto_documento BLOB NOT NULL);''')
        print("Tabela usuarios criada com sucesso")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "estacionamento.db"

    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()