from random import randint


class RollDices:
    def rolar(self, numero):
        return randint(0, numero - 1)

    def probabilidade(self, evento, espaco_amostral):
        if self.rolar(espaco_amostral)+1 < evento + 1:
            return True
        return False

    def parImpar(self):
        return randint(1, 2)
