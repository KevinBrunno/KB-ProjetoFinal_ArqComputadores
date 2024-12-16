import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def sair():
    window.quit()

def limpar_frame():
    for widget in frm1.winfo_children():
        widget.destroy()

def salvar_arquivo():
    arq = open("def.txt", "w")
    arq.write(n.get() + "\n")
    arq.write(n2.get() + "\n")
    arq.write(n3.get() + "\n")
    arq.write(n4.get() + "\n")
    arq.close()

    # Soma do conjunto de requisitos selecionados na interface
    total = (opcoes.current() + opcoes2.current() + opcoes3.current() + opcoes4.current())
    
    # Limpa o frame antes de mostrar a info da CPU selecionada
    limpar_frame()  
    verificar_arquivo(total)


# O arquivo "conf.csv" deve estar presente para o pleno funcionamento
#   da função "verificar_arquivo()"

def verificar_arquivo(total):
    with open("conf.csv", "r", encoding="utf-8") as arq2:
        dados = csv.reader(arq2)
        for linha in dados:
            # Se 0 <= valor <= 2 ; valor = 0 
            # Se 3 <= valor <= 6 ; valor = 4    
            # Se o valor for 7, ele é arredondado para cima; valor = 8
            if total < 8:
                if (total <=6) and (total >=3):
                    total = 4
                elif(total == 7):
                    total = 8
                else:
                    total = 0
            if int(linha[0]) == total:
                msgm1 = "Processador:\n\nModelo:\n\nFrequência:\n\nMemória Cache:\n\nMotivo:\n"
                msgm2 = f"{linha[1]}\n\n{linha[2]}\n\n{linha[3]}\n\n{linha[4]}\n\n{linha[5]}\n"
                ttk.Label(frm1, foreground='turquoise4', background='azure3', text=msgm1,
                          font=("Times New Roman", 15)).grid(column=0, row=5, padx=10, pady=10)
                ttk.Label(frm1, foreground='darkblue', background='azure3', text=msgm2,
                          font=("Times New Roman", 15)).grid(column=1, row=5, padx=15, pady=10)

def info():
    info1="Básico: Uso comum do dia a dia e trabalho convencional.\n\n"
    info2="Intermediário: Jogos(Requisitos mínimos ou recomendados) e\nProgramas mais exigentes.\n\n"
    info3="Avançado: Jogos mais recentes \ne/ou exigentes\n( >= Requisitos recomendados)\n"
    messagebox.showinfo(title="Info", message=info1 + info2 + info3 +"ou Programas pesados e tarefas específicos")

def sobre():
    msg1="UFG - INF 2024\nArquitetura de Computadores\nProfessora: Bruna Michelly\n\n"
    messagebox.showinfo(title="Sobre", message=msg1 + "Autor: Kevin Brunno")


window = Tk()
window.title("Projeto Final - Módulo de escolha da CPU")
window.geometry('800x500')
window.resizable(False, False) #Torna a janela "non-resizable"

frm1 = Frame(window, borderwidth=2, relief="solid", bg='azure3')
frm1.place(x=1,y=1, width=798, height=460)

# Componentes visuais da interface(Labels e 1 "botão" inativo)
btt_panel = Button(frm1,text="SELECIONE AS OPÇÕES DESEJADAS", borderwidth=2, foreground='turquoise3', state='disabled',
                   background='azure2', font='Arial 16 bold').grid(column = 0, row=0, pady=55, sticky="NW", ipady=5)


ttk.Label(frm1, background='azure3', text = "Desempenho:", 
          font = ("Times New Roman", 15)).grid(column = 0, 
          row = 5, padx = 10, pady = 15) 

ttk.Label(frm1, background='azure3', text = "Consumo de Energia:", 
          font = ("Times New Roman", 15)).grid(column = 0, 
          row = 6, padx = 10, pady = 15)

ttk.Label(frm1, background='azure3', text = "Custo:", 
          font = ("Times New Roman", 15)).grid(column = 0, 
          row = 7, padx = 10, pady = 15)

ttk.Label(frm1, background='azure3', text = "Uso específico:", 
          font = ("Times New Roman", 15)).grid(column = 0, 
          row = 8, padx = 10, pady = 15)

# Widget de ComboBox para cada um dos Requisitos da CPU
n = StringVar()
opcoes = ttk.Combobox(frm1, width=40, state='readonly', textvariable=n)
opcoes['values'] = ('Normal', 'Bom', 'Excelente')

n2 = StringVar()
opcoes2 = ttk.Combobox(frm1, width=40, state='readonly', textvariable=n2)
opcoes2['values'] = ('Baixo', 'Moderado', 'Alto')

n3 = StringVar()
opcoes3 = ttk.Combobox(frm1, width=40, state='readonly', textvariable=n3)
opcoes3['values'] = ('Baixo', 'Médio', 'Alto')

n4 = StringVar()
opcoes4 = ttk.Combobox(frm1, width=40, state='readonly', textvariable=n4)
opcoes4['values'] = ('Básico', 'Intermediário', 'Avançado')

opcoes.grid(column=1, row=5)  # Posicionamento Combobox
opcoes2.grid(column=1, row=6) # Posicionamento Combobox_2
opcoes3.grid(column=1, row=7) # Posicionamento Combobox_3
opcoes4.grid(column=1, row=8) # Posicionamento Combobox_4

# Botao de salvar
btt_op = Button(frm1,text="Salvar", command=salvar_arquivo, borderwidth=2, background='turquoise3')
btt_op.grid(column=1, pady=13) # Posicionamento do widget(dentro do frame)

# Botao de SAIR
btt2_op = Button(window,text="Sair", command=sair, background='lightcoral', activebackground='tomato')     
btt2_op.pack(side='bottom', anchor=W, padx=4, pady=4) # Posicionamento do widget

# Botao SOBRE
btt3_op = Button(window, text="Sobre", command=sobre)
btt3_op.pack(side='top', anchor=E, padx=4, pady=4)

# Botao INFO
btt4_op = Button(frm1, text="i", command=info, font='Arial 12 bold', foreground='grey')
btt4_op.grid(column=3, row=8, padx=10, pady=15)

opcoes.current(1)
opcoes2.current(1)
opcoes3.current(1)
opcoes4.current(1)

window.mainloop()
