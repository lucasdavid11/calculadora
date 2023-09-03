#AUTOR: LUCAS DAVID ROSCIZNIAK COSTA
#
#DESCRIÇÃO: CALCULADORA FEITA EM PYTHON UTILIZANDO A BIBLIOTECA TKINTER PARA CRIAÇÃO DA INTERFACE GRÁFICA

from tkinter import *

fdivisao=False#FLAG PARA VERIFICAR SE SERA UMA DIVISAO
fmultiplicacao=False#FLAG PARA VERIFICAR SE SERA UMA MULTIPLICACAO
fadicao=False#FLAG PARA VERIFICAR SE SERA UMA ADICAO
fsubtracao=False#FLAG PARA VERIFICAR SE SERA UMA SUBTRACAO
numero1=''
numero2=''
numeromaismenos=''
numerovirgula=''
fclick = False#FLASG PARA VERIFICAR SE HOUVE ALGUM CLICK EM ALGUM NÚMERO DEPOIS DE CHAMAR A FUNÇÃO igual(), CASO HAJA CLICK, CHAMA A FUNCAO limpa()

janela = Tk()

janela.geometry("355x360+700+300")
janela.resizable(False,False)
janela.title("Calculadora")
janela.iconbitmap("icon.ico")
janela.configure(background="#2e4053")

textuser = Entry(janela, width = 15,relief=FLAT, fg='#FFFFFF', bg='#76b58d', font=('futura', 30, 'bold'), justify=CENTER)
textuser.place(x=10,y=5)

def click(num):#INSERE NUMERO CLICKADO NA CAIXA DE TEXTO
    global fclick
    if fclick:
        limpa()
        fclick=False
    else:
        textuser.insert(END, num)

def divisao():
    global fdivisao
    global numero1
    global fclick

    fclick=False
    fdivisao = True
    numero1 = textuser.get()
    textuser.delete(0, END)

def multiplicacao():

    global fmultiplicacao
    global numero1
    global fclick

    fclick = False
    fmultiplicacao = True
    numero1 = textuser.get()
    textuser.delete(0, END)

def adicao():

    global fadicao
    global numero1
    global fclick

    fclick = False
    fadicao = True
    numero1 = textuser.get()
    textuser.delete(0, END)

def subtracao():
    global fsubtracao
    global numero1
    global fclick

    fclick = False
    fsubtracao = True
    numero1 = textuser.get()
    textuser.delete(0, END)

def porcentagem():

    global numero1
    global fclick

    fclick = False
    numero1 = textuser.get()
    textuser.delete(0, END)
    numero1 = float(numero1)
    resultado = numero1 / 100
    resultado = str(resultado)
    textuser.delete(0, END)
    textuser.insert(0, resultado)

def igual():#REALIZA AS CONTAS

    global fdivisao
    global fmultiplicacao
    global fadicao
    global fsubtracao
    global fporcentagem
    global numero1
    global numero2
    global fclick


    numero1 = float(numero1)
    numero2 = textuser.get()
    numero2 = float(numero2)


    if fdivisao:
        if numero2==0:
            textuser.delete(0, END)
            textuser.insert(0, 'ERROR')
        resultado = numero1/numero2
        resultado = str(resultado)
        textuser.delete(0, END)
        textuser.insert(0, resultado)
    elif fmultiplicacao:
        resultado = numero1*numero2
        resultado = str(resultado)
        textuser.delete(0, END)
        textuser.insert(0, resultado)
    elif fadicao:
        resultado = numero1+numero2
        resultado = str(resultado)
        textuser.delete(0, END)
        textuser.insert(0, resultado)
    elif fsubtracao:
        resultado = numero1-numero2
        resultado = str(resultado)
        textuser.delete(0, END)
        textuser.insert(0, resultado)

    fclick=True
    fdivisao=False
    fmultiplicacao = False
    fadicao = False
    fsubtracao = False

def maismenos():#INVERTE SINAL DO NÚMERO
    global numeromaismenos

    numeromaismenos= textuser.get()

    numeromaismenos = float(numeromaismenos)
    if numeromaismenos != 0:
        numeromaismenos *= -1

    textuser.delete(0, END)
    textuser.insert(0, numeromaismenos)

def limpa():#DESCARTA TODAS AS INFORMAÕES PARA REINICIAR OS CÁLCULOS
    global numero1
    global numero2
    global numeromaismenos

    numeromaismenos=''
    numero1=''
    numero2=''
    textuser.delete(0, END)

def virgula():

    textuser.insert(END, '.')

#CONFIGURAÇÃO E ESTILIZAÇÃO DE CADA BOTÃO
buttonlimpa = Button(janela, text="C", command=limpa, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#727a85', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
buttonlimpa.place(x=10, y=60)
button7 = Button(janela, text="7", command=lambda: click(7), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button7.place(x=10, y=120)
button4 = Button(janela, text="4", command=lambda: click(4), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button4.place(x=10, y=180)
button1 = Button(janela, text="1", command=lambda: click(1), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button1.place(x=10, y=240)
button0 = Button(janela, text="0", command=lambda: click(0), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=15)
button0.place(x=14, y=300)

buttonmaismenos = Button(janela, text="+/-", command=maismenos, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#727a85', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
buttonmaismenos.place(x=97, y=60)
button8 = Button(janela, text="8", command=lambda: click(8), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button8.place(x=97, y=120)
button5 = Button(janela, text="5", command=lambda: click(5), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button5.place(x=97, y=180)
button2 = Button(janela, text="2", command=lambda: click(2), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button2.place(x=97, y=240)

buttonporcentagem = Button(janela, text="%", command=porcentagem, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#727a85', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
buttonporcentagem.place(x=185, y=60)
button9 = Button(janela, text="9", command=lambda: click(9), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button9.place(x=185, y=120)
button6 = Button(janela, text="6", command=lambda: click(6), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button6.place(x=185, y=180)
button3 = Button(janela, text="3", command=lambda: click(3), fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
button3.place(x=185, y=240)
buttonvirgula = Button(janela, text=",", command=virgula, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#405a70', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=7)
buttonvirgula.place(x=185, y=300)

buttondivisao = Button(janela, text="÷", command=divisao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#ac9c5c', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=6)
buttondivisao.place(x=273, y=60)
buttonmultiplicacao = Button(janela, text="x", command=multiplicacao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#ac9c5c', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=6)
buttonmultiplicacao.place(x=273, y=120)
buttonsubtracao = Button(janela, text="-", command=subtracao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#ac9c5c', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=6)
buttonsubtracao.place(x=273, y=180)
buttonadicao = Button(janela, text="+", command=adicao, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#ac9c5c', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=6)
buttonadicao.place(x=273, y=240)
buttonigual = Button(janela, text="=", command=igual, fg='#FFFFFF', activeforeground='#FFFFFF', bg='#ac9c5c', activebackground='#2a3e50', relief=FLAT, font=('futura', 12, 'bold'), height=2, width=6)
buttonigual.place(x=273, y=300)

janela.mainloop()
