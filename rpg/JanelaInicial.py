from tkinter import * #Biblioteca Interface


import pymysql


#JANELA PRINCIPAL
class Application(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)





        '''#MUSICA
        import pygame
        pygame.init()
        pygame.mixer.music.load('C://Users//William//PycharmProjects//RPGPYTHON//rpg//Lord of the Rings Theme Song.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
        #MUSICA'''

        #pygame.mixer.unpause()

        # IMAGEM DE FUNDO
        imagemdefundo = PhotoImage(file="fantasyart.png")
        self.w = Label(self, image=imagemdefundo)
        self.w.imagemdefundo = imagemdefundo
        self.w.pack()
        #self.w.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        self.pack()
        self.bg = imagemdefundo

        # BOTÕES
        from rpg import JanelaCadastro
        from rpg import JanelaListaPerson
        self.cperson = Button(self, text='Criar Personagem', command=JanelaCadastro.criarjc)
        self.cperson.place(x=300, y=190)

        self.asperson = Button(self, text='Lista de Personagens', command=JanelaListaPerson.criarjlp)
        self.asperson.place(x=295, y=230)

        def csair():
            app.master.destroy()
        self.sair = Button(self, text='Sair', command=csair)
        self.sair.place(x=335, y=270)


#CONFIGURAÇÕES DA JANELA
app = Application()
app.master.title('RPG Python Tkinter')
app.master.geometry("700x467+350+100")
app.master.resizable(0, 0)
#app.master.maxsize(width=700,height=467)
#app.master.minsize(width=700,height=467)
mainloop()
