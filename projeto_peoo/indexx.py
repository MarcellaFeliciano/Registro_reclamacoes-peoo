from tkinter import *
import sqlite3
import arrow
import pickle

class Sistema:
    def __init__ (self):
        self.situacao = 'adicionar'

        self.janela = Tk()
        self.tela()
        self.frames()
        self.menu()
        self.criar_tabela()
        mainloop()
 


    def tela(self):
        self.janela.title("Sistema de reclamações")
        self.janela.geometry('1100x680')
        self.janela.configure(background='lightgrey')
        self.janela.resizable(width = False, height = False)



    def frames(self):
        self.frame_header = Frame(self.janela, height=100, width=1100, bd =4, bg='#00BFFF')
        self.frame_header.pack()

        self.frame_nav = Frame(self.janela, height=80, width=1100, bg='#F7FFF7')
        self.frame_nav.pack()

        self.frame_content= Frame(self.janela, height=500, width=1100, bd = 4, bg='#00BFFF')
        self.frame_content.pack()

        


    def menu(self):
        self.titulo = Label(self.frame_header, text='REGISTRO DE RECLAMAÇÕES', font='Arial 25 bold', bg = '#00BFFF')
        self.titulo.place(x=300, y=25)

        self.bt_adicionar = Button(self.frame_nav, command=self.adicionar, text='Adicionar',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_adicionar.place(x=110, y=12)

        self.bt_excluir = Button(self.frame_nav, command=self.excluir, text='Excluir',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_excluir.place(x=350, y=12)

        self.bt_consultar = Button(self.frame_nav, command=self.consultar, text='Consultar',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_consultar.place(x=590, y=12)

        self.bt_fazer_backup = Button(self.frame_nav, command=self.backup, text='Backup',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_fazer_backup.place(x=830, y=12)

        self.imagem_menu = PhotoImage(file='profsm.png').subsample(3)
        self.imagem_menu_label = Label(self.frame_content, image=self.imagem_menu, bg='#00BFFF', width=650, height=550)
        self.imagem_menu_label.place(x=220, y=0)


    def criar_tabela(self):
        
        self.conexao = sqlite3.connect('registro_reclamacoes.db') 
        self.sql = self.conexao.cursor()
        self.sql.execute('CREATE TABLE registro_reclamacoes (nome, email, telefone, titulo, reclamacao)')
        self.conexao.commit()
        self.conexao.close()


    def adicionar(self):

        
        self.frame_adicionar= Frame(self.frame_content, height=500, width=1100, bd = 4, bg='#00BFFF')
        self.frame_adicionar.place(x=-4, y=0)

        self.bt_adicionar = Button(self.frame_nav, command=self.adicionar, text='Adicionar',font='Arial 10 bold', height=2, width=20, bg="#fb3139")
        self.bt_adicionar.place(x=110, y=12)

        self.bt_excluir = Button(self.frame_nav, command=self.excluir, text='Excluir',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_excluir.place(x=350, y=12)

        self.bt_consultar = Button(self.frame_nav, command=self.consultar, text='Consultar',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_consultar.place(x=590, y=12)

        self.bt_fazer_backup = Button(self.frame_nav, command=self.backup, text='Backup',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_fazer_backup.place(x=830, y=12)

        self.text_dados = Label(self.frame_adicionar, text='Dados do registro: ', font='Arial 20', bg='#00BFFF')
        self.text_dados.place(x=70,y=15)

        self.nome_text = Label(self.frame_adicionar, text='Nome: ',font='Helvetica 16', bg='#00BFFF')
        self.nome_text.place(x=70,y=60)

        self.nome_add = Entry(self.frame_adicionar, width=30,font='Helvetica 14', bg='#F7FFF7')
        self.nome_add.place(x=150,y=60)

        self.email_text = Label(self.frame_adicionar, text='Email: ',font='Helvetica 16', bg='#00BFFF')
        self.email_text.place(x=70,y=90)

        self.email_add = Entry(self.frame_adicionar, width=30,font='Helvetica 14',bg='#F7FFF7')
        self.email_add.place(x=150,y=90)

        self.telef_text = Label(self.frame_adicionar, text='Telefone: ',font='Helvetica 16', bg='#00BFFF')
        self.telef_text.place(x=70,y=120)

        self.telef_add = Entry(self.frame_adicionar, width=27,font='Helvetica 14', bg='#F7FFF7')
        self.telef_add.place(x=180,y=120)

        self.text_reclamacao = Label(self.frame_adicionar, text='Informações da reclamação: ', font='Helvetica 20', bg='#00BFFF')
        self.text_reclamacao.place(x=70,y=170)

        self.title_text = Label(self.frame_adicionar, text='Titulo: ',font='Helvetica 16', bg='#00BFFF')
        self.title_text.place(x=70,y=210)

        self.title_reclamacao = Entry(self.frame_adicionar, width=30,font='Helvetica 14', bg='#F7FFF7')
        self.title_reclamacao.place(x=150,y=210)

        self.reclamacao_text = Label(self.frame_adicionar, text='Reclamação: ',font='Helvetica 16', bg='#00BFFF')
        self.reclamacao_text.place(x=70,y=250)

        self.add_reclamacao = Entry(self.frame_adicionar, font='Helvetica 14', bg='#F7FFF7')
        self.add_reclamacao.place(x=70,y=280, height = 100, width = 382)

        self.imagemAdicionar = PhotoImage(file='reclamacoes .png').subsample(3)

        self.imagem_add = Label(self.frame_adicionar,image=self.imagemAdicionar, width=400, height=350, bg='#00BFFF')
        self.imagem_add.place(x=580, y=10)

        self.bt_add = Button(self.frame_adicionar, text='Adicionar reclamação', width=40, height=2, bg='#FF6666', command=self.adicionado)
        self.bt_add.place(x=600, y=320)

        self.display_timer()

    def display_timer(self):
        end_time = arrow.now().shift(minutes=10)
        self.timer_label = Label(self.frame_adicionar, font='Helvetica 12', bg='#00BFFF')
        self.timer_label.place(x=30, y=420)
        self.update_timer(end_time)

    def update_timer(self, end_time):
        remaining_time = end_time - arrow.now()
        if remaining_time.total_seconds() <= 0:
            self.janela.destroy() 
        else:
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f'Expira em: {hours:02d}:{minutes:02d}:{seconds:02d}'
            self.timer_label.config(text=time_str)
            self.janela.after(1000, lambda: self.update_timer(end_time))

 
    def adicionado(self):
        
        self.text_adicionado = Label(self.frame_adicionar, text='Reclamação adicionada com sucesso!', font='Arial 18', bg='#00BFFF')
        self.text_adicionado.place(x=200, y=420, width=800)

        self.nome = self.nome_add.get()
        self.email = self.email_add.get()
        self.telefone = self.telef_add.get()
        self.titulo = self.title_reclamacao.get()
        self.msg_reclamacao = self.add_reclamacao.get()


         # TRATAMENTO DE ERROS
        
        self.situacao_nome = 'certo'
        self.situacao_telef = 'certo'

        while True:
            while True:
                try:
                    for i in self.nome:
                        if i.isnumeric():
                            print('digite apenas LETRAS')
                            self.situacao_nome = 'erro'
                            raise Exception('O nome não pode conter números!')
                        else:
                            print('só tem letra')
                except Exception as erro:    
                    self.situacao_nome = 'erro'
                    self.text_adicionado = Label(self.frame_adicionar, text=f'ERRO! {erro}', font='Arial 18', bg='#00BFFF')
                    self.text_adicionado.place(x=200, y=420, width=800)
                    break

                else:
                    break

            while True:
                try:
                    for i in self.telefone:
                        if i.isnumeric():
                            print('numero')
                        else:
                            self.situacao_telef = 'erro'
                            print('digite apenas números')
                            raise Exception('O telefone só pode conter números!')
                except Exception as erro:    
                    self.situacao_telef = 'erro'
                    self.text_adicionado = Label(self.frame_adicionar, text=f'ERRO! {erro}', font='Arial 18', bg='#00BFFF')
                    self.text_adicionado.place(x=200, y=420, width=800)
                    break
                else:
                    break

            if self.situacao_nome == 'certo' and self.situacao_telef == 'certo':

                self.conexao = sqlite3.connect('registro_reclamacoes.db') 
                self.sql = self.conexao.cursor()

                self.sql.execute(f"INSERT INTO registro_reclamacoes (nome) VALUES ('{self.nome}')")
                
                self.sql.execute(f"UPDATE registro_reclamacoes SET email = '{self.email}' WHERE nome = '{self.nome}'")
                self.sql.execute(f"UPDATE registro_reclamacoes SET telefone = '{self.telefone}' WHERE nome = '{self.nome}'")
                self.sql.execute(f"UPDATE registro_reclamacoes SET titulo = '{self.titulo}' WHERE nome = '{self.nome}'")
                self.sql.execute(f"UPDATE registro_reclamacoes SET reclamacao = '{self.msg_reclamacao}' WHERE nome = '{self.nome}'")

                self.conexao.commit()
                self.conexao.close()   


                self.nome_add.delete(0,END)
                self.email_add.delete(0,END)
                self.telef_add.delete(0,END)
                self.title_reclamacao.delete(0,END)
                self.add_reclamacao.delete(0,END)
                break

            else:
                print('não pode adicionar')
                break
                    
                
                    


    def excluir(self):
        self.frame_excluir= Frame(self.frame_content, height=500, width=1100, bd = 4, bg='#00BFFF')
        self.frame_excluir.place(x=-4, y=0)

        self.bt_adicionar = Button(self.frame_nav, command=self.adicionar, text='Adicionar',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_adicionar.place(x=110, y=12)

        self.bt_excluir = Button(self.frame_nav, command=self.excluir, text='Excluir',font='Arial 10 bold', height=2, width=20, bg="#fb3139")
        self.bt_excluir.place(x=350, y=12)

        self.bt_consultar = Button(self.frame_nav, command=self.consultar, text='Consultar',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_consultar.place(x=590, y=12)

        self.bt_fazer_backup = Button(self.frame_nav, command=self.backup, text='Backup',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_fazer_backup.place(x=830, y=12)

        self.text_excluir = Label(self.frame_excluir, text='Insira o título da reclamação:  ', font='Arial 20', bg='#00BFFF')
        self.text_excluir.place(x=70,y=15)

        self.ex_reclamacao = Entry(self.frame_excluir, font='Helvetica 16', bg='#F7FFF7')
        self.ex_reclamacao.place(x=70,y=60, height = 30, width = 400)

        self.bt_ver = Button(self.frame_excluir, text='Conferir', width=5, height=1, bg='white', command=self.ver_reclamacao)
        self.bt_ver.place(x=480, y=60)

        self.mostrar_reclamacao = LabelFrame(self.frame_excluir, text = 'Descrição da reclamação', bg='white')
        self.mostrar_reclamacao.place(x=70, y=110, height = 130, width = 600, anchor = 'nw')

        self.Label_mostrar = Label(self.frame_excluir, font = 'Arial 16 bold', text = '', bg='white')
        self.Label_mostrar.place(x = 80, y = 130, height = 80, width = 555, anchor = 'nw')

        self.imagemExcluir = PhotoImage(file='apagar_reclamacoes.png').subsample(3)

        self.imagem_apagar = Label(self.frame_excluir,image=self.imagemExcluir, width=300, height=350, bg='#00BFFF')
        self.imagem_apagar.place(x=710, y=0)

        self.bt_apagar = Button(self.frame_excluir, text='Excluir reclamação', width=40, height=2, bg='#FF6666', command=self.apagado)
        self.bt_apagar.place(x=80, y=300)

    def ver_reclamacao(self):

        self.con = sqlite3.connect('registro_reclamacoes.db')
        self.sql = self.con.cursor()

        self.sql.execute("SELECT * FROM registro_reclamacoes")

        self.registros = self.sql.fetchall()

        self.situacao_titulo = ''
        for reg in self.registros: 
            if self.ex_reclamacao.get() == reg[3]:
                self.situacao_titulo = 'existe'
            else:
                print()

        if self.situacao_titulo == 'existe':
            self.sql.execute(f"SELECT reclamacao FROM registro_reclamacoes WHERE titulo = '{self.ex_reclamacao.get()}'")
            self.registros = self.sql.fetchone()
            self.Label_mostrar = Label(self.frame_excluir, font = 'Arial 16 bold', text = f'{self.registros[0]}', bg='white')
            self.Label_mostrar.place(x = 80, y = 130, height = 80, width = 555, anchor = 'nw')
        

        else:
            self.Label_mostrar = Label(self.frame_excluir, font = 'Arial 16 bold', text = f'Titulo não encontrado', bg='white')
            self.Label_mostrar.place(x = 80, y = 130, height = 80, width = 555, anchor = 'nw')


    def apagado(self): 

        self.conexao = sqlite3.connect('registro_reclamacoes.db') 
        self.sql = self.conexao.cursor()

        self.sql.execute("SELECT * FROM registro_reclamacoes")
        self.registros = self.sql.fetchall()

        self.situacao_titulo = ''
        for reg in self.registros: 
            if self.ex_reclamacao.get() == reg[3]:
                self.situacao_titulo = 'existe'
            else:
                print()

        if self.situacao_titulo == 'existe':
            self.sql.execute(f"DELETE FROM registro_reclamacoes WHERE titulo == '{self.ex_reclamacao.get()}'")
            self.conexao.commit()
            self.conexao.close()

            self.ex_reclamacao.delete(0,END)
            self.Label_mostrar = Label(self.frame_excluir, font = 'Arial 16 bold', text = '', bg='white')
            self.Label_mostrar.place(x = 80, y = 130, height = 80, width = 555, anchor = 'nw')

            self.text_apagado = Label(self.frame_excluir, text='Reclamação excluída com sucesso! ', font='Arial 21', bg='#00BFFF')
            self.text_apagado.place(x=320,y=420)

        else:
            self.Label_mostrar = Label(self.frame_excluir, font = 'Arial 16 bold', text = f'Titulo não encontrado', bg='white')
            self.Label_mostrar.place(x = 80, y = 130, height = 80, width = 555, anchor = 'nw')





    def consultar(self):
        self.frame_consultar= Frame(self.frame_content, height=500, width=1100, bd = 4, bg='#00BFFF')
        self.frame_consultar.place(x=-4, y=0)

        self.bt_consultar = Button(self.frame_nav, command=self.consultar, text='Consultar',font='Arial 10 bold', height=2, width=20, bg='#fb3139')
        self.bt_consultar.place(x=590, y=12)

        self.bt_adicionar = Button(self.frame_nav, command=self.adicionar, text='Adicionar',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_adicionar.place(x=110, y=12)

        self.bt_excluir = Button(self.frame_nav, command=self.excluir, text='Excluir',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_excluir.place(x=350, y=12)

        self.bt_fazer_backup = Button(self.frame_nav, command=self.backup, text='Backup',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_fazer_backup.place(x=830, y=12)


        self.text_consultar = Label(self.frame_consultar, text='Insira o título da reclamação:  ', font='Arial 20', bg='#00BFFF')
        self.text_consultar.place(x=70,y=15)

        self.cons_reclamacao = Entry(self.frame_consultar, font='Helvetica 16', bg='#F7FFF7')
        self.cons_reclamacao.place(x=430,y=18, height = 30, width = 400)

        self.info_cons = Label(self.frame_consultar, text='Informações da consulta: ', font='Arial 20', bg='#00BFFF')
        self.info_cons.place(x=70,y=100)

        self.nome_cons = Label(self.frame_consultar, text='Nome: ', font='Arial 16', bg='#00BFFF')
        self.nome_cons.place(x=70,y=140)

        self.nome_box = Label(self.frame_consultar, text='', font='Arial 20', bg='white', anchor='w')
        self.nome_box.place(x=150,y=140, height=30, width=365)

        self.email_cons = Label(self.frame_consultar, text='Email: ', font='Arial 16', bg='#00BFFF')
        self.email_cons.place(x=70,y=180)

        self.email_box = Label(self.frame_consultar, text='', font='Arial 20', bg='white', anchor='w')
        self.email_box.place(x=150,y=180, height=30, width=365)

        self.telef_cons = Label(self.frame_consultar, text='Telefone: ', font='Arial 16', bg='#00BFFF')
        self.telef_cons.place(x=70,y=220)

        self.telef_box = Label(self.frame_consultar, text='', font='Arial 20', bg='white', anchor='w')
        self.telef_box.place(x=180,y=220, height=30, width=335)

        self.reclamacao_cons = Label(self.frame_consultar, text='Reclamação: ', font='Arial 17', bg='#00BFFF')
        self.reclamacao_cons.place(x=70,y=270)

        self.reclamacao_box = Label(self.frame_consultar, text='', font='Arial 20', bg='white', anchor='w')
        self.reclamacao_box.place(x=70,y=310, height = 70, width = 450)

        self.imagemConsultar = PhotoImage(file='consultar_reclamacoes.png').subsample(3)

        self.imagem_consultar = Label(self.frame_consultar,image=self.imagemConsultar, width=300, height=350, bg='#00BFFF')
        self.imagem_consultar.place(x=670, y=0)

        self.bt_consultar = Button(self.frame_consultar, text='Consultar reclamação', width=40, height=2, bg='#FF6666', command=self.consultado)
        self.bt_consultar.place(x=650, y=320)



        
    def consultado(self): 
        self.text_consultado = Label(self.frame_consultar, text='Reclamação consultada com sucesso! ', font='Arial 21', bg='#00BFFF')
        self.text_consultado.place(x=320,y=420)

        self.con = sqlite3.connect('registro_reclamacoes.db')
        self.sql = self.con.cursor()

        self.sql.execute("SELECT * FROM registro_reclamacoes")

        registros = self.sql.fetchall()

        self.situacao_titulo = ''

        for reg in self.registros: 
            if self.cons_reclamacao.get() == reg[3]:
                self.situacao_titulo = 'existe'
            else:
                print()

        if self.situacao_titulo == 'existe':

            for reg in registros:
                if reg[3] == f'{self.cons_reclamacao.get()}':

                    self.nome_box = Label(self.frame_consultar, text=f'{reg[0]}', font='Arial 20', bg='white',anchor='w')
                    self.nome_box.place(x=150,y=140, height=30, width=365)

                    self.email_box = Label(self.frame_consultar, text=f'{reg[1]}', font='Arial 20', bg='white',anchor='w')
                    self.email_box.place(x=150,y=180, height=30, width=365)

                    self.telef_box = Label(self.frame_consultar, text=f'{reg[2]}', font='Arial 20', bg='white',anchor='w')
                    self.telef_box.place(x=180,y=220, height=30, width=335)

                    self.reclamacao_box = Label(self.frame_consultar, text=f'{reg[4]}', font='Arial 20', bg='white',anchor='w')
                    self.reclamacao_box.place(x=70,y=310, height = 70, width = 450)

            print()






    def backup(self):
        self.frame_backup = Frame(self.frame_content, height=500, width=1100, bd = 4, bg='#00BFFF')
        self.frame_backup.place(x=-4, y=0)

        self.bt_adicionar = Button(self.frame_nav, command=self.adicionar, text='Adicionar',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_adicionar.place(x=110, y=12)

        self.bt_excluir = Button(self.frame_nav, command=self.excluir, text='Excluir',font='Arial 10 bold', height=2, width=20, bg="#FF6666")
        self.bt_excluir.place(x=350, y=12)

        self.bt_consultar = Button(self.frame_nav, command=self.consultar, text='Consultar',font='Arial 10 bold', height=2, width=20, bg='#FF6666')
        self.bt_consultar.place(x=590, y=12)

        self.bt_fazer_backup = Button(self.frame_nav, command=self.backup, text='Backup',font='Arial 10 bold', height=2, width=20, bg='#fb3139')
        self.bt_fazer_backup.place(x=830, y=12)

        self.text_backup = Label(self.frame_backup, text='Backup do registro de reclamações  ', font='Arial 20', bg='#00BFFF')
        self.text_backup.place(x=100,y=20)

        self.bt_dumpbackup = Button(self.frame_backup, command=self.dumpbackup, text='Fazer o backup dos registros',font='Arial 10 bold', height=2, width=30, bg='white')
        self.bt_dumpbackup.place(x=100, y=90)

        self.bt_loadbackup = Button(self.frame_backup, command=self.loadbackup, text='Baixar o backup dos registros',font='Arial 10 bold', height=2, width=30, bg='white')
        self.bt_loadbackup.place(x=100, y=150)

        self.imagemBackup = PhotoImage(file='backup_reclamacoes.png').subsample(3)

        self.imagem_backup = Label(self.frame_backup,image=self.imagemBackup, width=300, height=350, bg='#00BFFF')
        self.imagem_backup.place(x=670, y=0)





    def dumpbackup(self):
        self.text_backupConcluido = Label(self.frame_backup, text='Backup concluído ', font='Arial 20', bg='#00BFFF')
        self.text_backupConcluido.place(x=450,y=400)

        self.con = sqlite3.connect('registro_reclamacoes.db')
        self.sql = self.con.cursor()

        self.sql.execute("SELECT * FROM registro_reclamacoes")

        self.registros = self.sql.fetchall()

        self.list_registro = []

        for reg in self.registros:
            print(reg)
            self.lista = []
            self.lista.append(reg[0])
            self.lista.append(reg[1])
            self.lista.append(reg[2])

            self.reclamacao = {'titulo': reg[3], 'msg_reclamacao': reg[4]}
            self.lista.append(self.reclamacao)

            self.list_registro.append(self.lista)


        self.arq = open('backup_reclamacoes.bin','wb')
        pickle.dump(self.list_registro, self.arq)
        print(self.list_registro)

    def loadbackup(self):
        self.text_backupConcluido = Label(self.frame_backup, text='Baixando Backup', font='Arial 20', bg='#00BFFF')
        self.text_backupConcluido.place(x=450,y=400)

        self.arq = open("backup_reclamacoes.bin",'rb')
        self.backup_loaded = pickle.load(self.arq)

        print(self.backup_loaded)

        for reg in self.backup_loaded:

            self.nome = reg[0]
            self.email = reg[1]
            self.telefone = reg[2]
            self.titulo = reg[3]['titulo']
            self.msg_reclamacao = reg[3]['msg_reclamacao']


            self.conexao = sqlite3.connect('registro_reclamacoes.db') 
            self.sql = self.conexao.cursor()

            self.sql.execute(f"INSERT INTO registro_reclamacoes (nome) VALUES ('{self.nome}')")
            
            self.sql.execute(f"UPDATE registro_reclamacoes SET email = '{self.email}' WHERE nome = '{self.nome}'")
            self.sql.execute(f"UPDATE registro_reclamacoes SET telefone = '{self.telefone}' WHERE nome = '{self.nome}'")
            self.sql.execute(f"UPDATE registro_reclamacoes SET titulo = '{self.titulo}' WHERE nome = '{self.nome}'")
            self.sql.execute(f"UPDATE registro_reclamacoes SET reclamacao = '{self.msg_reclamacao}' WHERE nome = '{self.nome}'")

            self.conexao.commit()
            self.conexao.close()   
        

    


        

 
import os

arquivo = "registro_reclamacoes.db"
if os.path.exists(arquivo):
    os.remove('registro_reclamacoes.db')
    api = Sistema()
else:
    api = Sistema()


