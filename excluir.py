import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

id_para_delete = input("Digite o ID do usuário que deseja excluir: ")
comando_delete = "DELETE FROM usuarios WHERE id = ?"
cursor.execute(comando_delete, (id_para_delete,))

conexao.commit()
conexao.close()

if cursor.rowcount > 0:
    print(f"Usuário com ID {id_para_delete} deletado com sucesso!")
else:
    print("nenhum usuário encontrado com o ID fornecido.")