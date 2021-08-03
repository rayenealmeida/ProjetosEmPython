import random 
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0 
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o numero!',layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber os valores
                self.vento, self.valores = self.janela.Read()
                # Fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores ['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns você acertou!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.iniciar()


    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.iniciar()