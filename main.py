import tkinter as tk
from tkinter import messagebox, simpledialog

def salvar_tarefas():
    with open('tarefas.txt', 'w') as file:
        for tarefa in lista_tarefas.get(0, tk.END):
            file.write(f"{tarefa}\n")

def carregar_tarefas():
    try:
        with open('tarefas.txt', 'r') as file:
            for tarefa in file:
                lista_tarefas.insert(tk.END, tarefa.strip())
    except FileNotFoundError:
        pass

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa!")

def remover_tarefa():
    try:
        tarefa_selecionada = lista_tarefas.curselection()[0]
        lista_tarefas.delete(tarefa_selecionada)
        salvar_tarefas()
    except:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover!")

def editar_tarefa():
    try:
        tarefa_selecionada_index = lista_tarefas.curselection()[0]
        tarefa_selecionada = lista_tarefas.get(tarefa_selecionada_index)

        tarefa_editada = simpledialog.askstring("Editar Tarefa", "Qual é a nova descrição da tarefa?", initialvalue=tarefa_selecionada)
        
        if tarefa_editada:
            lista_tarefas.delete(tarefa_selecionada_index)
            lista_tarefas.insert(tarefa_selecionada_index, tarefa_editada)
            salvar_tarefas()
    except:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para editar!")

app = tk.Tk()
app.title("Gerenciador de Tarefas Avançado")

# Campo de entrada
entrada_tarefa = tk.Entry(app, width=45)
entrada_tarefa.pack(pady=20)

# Lista de tarefas
lista_tarefas = tk.Listbox(app, width=50, height=15, bg="#f7f7f7", fg="#333", selectbackground="#a6a6a6", selectforeground="#ffffff")
lista_tarefas.pack(pady=20)

# Botões
botao_adicionar = tk.Button(app, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=10)

botao_remover = tk.Button(app, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(pady=10)

botao_editar = tk.Button(app, text="Editar Tarefa", command=editar_tarefa)
botao_editar.pack(pady=10)

# Carregar tarefas salvas
carregar_tarefas()

app.mainloop()
