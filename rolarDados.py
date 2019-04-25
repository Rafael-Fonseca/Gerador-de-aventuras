import random

def rolar(numero):
    rolado = random.randint(0,numero-1)
    return (rolado)

def select(lista):
    selecionado = lista[rolar(len(lista))]
    return (selecionado)

def probabilidade(evento, espacoAmostral):
    if (rolar(espacoAmostral)+1 < evento + 1):
        return True
    return False

def parImpar():
    rolado = random.randint(1,2)
    return rolado

''' TESTE Def Dentro de outro /// FUNCIONA
def teste2():
    
    def teste():
        return "Funciona"

    testado = teste()
    testado += " Super Teste"
    return testado

vai = teste2()
vai += " Supremo Teste"

print (vai)
'''
