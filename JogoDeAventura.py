# Jogo de Aventura 
# Um jogo de decisões onde eu terei que criar vários finais diferentes baseados nas respostas que forem dadas
# chegar em finais diferentes na minha historia de acordo com as respostas que eu passe para o programa

#Cenário; Guerra entre duas casas: grifinória e sonserina. Somente sonserina irá vencer, e grifinória irá perder! então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente sonserina ira conseguir! 
class jogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Vai haver uma guerra entre duas casas e vocẽ será direcionado para a sua. Vocẽ chega na escola de magia e bruxaria de Hogwarts e precisa de escolher qual local você quer para ser a sala comunal da sua casa. A professora te entrega um mapa com duas direções, e você precisa ir em apenas uma delas. Você gostaria de ir ao subsolo ou à torre? (s/t)' #subsolo = sonserina e torre = grifinória
        self.pergunta2 = 'Chegando no local da sua casa, vocẽ é levada para escolher qual criatura te chama mais atenção. E isso te ajudará a saber o seu camminho. Você prefere um grifo ou uma cobra? (grifo/cobra) ' #grifo = grifinória e cobra = sonserina
        self.pergunta3 = 'Você está com pouco tempo e precisa de ir até a biblioteca para estudar para o teste de amanhã, portato há uma regra que diz que é proibido estar fora da cama após as 22 horas, e você acabou de chegar da escolha da criatura. Então você escolhe seguir sempre as regras ou ir contra as regras? (seguir/ir contra) ' # seguir sempre as regras = grifinória e ir contra as regras = sonserina
        self.pergunta4 = 'Após o teste, você foi levado para para a quadra para escolher por fim qual elemento te representa. Qual elemento você vai escolher? terra ou fogo? (t/f) ' #terra = sonserina e fogo = grifinória
        self.finalHistoria1 = 'O Barão Sangrento vai ficar feliz em te conhecer'  
        self.finalHistoria2 = 'Cara de Trouxa!'
        self.finalHistoria3 = 'Eu amo essa sua ambição'
        self.finalHistoria4 = 'Cara de Trouxa!'

    def iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'subsolo' or resposta1 == 's':
               print(self.finalHistoria1)
        elif resposta1 == 'torre' or resposta1 == 't':
               print(self.finalHistoria2)
               resposta2 = input(self.pergunta2)
        if resposta2 == 'cobra':
               print(self.finalHistoria3)
        elif resposta2 == 'grifo':
               print(self.finalHistoria4)

jogo = jogoDeAventura()
jogo.iniciar()