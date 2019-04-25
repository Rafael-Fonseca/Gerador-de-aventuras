import rolarDados;
import gerarPersonagem;

'''
As perguntas abaixo fomentam o sistema com informações necessárias para que a IA gere, no futuro, do verbo ainda não gera, aventuras aleatórias e complexas
'''

#qtdJogadores vai servir para equilibrar a qtd de inimigos em cada confronto de batalha.
qtdJogadores = int(input("Para quantos jogadores é esta aventura?\n"))

#qtdViloesPrincipais vai servir para distribuir os maiores desafios da aventura. 
qtdViloesPrincipais = int(input("Quantos vilões principais terá a aventura?\n"))

#tipoXp vai servir para o calculo da XP total que a aventura deve abarcar.
tipoXp = input("A experiência necessária para upar de level é escalável?(s/n)\n")
'''
Essa pergunta necessita de outros tratamentos
'''
if tipoXp == 'n':
    #qtdXpPorLevel vai servir para o cálculo da XP total que a aventura deve abarcar.
    qtdXpPorLevel = int(input("Quanta experiência é necessária para evoluir um level?\n"))
else:
    #qtdXpLevel1 e qtdIncrementoPorLevel vão servir para o cálculo da XP total que a aventura deve abarcar.
    qtdXpLevel1 = int(input("Quanta experiência é necessária para passar do primeiro level?\n"))
    qtdIncrementoPorLevel = int(input("De quanto é o incremento da experiência necessária para passar de level?\n"))

#lvlMaximo vai servir para o cálculo da XP total que a aventura deve abarcar.
lvlMaximo = int(input("Qual o level máximo do seu sistema de RPG?\n"))

#qtdXpPorConfronto vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfronto = int(input("Quantos pontos de experiência cada confronto normal concede?\n"))

#qtdXpPorConfrontoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfrontoDificil = int(input("Quantos pontos de experiência cada confronto difícil concede?\n"))

#qtdXpPorConfrontoMuitoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfrontoMuitoDifícil = int(input("Quantos pontos de experiência cada confronto muito difícil concede?\n"))

#porcentagemConfronto vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
porcentagemConfronto = int(input("Qual será a porcentagem de confrontos normais nesta aventura?\n"))/100

#porcentagemConfrontoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
porcentagemConfrontoDificil = int(input("Qual será a porcentagem de confrontos difíceis nesta aventura?\n"))/100

#porcentagemConfrontoMuitoDificil vai ser calculada a partir da diferença do total menos os outros confrontos
porcentagemConfrontoMuitoDificil = 1 - (porcentagemConfronto + porcentagemConfrontoDificil)


#Cabeçalho da questão
print("\nVocê será indagado sobre a porcetagem dos tipos de confronto, a saber: Batalha, Enigmas, Armadilhas, Obstáculos, Sobrevivência.")
print("O somatório deve ser igual a 100.\n")

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoBatalha = int(input("Porcentagem de batalhas?\n"))/100

#tipoConfrontoEnigma vai servir para diversificar os confrontos da aventura.
tipoConfrontoEnigma = int(input("Porcentagem de enigmas?\n"))/100

#tipoConfrontoArmadilhas vai servir para diversificar os confrontos da aventura.
tipoConfrontoArmadilha = int(input("Porcentagem de armadilhas?\n"))/100 

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoObstaculos = int(input("Porcentagem de obstáculos?\n"))/100 

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoSobrevivencia = int(input("Porcentagem de sobrevivência?\n"))/100

'''
Essas perguntas necessitam de tratamento especial
'''

#qtdNpcsBons vai servir para dar profundidade na história
qtdNpcsBons = int(input("Quantos NPCs ajudarão os aventureiros?\n"))

#qtdNpcsRuins, serve para o mesmo que qtdNpcsBons
qtdNpcsRuins = int(input("Quantos NOCs ajudarão os vilões?\n"))

#traicao vai servir para setar a maior quantidade possível de traições.
traicao = int(input("Quantas traições destes NPCs podem haver?\n"))

#qtdMissoesLaterais nome auto explicativo.
qtdMissoesLaterais = int(input("Quantas missões laterais você quer?\n"))

'''
Necessário uma função que solicite os nomes dos chefões das missões laterais enquanto qtd de nomes < qtdMissoesLaterais
'''

#qtdItensMagicos nome auto explicativo
qtdItensMagicos = int(input("Quantos itens mágicos ou especiais existirão?\n"))

estacoes = input("Estações iguais ao planeta terra?(s/n)\n")

if estacoes == 's':
    ordemEstacoes = ["primavera" , "verão" , "outono" , "inverno"]
else:
    qtdEstacoes = int(input("Quantas estações existem?\n"))
    ordemEstacoes = input("Escreva o nome das estações em ordem cronológica, separadas apenas por um caractere de espaço.\n")
    ordemEstacoes = ordemEstacoes.split()
'''
Necessário um código que compare a quantidade de estações com o tamanho do vetor, e caso não seja o mesmo solicite novamente os dados
'''

#limiteTempoMissaoPrincipal
#limiteTempoMissaoLateral      
#qtdLocaisImportantes                  Nomes auto explicativos

limiteTempoMissaoPrincipal = input("Existe limite de tempo para a missão principal?(s/n)\n")
limiteTempoMissaoLateral = input("Existe limite de tempo para as missões laterais?(s/n)\n")
qtdLocaisImportantes = int(input("Quantos locais importantes existem?\n"))



############################################################### Tratamento de Entradas #############################################################################

############################# VILÕES
viloes = []

contador = 0
while contador < qtdViloesPrincipais:
    viloes[contador] = gerarPersonagem.gerarPersonagem()
    contador += 1

    
