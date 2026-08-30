import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

id_busca = input("Digite o ID do usuário que deseja buscar: ")
comando_sql1 = "SELECT * FROM usuarios WHERE id = ?"
cursor.execute(comando_sql1, (id_busca,))

usuario = cursor.fetchone()

if usuario:
    print(f"usuario encontrado: ID: {usuario[0]}, Nome: {usuario[1]}")

else:
    print("usuario não encontrado.")

conexao.close()