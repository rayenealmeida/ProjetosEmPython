import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei',
            'Não faça isso!',
            'Acho que está na hora certa!'
        ]

    def iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]
        #Criar a janela
        self.janela = sg.Window('Decida por mim!',layout=layout)
        while True:
        # ler valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer alguma coisa com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMim() 
decida.iniciar()