############################ TOTAL DE EXPERIÊNCIA A SER CONCEDIDA
if tipoXp == 'n':#Não escalavel
    totalXp = qtdXpPorLevel * lvlMaximo
else: #Escalavel
    totalXp = (qtdXpLevel1 + (qtdXpLevel1 + (lvlMaximo - 1)*qtdIncrementoPorLevel)) * lvlMaximo/2
    

########################### QUANTIDADE DE CADA NÍVEL DE CONFRONTOS
xpConfrontoNormal = totalXp * porcentagemConfronto
xpConfrontoDificil = totalXp * porcentagemConfrontoDificil
xpConfrontoMuitoDificil = totalXp * porcentagemConfrontoMuitoDificil

qtdConfrontoNormal = xpConfrontoNormal / qtdXpPorConfronto
if xpConfrontoNormal % qtdXpPorConfronto > 0:
    qtdConfrontoNormal = int(xpConfrontoNormal / qtdXpPorConfronto) + 1

qtdConfrontoDificil = xpConfrontoDificil / qtdXpPorConfrontoDificil
if xpConfrontoDificil % qtdXpPorConfrontoDificil > 0:
    qtdConfrontoDificil = int(xpConfrontoDificil / qtdXpPorConfrontoDificil) + 1

qtdConfrontoMuitoDificil = xpConfrontoMuitoDificil / qtdXpPorConfrontoMuitoDificil
if xpConfrontoMuitoDificil % qtdXpPorConfrontoMuitoDificil > 0:
    qtdConfrontoMuitoDificil = int(xpConfrontoMuitoDificil / qtdXpPorConfrontoMuitoDificil) + 1


########################### QUANTIDADE DE CADA TIPO DE CONFRONTOS

qtdConfrontoBatalha_N  = int(qtdConfrontoNormal * tipoConfrontoBatalha)
qtdConfrontoBatalha_D  = int(qtdConfrontoDificil * tipoConfrontoBatalha)
qtdConfrontoBatalha_MD = int(xpConfrontoMuitoDificil * tipoConfrontoBatalha)

qtdConfrontoEnigma_N  = int(qtdConfrontoNormal * tipoConfrontoEnigma)
qtdConfrontoEnigma_D  = int(qtdConfrontoDificil * tipoConfrontoEnigma)
qtdConfrontoEnigma_MD = int(xpConfrontoMuitoDificil * tipoConfrontoEnigma)

qtdConfrontoArmadilha_N  = int(qtdConfrontoNormal * tipoConfrontoArmadilha)
qtdConfrontoArmadilha_D  = int(qtdConfrontoDificil * tipoConfrontoArmadilha)
qtdConfrontoArmadilha_MD = int(xpConfrontoMuitoDificil * tipoConfrontoArmadilha)

qtdConfrontoObstaculo_N  = int(qtdConfrontoNormal * tipoConfrontoObstaculos)
qtdConfrontoObstaculo_D  = int(qtdConfrontoDificil * tipoConfrontoObstaculos)
qtdConfrontoObstaculo_MD = int(xpConfrontoMuitoDificil * tipoConfrontoObstaculos)

qtdConfrontoSobrevivencia_N  = int(qtdConfrontoNormal * tipoConfrontoSobrevivencia)
qtdConfrontoSobrevivencia_D  = int(qtdConfrontoDificil * tipoConfrontoSobrevivencia)
qtdConfrontoSobrevivencia_MD = int(xpConfrontoMuitoDificil * tipoConfrontoSobrevivencia)

acerto = qtdConfrontoBatalha_N + qtdConfrontoEnigma_N + qtdConfrontoArmadilha_N + qtdConfrontoObstaculo_N + qtdConfrontoSobrevivencia_N
if (acerto != qtdConfrontoNormal):
    qtdConfrontoBatalha_N += qtdConfrontoNormal - acerto

acerto = qtdConfrontoBatalha_D + qtdConfrontoEnigma_D + qtdConfrontoArmadilha_D + qtdConfrontoObstaculo_D + qtdConfrontoSobrevivencia_D
if (acerto != qtdConfrontoDificil):
    qtdConfrontoBatalha_D += qtdConfrontoDificil - acerto

acerto = qtdConfrontoBatalha_MD + qtdConfrontoEnigma_MD + qtdConfrontoArmadilha_MD + qtdConfrontoObstaculo_MD + qtdConfrontoSobrevivencia_MD
if (acerto != qtdConfrontoMuitoDificil):
    qtdConfrontoBatalha_MD += qtdConfrontoMuitoDificil - acerto


############################# NPCS BONS
npcsBons = []

contador = 0
while contador < qtdNpcsBons:
    npcsBons[contador] = gerarPersonagem.gerarPersonagem()
    contador += 1


############################# NPCS RUINS
npcsRuins = []

contador = 0
while contador < qtdNpcsRuins:
    npcsRuins[contador] = gerarPersonagem.gerarPersonagem()
    contador += 1


############################# TRAIÇÕES
npcTraidor = ""

contador = 0
counterNpcs = 0
while counterNpcs < len(npcsBons)+len(npcsRuins):
    if rolarDados.probabilidade(rolarDados.rolar(20),100): #Duplo Check para traição
        if rolarDados.parImpar() < 2: #Se for impar traição NPC Bom para Ruim
            npcTraidor += "Traição Bom/Ruim " + (counterNpcs+1) + "\n"
            contador += 1
        else:
            npcTraidor += "Traição Bom/Ruim " + (counterNpcs+1) + "\n"
            contador += 1
            counterNpcs += 1
            
    if contador < traicao+1 :
        break

   
#print("Ok")
