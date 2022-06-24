from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

janela = Tk()
janela.title('tela de login')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('310x360')

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font='Ivy 25', bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=295, anchor=NW, font='Ivy 1', bg=co2, fg=co4)
l_linha.place(x=5, y=45)


credenciais = ['junior', '123456789']

def verificar_senhar():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta')


        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique login e senha')

def nova_janela():
    l_nome = Label(frame_cima, text='Usuário: ' + credenciais[0], anchor=NE, font='Ivy 20', bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=295, anchor=NW, font='Ivy 1', bg=co2, fg=co4)
    l_linha.place(x=5, y=45)


    l_nome = Label(frame_baixo, text='Seja bem vindo:\n' + credenciais[0], anchor=NE, font='Ivy 20', bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

l_nome = Label(frame_baixo, text='Nome * ', anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left',  highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)



l_pass = Label(frame_baixo, text='Password * ', anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', highlightthickness=1, relief="solid")
e_pass.place(x=14, y=130)


l_bnt = Button(frame_baixo, text='CONFIMAR', height=1, width=10, anchor=NW, font='Ivy 8 bold', bg=co2, fg=co1, command=verificar_senhar)
l_bnt.place(x=100, y=200)



janela.mainloop()
