import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que está na hora certa!'
        ]
    def iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por mim')]
        ]
        #Criar a janela
        self.janela = sg.Window('Decida por mim!')
        # ler valores
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com os valores
        if self.eventos == 'Decida por mim':
            print(random.choice(self.respostas))
            self.janela.Close()

        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim() 
decida.iniciar()