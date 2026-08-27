# Agenda de Tarefas - Programa em Python

Permite adicionar, listar, concluir, remover e salvar tarefas. As tarefas ficam gravadas em um arquivo JSON (`tarefas.json`) para não serem perdidas ao fechar o programa.

```python
import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON, se ele existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("⚠️ A descrição não pode ficar vazia.\n")
        return

    prazo = input("Prazo (dd/mm/aaaa) - opcional, aperte Enter para pular: ").strip()
    if prazo:
        try:
            datetime.strptime(prazo, "%d/%m/%Y")
        except ValueError:
            print("⚠️ Data inválida, tarefa criada sem prazo.\n")
            prazo = ""

    tarefa = {
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("📌 Nenhuma tarefa cadastrada.\n")
        return

    print("\n===== SUAS TAREFAS =====")
    for i, t in enumerate(tarefas, start=1):
        status = "✔️ Concluída" if t["concluida"] else "🔘 Pendente"
        prazo = f" | Prazo: {t['prazo']}" if t["prazo"] else ""
        print(f"{i}. [{status}] {t['descricao']}{prazo}")
    print("========================\n")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        numero = int(input("Número da tarefa para concluir: "))
        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("🎉 Tarefa concluída com sucesso!\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")
