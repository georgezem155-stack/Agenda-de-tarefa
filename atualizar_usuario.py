import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

id_usuario = id_para_delete = input("Digite o ID do usuário que deseja atualizar: ")
novo_email = input("Digite o novo e-mail do usuário: ")

comando_update = "UPDATE usuarios SET email = ? WHERE id = ?"
cursor.execute(comando_update, (novo_email, id_usuario))

conexao.commit()
conexao.close()


if cursor.rowcount > 0:
    print(f"Usuário com ID {id_para_delete} atualizado com sucesso!")
else:
    print("nenhum usuário encontrado com o ID fornecido.")