import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

nome = input("Digite o nome do usuário: ")
email = input("Digite o email do usuário: ")

comando_sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
try:
    cursor.execute(comando_sql, (nome, email))
    conexao.commit()

    print(f'usuario {nome} inserido com sucesso!')
except sqlite3.IntegrityError:
    print("Erro: O email já está cadastrado !.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

conexao.close()

