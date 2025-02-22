#faz as importações necessárias
from tkinter import *
from tkinter import ttk

#cria a janela principal
Janela = Tk()
Janela.title("Calculadora")

#Cria as variáveis
numero = StringVar(value='')
global operação
global memoria
global decimal
operação = ''
memoria = 0.0

#Define fonte
fonte = ('Helvatica', 18)

#Define as funções
def bt_click_1():
    print('Botão 1 clicado')
    numero.set(numero.get() + '1')
def bt_click_2():
    print('Botão 2 clicado')
    numero.set(numero.get() + '2')
def bt_click_3():
    print('Botão 3 clicado')
    numero.set(numero.get() + '3')
def bt_click_4():
    print('Botão 4 clicado')
    numero.set(numero.get() + '4')
def bt_click_5():
    print('Botão 5 clicado')
    numero.set(numero.get() + '5')
def bt_click_6():
    print('Botão 6 clicado')
    numero.set(numero.get() + '6')
def bt_click_7():
    print('Botão 7 clicado')
    numero.set(numero.get() + '7')
def bt_click_8():
    print('Botão 8 clicado')
    numero.set(numero.get() + '8')
def bt_click_9():
    print('Botão 9 clicado')
    numero.set(numero.get() + '9')
def bt_click_0():
    print('Botão 0 clicado')
    numero.set(numero.get() + '0')

#Operações
def bt_click_soma(): #OK
    global operação #Adiona a variável operação ao escopo global
    global memoria
    print('Botão + clicado') #printa no console que o botão + foi clicado
    if operação != '': #Verifica se não há uma operação ocorrendo
        bt_click_igual()
    memoria =+ float(numero.get()) #Adiciona o valor do número ao valor da memória
    print(memoria) #Printa o valor da memória
    numero.set('') #Limpa o visor
    operação = 'soma' #Define a operação como soma
    print(f'o valor na memória (Na soma) é: {memoria}') #Verificar o valor da memória
    print(f'O valor do número (Na soma) é {numero.get()}') #Verificar o valor do número
def bt_click_sub(): #OK
    print('Botão - clicado') #printa no console que o botão - foi clicado
    global operação #adiciona a variável operação ao escopo global
    global memoria
    if operação != '': #Verifica se não há operação ocorrendo
        bt_click_igual()
    memoria =+ float(numero.get()) #Adiona o valor do número ao valor da memória
    numero.set('') #Limpa o visor
    operação = 'sub' #Define a operação como subtração
    print(f'o valor na memória (Na soma) é: {memoria}') #Verificar o valor da memória
    print(f'O valor do número (Na soma) é {numero.get()}') #Verificar o valor do número
def bt_click_mult(): #OK
    print('Botão * clicado')
    global operação #Adiona a variável operação ao escopo global
    global memoria
    if operação != '': #Verifica se não há operações pendentes
        bt_click_igual()
    memoria =+ float(numero.get()) #Adiiona a memoria o número
    numero.set('') #Limpa o vizor
    operação = 'mult' #Define a operação como multiplicação
def bt_click_div():
    print('Botão / clicado')
    global operação #Adiona a variável operação ao escopo global
    global memoria
    if operação != '': #Verifica se não há operações pendentes
        bt_click_igual()
    memoria =+ float(numero.get()) #Adiiona a memoria o número
    numero.set('') #Limpa o vizor
    operação = 'div' #Define a operação como multiplicação
def bt_click_igual(*args): #OK (Falta adicionar as outras operações)
    print('Botão = clicado')
    global operação
    global memoria
    print(operação)
    print(f'o valor na memória é: {memoria}') #Verificar o valor da memória
    print(f'O valor do número é {numero.get()}') #Verificar o valor do número
    match operação: #Identifica o tipo de operação
        case 'soma':
            numero.set(memoria + float(numero.get())) #Adiona o valor da memória
        case 'sub':
            numero.set(memoria - float(numero.get())) #Subtrai o valor da memória
        case 'mult':
            numero.set(memoria * float(numero.get())) #Multiplica o valor da memória
        case 'div':
            numero.set(memoria / float(numero.get())) #Divide o valor da memória
    print(numero.get())
    numerotemp = numero.get()
    operação = ''
    if str(numerotemp[-2:]) == '.0': #Identifica se é um número inteiro ou não
        numero.set(numerotemp[:-2]) #Caso for um número inteiro ele remove o .0
def bt_click_ponto(): #OK
    if '.' in numero.get(): #Verifica se já existe um ponto no número
        return
    print('Botão . clicado')
    numero.set(numero.get() + '.') #Adiciona um ponto ao número
def bt_click_limpar(): #OK
    print('Botão C clicado')
    global operação
    global memoria
    operação = ''
    memoria = 0.0
    numero.set('')
def bt_click_signal(): #OK
    print('Botão +/- clicado')
    if numero.get() == '': #Verifica se o número está vazio
        return
    if numero.get()[0] == '-': #Verifica se o número contem um sinal negativo
        numero.set(numero.get()[1:]) #Retira o primeiro sinal do número
    else:
        numero.set('-' + numero.get()) #Adiciona um sinal negativo ao número
#cria os frames
Botões = Frame(Janela, borderwidth=1, relief='raised')
Botões.grid(row=1)
visor = Frame(Janela)
visor.grid(row=0,sticky='e')

#cria os botões
bt1 = ttk.Button(Botões, text='1', command=bt_click_1).grid(row=2, column=0)
bt2 = ttk.Button(Botões, text='2', command=bt_click_2).grid(row=2, column=1)
bt3 = ttk.Button(Botões, text='3', command=bt_click_3).grid(row=2, column=2)
bt4 = ttk.Button(Botões, text='4', command=bt_click_4).grid(row=3, column=0)
bt5 = ttk.Button(Botões, text='5', command=bt_click_5).grid(row=3, column=1)
bt6 = ttk.Button(Botões, text='6', command=bt_click_6).grid(row=3, column=2)
bt7 = ttk.Button(Botões, text='7', command=bt_click_7).grid(row=4, column=0)
bt8 = ttk.Button(Botões, text='8', command=bt_click_8).grid(row=4, column=1)
bt9 = ttk.Button(Botões, text='9', command=bt_click_9).grid(row=4, column=2)
bt0 = ttk.Button(Botões, text='0', command=bt_click_0).grid(row=5, column=1)
bt_soma = ttk.Button(Botões, text='+', command=bt_click_soma).grid(row=4, column=3)
bt_sub = ttk.Button(Botões, text='-', command=bt_click_sub).grid(row=3, column=3)
bt_mult = ttk.Button(Botões, text='*', command=bt_click_mult).grid(row=2, column=3)
bt_div = ttk.Button(Botões, text='/', command=bt_click_div).grid(row=1, column=3)
bt_igual = ttk.Button(Botões, text='=', command=bt_click_igual).grid(row=5, column=3)
bt_ponto = ttk.Button(Botões, text='.', command=bt_click_ponto).grid(row=5, column=0)
bt_limpar = ttk.Button(Botões, text='C', command=bt_click_limpar).grid(row=1, column=2)
bt_flip = ttk.Button(Botões, text='+/-',command=bt_click_signal).grid(row=1, column=1)

#Cria o visor
visor = ttk.Label(visor, textvariable=numero,anchor='e',justify='right',font=fonte).grid(row=0, column=0,columnspan=5)

#Roda a janela principal
Janela.mainloop()