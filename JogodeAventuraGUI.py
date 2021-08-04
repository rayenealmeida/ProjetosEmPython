import PySimpleGUI as sg
class jogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Vai haver uma guerra entre duas casas e vocẽ será direcionado para a sua. Vocẽ chega na escola de magia e bruxaria de Hogwarts e precisa de escolher qual local você quer para ser a sala comunal da sua casa. A professora te entrega um mapa com duas direções, e você precisa ir em apenas uma delas. Você gostaria de ir ao subsolo ou à torre? (s/t)' #subsolo = sonserina e torre = grifinória
        self.pergunta2 = 'Chegando no local da sua casa, vocẽ é levada para escolher qual criatura te chama mais atenção. E isso te ajudará a saber o seu camminho. Você prefere um grifo ou uma cobra? (grifo/cobra) ' #grifo = grifinória e cobra = sonserina
        self.pergunta3 = 'Você está com pouco tempo e precisa de ir até a biblioteca para estudar para o teste de amanhã, portato há uma regra que diz que é proibido estar fora da cama após as 22 horas, e você acabou de chegar da escolha da criatura. Então você escolhe seguir sempre as regras ou ir contra as regras? (seguir/ir contra) ' # seguir sempre as regras = grifinória e ir contra as regras = sonserina
        self.pergunta4 = 'Após o teste, você foi levado para a quadra para escolher por fim qual elemento te representa. Qual elemento você vai escolher? terra ou fogo? (t/f) ' #terra = sonserina e fogo = grifinória
        self.finalHistoria1 = 'Parabéns! Vocẽ venceu a guerra das casas. O Barão Sangrento vai ficar feliz em te conhecer'  
        self.finalHistoria2 = 'Perdeu seu cara de Trouxa!'
        self.finalHistoria3 = 'Parabéns! Vocẽ venceu a guerra das casas. Eu amo essa sua ambição!'
        self.finalHistoria4 = 'Perdeu!Sangue ruim!'
        self.finalHistoria5 = 'Perdeu!Aborto!'
        self.finalHistoria6 = 'Parabéns! Vocẽ venceu a guerra das casas. Isso que é ter inteligência!'
        self.finalHistoria7 = 'Parabéns! Vocẽ venceu a guerra das casas. Isso se chama Determinação!'
        self.finalHistoria8 = 'Perdeu! você deve ser um Weasley'

    def iniciar(self):
        # layout
        layout = [ 
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0))],
            [sg.Button('Iniciar'), sg.Button('Responder')]
        ]
        # Criar uma janela
        self.janela = sg.Window('Jogo de aventura!', layout=layout)
        while True:
            # Ler os dados
            self.LerValores()
            #Fazer algo com os dados 
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                
                if self.valores['escolha']== 'subsolo':
                    print(self.finalHistoria1)
                    print(self.pergunta2)
                    self.LerValores()
                if self.valores['escolha'] == 'torre':
                    print(self.finalHistoria2)
                    print(self.pergunta2)
                    self.LerValores()

                if self.valores['escolha']== 'cobra':
                    print(self.finalHistoria3)
                    print(self.pergunta3)
                    self.LerValores()
                if self.valores['escolha'] == 'grifo':
                    print(self.finalHistoria4)
                    print(self.pergunta3)
                    self.LerValores()

            
                if self.valores['escolha'] == 'seguir':
                    print(self.finalHistoria5)
                    print(self.pergunta4)
                    self.LerValores()
                if self.valores['escolha'] == 'ir contra':
                    print(self.finalHistoria6)
                    print(self.pergunta4)
                    self.LerValores()

                if self.valores['escolha'] == 'terra':
                    print(self.finalHistoria7)
                if self.valores['escolha'] == 'fogo':
                    print(self.finalHistoria8)


    def LerValores(self):
        self.evento, self,valores = self.janela.Read()

jogo = jogoDeAventura()
jogo.iniciar()