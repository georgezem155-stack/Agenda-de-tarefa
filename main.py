import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

comando_sql = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""
cursor.execute(comando_sql)


conexao.commit()


conexao.close()

print("Banco de dados e tabela criados com sucesso!")
