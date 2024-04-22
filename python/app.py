from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('users.db')

# Cria uma tabela para armazenar os e-mails
conn.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT)''')

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()

def email_exists(email):
    # Conecta ao banco de dados
    conn = sqlite3.connect('users.db')

    # Faz uma consulta para verificar se o e-mail existe
    cursor = conn.execute("SELECT * FROM users WHERE email=?", (email,))

    # Se a consulta retornar algum resultado, então o e-mail existe
    result = cursor.fetchone() is not None

    # Fecha a conexão com o banco de dados
    conn.close()

    return result

email = request.form['email']
if email_exists(email):
    # O e-mail está cadastrado, então você pode continuar com o processo de login
    pass
else:
    # O e-mail não está cadastrado, então você pode exibir uma mensagem de erro
    flash('E-mail não cadastrado')