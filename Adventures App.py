import rolarDados;

'''
As perguntas abaixo fomentam o sistema com informações necessárias para que a IA gere aventuras aleatórias e complexas
'''

#qtdJogadores vai servir para equilibrar a qtd de inimigos em cada confronto de batalha.
qtdJogadores = input("Para quantos jogadores é esta aventura?\n")

#qtdViloesPrincipais vai servir para distribuir os maiores desafios da aventura. 
qtdViloesPrincipais = input("Quantos vilões principais terá a aventura?\n")

#tipoXp vai servir para o calculo da XP total que a aventura deve abarcar.
tipoXp = input("A experiência necessária para upar de level é escalável?(s/n)\n")
'''
Essa pergunta necessita de outros tratamentos
'''
if tipoXp == 'n':
    #qtdXpPorLevel vai servir para o cálculo da XP total que a aventura deve abarcar.
    qtdXpPorLevel = input("Quanta experiência é necessária para evoluir um level?\n")
else:
    #qtdXpLevel1 e qtdIncrementoPorLevel vão servir para o cálculo da XP total que a aventura deve abarcar.
    qtdXpLevel1 = input("Quanta experiência é necessária para passar do primeiro level?\n")
    qtdIncrementoPorLevel = input("De quanto é o incremento da experiência necessária para passar de level?\n")

#lvlMaximo vai servir para o cálculo da XP total que a aventura deve abarcar.
lvlMaximo = input("Qual o level máximo do seu sistema de RPG?\n")

#qtdXpPorConfronto vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfronto = input("Quantos pontos de experiência cada confronto normal concede?\n")

#qtdXpPorConfrontoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfrontoDificil = input("Quantos pontos de experiência cada confronto difícil concede?\n")

#qtdXpPorConfrontoMuitoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
qtdXpPorConfrontoMuitoDifícil = input("Quantos pontos de experiência cada confronto muito difícil concede?\n")

#porcentagemConfronto vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
porcentagemConfronto = input("Qual será a porcentagem de confrontos normais nesta aventura?\n")

#porcentagemConfrontoDificil vai servir para a divisão da XpTotal(Variável esta ainda não criada) pela quantidade de confrontos.
porcentagemConfrontoDificil = input("Qual será a porcentagem de confrontos difíceis nesta aventura?\n")

#porcentagemConfrontoMuitoDificil vai ser calculada a partir da diferença do total menos os outros confrontos
porcentagemConfrontoMuitoDificil = 100 - ((int)(porcentagemConfronto) + (int)(porcentagemConfrontoDificil))


#Cabeçalho da questão
print("\nVocê será indagado sobre a porcetagem dos tipos de confronto, a saber: Batalha, Enigmas, Armadilhas, Obstáculos, Sobrevivência.")
print("O somatório deve ser igual a 100.\n")

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoBatalha = input("Porcentagem de batalhas?\n")

#tipoConfrontoEnigma vai servir para diversificar os confrontos da aventura.
tipoConfrontoEnigma = input("Porcentagem de enigmas?\n")

#tipoConfrontoArmadilhas vai servir para diversificar os confrontos da aventura.
tipoConfrontoArmadilha = input("Porcentagem de armadilhas?\n")

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoObstáculos = input("Porcentagem de obstáculos?\n")

#tipoConfrontoBatalha vai servir para diversificar os confrontos da aventura.
tipoConfrontoSobrevivência = input("Porcentagem de sobrevivência?\n")

'''
Essas perguntas necessitam de tratamento especial
'''

#qtdNpcsBons vai servir para dar profundidade na história
qtdNpcsBons = input("Quantos NPCs ajudarão os aventureiros?\n")

#qtdNpcsRuins, serve para o mesmo que qtdNpcsBons
qtdNpcsRuins = input("Quantos NOCs ajudarão os vilões?\n")

#traicao vai servir para setar a maior quantidade possível de traições.
traicao = input("Quantas traições destes NPCs podem haver?\n")

#qtdMissoesLaterais nome auto explicativo.
qtdMissoesLaterais = input("Quantas missões laterais você quer?\n")

'''
Necessário uma função que solicite os nomes dos chefões das missões laterais enquanto qtd de nomes < qtdMissoesLaterais
'''

#qtdItensMagicos nome auto explicativo
qtdItensMagicos = input("Quantos itens mágicos ou especiais existirão?\n")

estacoes = input("Estações iguais ao planeta terra?(s/n)\n")

if estacoes == 's':
    ordemEstacoes = ["primavera" , "verão" , "outono" , "inverno"]
else:
    qtdEstacoes = input("Quantas estações existem?\n")
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
qtdLocaisImportantes = input("Quantos locais importantes existem?\n")

#print("Ok")
