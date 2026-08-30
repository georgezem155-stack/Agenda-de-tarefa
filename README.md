Cadastro de Usuários (CRUD com SQLite)

Projeto em Python que implementa um CRUD completo (Create, Read, Update, Delete) para gerenciamento de usuários, utilizando o banco de dados SQLite.

Funcionalidades
Inserir um novo usuário (nome e e-mail)
Listar todos os usuários cadastrados
Buscar um usuário específico por ID
Atualizar o e-mail de um usuário existente
Excluir um usuário pelo ID
Conceitos aplicados
Conexão e manipulação de banco de dados com o módulo sqlite3
Uso de queries parametrizadas (?) para prevenir SQL Injection
Tratamento de erros com try/except, incluindo o tratamento específico de sqlite3.IntegrityError (para e-mails duplicados)
Verificação de resultados com cursor.rowcount (para saber se uma atualização ou exclusão realmente afetou algum registro)
Estrutura do projeto
├── main.py               # Ponto de entrada do programa
├── inserir.py            # Cadastra um novo usuário
├── ler.py                # Lista todos os usuários
├── buscar_usuario.py     # Busca um usuário por ID
├── atualizar_usuario.py  # Atualiza o e-mail de um usuário
├── excluir.py            # Remove um usuário pelo ID
└── meu_banco.db          # Banco de dados SQLite gerado automaticamente
Como executar
bash
python main.py

A tabela usuarios é criada automaticamente (CREATE TABLE IF NOT EXISTS) na primeira execução, caso ainda não exista.

Estrutura da tabela usuarios
Campo	Tipo	Restrição
id	INTEGER	Chave primária, autoincremento
nome	TEXT	Obrigatório
email	TEXT	Obrigatório e único
Possíveis melhorias futuras
Unificar as operações em um único programa com menu interativo (loop no terminal)
Separar a lógica em funções reutilizáveis
Adicionar validação de formato de e-mail antes de inserir
Migrar para uma classe Usuario responsável por se salvar/buscar/atualizar (padrão Repository)
