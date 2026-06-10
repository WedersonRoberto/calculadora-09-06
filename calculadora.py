import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def adicionar(valor: str):
    # '''Função para inserir o valor clicado no display da calculadora.'''
    display.insert(tk.END, valor)


def limpar():
    display.delete(0, tk.END)  # '''Limpa o display da calculadora.'''


def calcular():
    try:

        expressao = display.get()  # '''Pega o texto do display da calculadora.'''
        # Substitui os símbolos de multiplicação e divisão pelos equivalentes em Python.
        expressao = expressao.replace('×', '*').replace('÷', '/')
        resultado = eval(expressao)  # '''Avalia a expressão matemática usando a função eval.'''
        display.delete(0, tk.END)  # '''Limpa o display da calculadora.'''
        display.insert(tk.END, str(resultado))  # '''Insere o resultado no display da calculadora.'''
    except ZeroDivisionError:
        messagebox.showerror(title="Erro", message="Divisão por zero não é permitida.")
        limpar()


janela = tk.Tk()
janela.title("Calculadora WFR")
janela.geometry("360x500")
janela.resizable(width=False, height=False)
janela.configure(bg="#810d0d")  # Cor de fundo da janela
style = ttk.Style()
style.theme_use("clam")  # Usa o tema "clam" para personalizar os botões
style.configure(
    "Botaoredondo.TButton",
    background="#3498db",  # Cor de fundo do botão
    foreground="white",
    borderwidth=1,
    focusthickness=3,
    focuscolor="none")
style.map("Botaoredondo.TButton",
          background=[("active", "#2980b9")],  # Cor de fundo quando o botão é pressionado
          foreground=[("active", "white")])  # Cor do texto quando o botão é pressionado

# Display (Unico campo de texto onde os números e resultados são exibidos)
display = tk.Entry(janela, font=("Arial", 20), justify="right", bd=10, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)
# Botões da calculadora
botoes = [
    'C', '±', '%', '÷',
    '7', '8', '9', '×',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', '⌫'
]
# cores dos botões
cor_numeros = '#e0e0e0'  # Cinza claro para números
cor_operadores = '#2196f3'  # Azul para operadores
cor_funcionais = '#f44336'  # Vermelho para funções como limpar e backspace
cor_especial = '#9e9e9e'  # Cinza para botões especiais como ± e %
cores = {
    'C': '#f44336',  # Vermelho para limpar
    '±': '#9e9e9e',  # Cinza para alternar sinal
    '%': '#9e9e9e',  # Cinza para porcentagem
    '÷': '#2196f3',  # Azul para divisão
    '×': '#2196f3',  # Azul para multiplicação
    '-': '#2196f3',  # Azul para subtração
    '+': '#2196f3',  # Azul para adição
    '=': '#4caf50',  # Verde para igual
    '⌫': '#f44336'  # Vermelho para backspace
}
# Criação dos botões e atribuição de suas funções
row = 1  # Começa na linha 1(pois a linha 0 é ocupada pelo display)
col = 0  # Começa na coluna 0
for botao in botoes:
    if botao == "=":
        btn = ttk.Button(janela, text="Botao Clam", style="Botaoredondo.TButton")
        btn.config(command=calcular)
        btn.grid(row=row, column=col, columnspan=1, padx=3, pady=3, sticky="nsew")
        col += 1
    elif botao == "0":
        btn = ttk.Button(janela, text="Botao Clam", style="Botaoredondo.TButton")
        btn.config(command=lambda v=botao: adicionar(v))
        btn.grid(row=row, column=col, columnspan=1, padx=3, pady=3, sticky="nsew")
        col += 1
    elif botao in ['+', '-', '×', '÷']:
        btn = ttk.Button(janela, text="Botao Clam", style="Botaoredondo.TButton")
        btn.config(command=lambda v=botao: adicionar(v))
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        col += 1
    elif botao in ['C', '±', '%', '⌫']:
        btn = ttk.Button(janela, text="Botao Clam", font=("Arial", 14, "bold"), style="Botaoredondo.TButton")
        if botao == 'C':
            btn.config(command=limpar)
        elif botao == '⌫':
            btn.config(command=lambda: display.delete(len(display.get()) - 1, tk.END))
        else:
            btn.config(command=lambda v=botao: adicionar(v))
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        col += 1
    elif botao in ['7', '8', '9', '4', '5', '6', '1', '2', '3']:
        btn = ttk.Button(janela, text="Botao Clam", font=("Arial", 14,), style="Botaoredondo.TButton")
        btn.config(command=lambda v=botao: adicionar(v))
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        col += 1
    else:
        btn = ttk.Button(janela, text="Botao Clam", font=("Arial", 14, "bold"), style="Botaoredondo.TButton")
        btn.config(command=lambda v=botao: adicionar(v))
        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        col += 1
    if col > 3:
        col = 0
        row += 1
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()