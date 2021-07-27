# Decida por mim
# Faça uma pergunta para o programa e ele terá que dar uma resposta
import random
class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que está na hora certa!'
        ]
    def iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim() 
decida.iniciar()
