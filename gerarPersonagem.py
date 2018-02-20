import rolarDados;

# Vetores Banco de Dados

def setClass():
    classes = ["bardo", "druida", "espadachim", "feiticeiro", "barbaro", "ladino", "paladino", "patrulheiro", "rúnico", "sacerdote", "xamã"]
    selectedClass = rolarDados.select(classes)
    return selectedClass

def setGenero():
    generos = ["homem", "mulher"]
    selectedGender = rolarDados.select(generos)

    trans = rolarDados.probabilidade(5,75000)
    if selectedGender == "homem":
        trans = rolarDados.probabilidade(5,25000)

    hermafrodita = rolarDados.probabilidade(1,25000)

    if trans
        selectedGender += " trans"
    if hermafrodita
        selectedGender += " hermafrodita"
    return selectedGender

def setSexualidade():
    sexualidade = ["homo","bi","a","pan","demi"]
    selectedSexualidade = "hetero"
    
    if rolarDados.probabilidade(5,100):
        selectedSexualidade = rolarDados.select(sexualidade)
    return selectedSexualidade

def setRacas():
    racas = ["aesir","anã","elfica","faen","fauno","fira","humana", "juban", "levent", "mahok", "tailox", "aquila", "drow", "reptiliano",
             "naga", "bearos", "centauro", "draconiano/a", "equiceph", "genasi", "groton", "globin", "halfling", "lige", "minotauro", "náiade", "orc", "ratling"]
    selectedRace = rolatDados.select(racas)
    return selectedRace

def setPersonalidade():
    tiposPsicologicos = ["reformador(a)", "sedutor(a)", "competidor(a)", "individualista", "investigador(a)", "controlador(a)", "entusiasta", "dominador(a)",
                         "diplomata"]
    qtd = rolarDados.rolar(3)+1
    x = 0
    selectedPersonalidade = ""
    
    while x != qtd
        selectedPersonalidade += rolarDados.select(tiposPsicologicos) + " "
        x += 1
    return selectedPersonalidade

def setPele():
    corPele = ["Azeviche", "Negra", "Mulata", "Parda", "Bronzeada", "Sardenta", "Branca", "Branca pálida", "Amarela", "Trigueira", "Vermelha", "Negra", "Branca",
               "Branca pálida", "Trigueira", "Negra", "Bronzeada", "Branca", "Mulata", "Parda", "Azeviche", "Branca", "Negra", "Vermelha", "Amarela", "Albino",
               "Cicatrizes", "Tatuagens", "Marca de Nascença", "Pele manchada"]

    def cicatrizes(selectedPele, corPele, auxPele):
        if corPele[auxPele] == "Cicatrizes":
            selectedPele += " " + corPele[auxPele]
            if random.randint(1,2)%2 == 0
                selectedPele += " comuns"
            else:
                selectedPele += " ritualisticas"

            return selectedPele
        
        return selectedPele

    def tatuagens(selectedPele, corPele, auxPele):
        if corPele[auxPele] == "Tatuagens":
            selectedPele += " " + corPele[auxPele]
                
            return selectedPele
                
        return selectedPele

    def marca(selectedPele, corPele, auxPele):
        if corPele[auxPele] == "Marca de Nascença":
            selectedPele += " " + corPele[auxPele]
            corPele.remove("Albino")
                
            return selectedPele
                
        return selectedPele

    def mancha(selectedPele, corPele, auxPele):
        if corPele[auxPele] == "Pele manchada":
            if rolarDados.parImpar()%2 == 0:
                selectedPele += " mancha na pele mais clara que a pele"
            else:
                selectedPele += " mancha na pele mais escura que a pele"
            return selectedPele
                
        return selectedPele  

    auxPele = rolarDados.rolar(len(corPele))
    selectedPele = ""
    counter = 1
    
    while auxPele > 25:

        selectedPele += cicatrizes(selectedPele, corPele, auxPele)
        selectedPele += tatuagens(selectedPele, corPele, auxPele)
        selectedPele += marca(selectedPele, corPele, auxPele)
        selectedPele += mancha(selectedPele, corPele, auxPele)

        corPele.remove(corPele[auxPele])
        auxPele = rolarDados.rolar(len(corPele))

    #A linha de baixo coloca valor caso a 1 rolagem seja menor que 26 ou completa no caso de a 1 ter sido maior que 25
    selectedPele += " " + corPele[auxPele]

    return selectedPele
        
def set corOlhos():
    corOlhos = [ "Negro", "Castanho", "Castanho claro", "Castanho escuro", "Castanho esverdeado", "Verde", "Verde esmeralda", "Verde acinzentado", "Azul claro",
                 "Azul escuro", "mel", "Cinzento", "Cinza prateado", "Dourado", "Violeta", "Cor de avelã", "Azul acinzentado", "Vermelho(albino)", "Âmbar",
                 "Azul", "Castanho", "Castanho claro", "Castanho escuro", "Verde oliva", "Caramelo", "Olheiras", "Esclera com veios de sangue",
                 "Esclera amarelada", "Caolho", "Um olho de cada cor"]

    auxCorOlhos = rolarDados.rolar(len(corOlhos))
    selectedCorOlhos = ""
    
    while auxCorOlhos > 24:
        selectedCorOlhos += corOlhos[auxCorOlhos] + " "

        corOlhos.remove(corOlhos[auxCorOlhos])
        auxCorOlhos = rolarDados.rolar(len(corOlhos))

    selectedCorOlhos += corOlhos[auxCorOlhos]

    return selectedCorOlhos
    
def set
    corCabelos = [ "Preto","Castanho escuro","Castanho","Castanho claro","Castanho avermelhado","Vermelho","Ruivo","Acobreado","Louro arruivado","Louro-platinado",
                   "Louro claro","Louro","Louro acinzentado","Louro escuro","Louro dourado","Castanho claro","Castanho","Castanho escuro","Preto","Louro escuro",
                   "Louro","Louro claro","Cinzento","Branco prateado","Branco","Têmporas grisalhas","Grisalho","Calvo","Careca"]
    
    auxCorCabelos = rolarDados.rolar(len(corCabelos))
    selectedCorCabelos = ""

    if corCabelos[auxCorCabelos] == "Careca":
        if rolarDados.parImpar()%2 == 0:
            return "Careca porque raspa"
        else:
            return "Naturalmente careca"

    while auxCorCabelos > 24 and auxCorCabelos < 28:
        selectedCorCabelos += corCabelos[auxCorCabelos] + " "

        corCabelos.remove(corCabelos[auxCorCabelos])
        auxCorCabelos = rolarDados.rolar(len(corCabelos))

    selectedCorCabelos += corCabelos[auxCorCabelos]
    
    return selectedCorCabelos


#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUIIIIIIIIIIIIIIIIIIIIIIIIIII


def set
tiposCabelo = ["Cabelos longos","Cabelos curtos","Cabelo volumoso","Cabelo ralo","Cabelo raspado","Cabelo liso","Cabelo cacheado","Cabelo crespo","Costeletas longas",
               "Suíças proeminentes","Tranças nos cabelos","Dreadlocks","Moicano longo","Moicano curto","Bigode curto","Bigode longo","Bigode fino",
               "Cavanhaque sem bigode","Cavanhaque e bigode","Tranças no cavanhaque","Barba por fazer","Barba rala","Barba curta","Barba crespa","Barba longa",
               "Tranças na barba","Sobrancelhas finas","Sobrancelhas grossas","Sobrancelhas unidas","Sobrancelhas hirsutas"]

    #selectedClass = rolarDados.select(classes)
    #return selectedClass

def set
nascimentoMundano = ["Em uma área montanhosa","Em um casebre no meio do nada","Em um pântano","Em um navio","Em uma floresta","Em uma cidade portuária",
                     "Em um vilarejo","Em uma fortaleza anã","Em um grande centro urbano","Em uma aldeia élfica","Em um monastério ou templo clerical",
                     "Em um reino distante","Durante uma viagem","Em uma fazenda","Em uma ilha","Em uma comunidade halfling","Você não sabe nada sobre seu nascimento",
                     "Em um acampamento de salteadores","Em uma caverna","Em um circo","Em um cemitério","Em um campo de batalha","Em uma cidade de porte médio",
                     "No subterrâneo","Na capital do reino","Em uma cela de prisão","No palácio real","Em um acampamento cigano","Em um deserto",
                     "Em um local completamente destruído"]

def set
nascimentoEspecial = ["Durante um equinócio","Durante um ataque de mortos vivos","Durante o ataque de um dragão","Em uma importante data religiosa",
                      "Durante uma terrível tempestade","Durante a passagem de um cometa","Em uma construção sobre as nuvens","Nas condições de uma antiga profecia",
                      "Durante um solstício","Em uma ilha que afundou","Durante um ataque de orcs","Durante uma chuva de estrelas cadentes","Em um ritual arcano",
                      "Durante uma aurora boreal/austral","Você não nasceu, foi “construído” ou “criado”","Durante um terremoto",
                      "Você não sabe nada sobre seu nascimento","Durante um eclipse lunar","Durante a queda de um meteoro","Prematuramente",
                      "Em um outro plano de existência","No momento da erupção de um vulcão","Debaixo d’água, ou em um reino submerso",
                      "Em um barco voador, ou aparato aéreo","Durante um eclipse solar","Durante uma grande epidemia","No dia extra de um ano bissexto",
                      "Role uma vez nesta tabela e outra na de nascimento mundano","Em outro planeta ou corpo celeste","Role duas vezes nesta tabela"]
'''
FAZER
27 e 29
'''

def set
seusPais = ["Seus pais eram moradores de rua, a classe social mais baixa do populacho",
            "Órfão de um, mas criado pelo outro. (Role para determinar qual morreu: par - pai; impar - mãe)",
            "Órfão de pai e mãe, mas criado por outros (par - parentes. ímpar - não parentes)",
            "Você é completamente órfão e cresceu nas ruas ou em um orfanato","Seus pais são nobres",
            "Um de seus pais é nobre (Role para determinar: par - pai; impar - mãe)",
            "Seus pais são mercadores/comerciantes","Seus pais são ladrões/piratas/foragidos","Seus pais são artistas/artesãos",
            "Seus pais são vivos, mas lhe deram para ser criado por outros (Role: par - parentes; impar - não parentes)",
            "Seus pais são escravos/servos","Seus pais são aventureiros","Você foi adotado por uma raça diferente da sua",
            "Você foi adotado por uma Instituição Religiosa","Você foi adotado por uma Guilda de Ladrões/Mercantes",
            "Seus pais são uma união de duas famílias inimigas","Você é fruto de uma relação incestuosa","Sua mãe não sabe que você ainda vive",
            "Seu pai não sabe que você existe/ainda vive","Você foi abandonado à própria sorte e não sabe nada sobre seus pais","Seus pais são camponeses",
            "Seu pai é um rei","Sua mãe é uma rainha","Um de seus pais morreu e você tem uma madrasta ou padrasto (Role: par - padrasto; impar - madrasta)",
            "Um de seus pais é membro do clero (Role para determinar quem: par - pai; impar - mãe)",
            "Seus pais são separados (Role para determinar quem lhe criou: par - pai; impar - mãe)",
            "Seus pais são separados e você tem madrasta e padrasto","Você é filho de um ser de outro plano/mundo com um habitante deste mundo.",
            "Ambos os seus pais são de outro plano/mundo","Você é um filho bastardo"]
#FAZER 1,2,5,9,22,23,24

def set
houveSorteTragedia = ["Nada aconteceu, você teve uma vida bem mundana e monótona","Role uma vez na tabela TRAGÉDIA","Role uma vez na tabela SORTE",
                      "Role uma vez na tabela SORTE e uma vez na tabela TRAGÉDIA."]

sorte = ["Você herdou bens familiares (uma casa, terras,cavalo, dinheiro, armas, etc.)",
         "Sua infância foi próxima a circos/estábulos/afins e aprendeu coisas que acalmam os animais.",
         "Você ou sua família encontrou um item muito poderoso e desejado.",
         "Independente de seu status social, você conviveu com nobres na corte, e você acabou recebendo educação para se portar entre eles",
         "Você encontrou um mestre que lhe ensinou uma técnica/segredo profissional importante e fenomenal.",
         "Você ou sua família descobriu um segredo importante que pode beneficiá-lo de alguma forma muito vantajosa.",
         "Uma pessoa de poder político ou econômico no reino lhe deve um favor","Você encontrou um mapa que pode guiá-lo a um grande tesouro que pode existir ou não.",
         "Uma criatura poderosa (ex: um gênio, um dragão, uma fada, etc.) lhe deve um favor",
         "Você e sua família estão em boas graças com o clero local. Além disso, você fosse muito bem educado nas tradições religiosas.",
         "Você ou sua família fez um contato poderoso nos altos escalões de governo do reino (um conselheiro/regente/ministro).",
         "Você nasceu em um dia iluminado, e os animais selvagens tendem a reagir positivamente na sua presença e tentativa de contatos.",
         "Você ganhou a confiança de uma guilda ou grupo comum. (de ladrões, de artífices, de mercadores, etc.)",
         "Você tornou-se próximo de membros de uma comunidade de uma outra raça e eles lhe consideram um amigo de seu povo.",
         "Você ganhou a confiança da guilda (de ladrões, de artífices, de mercadores, etc.) mais poderosa do reino",
         "Você tem uma facilidade natural para línguas, podendo aprender qualquer uma (desde que haja alguém com quem aprender).",
         "Sua família está envolvida em uma conspiração, em uma posição confortável",
         "Sua família descende de um grande e famoso herói, e seu sobrenome é muito reconhecido.",
         "Sua família recebeu algum tipo de benção divina ou dom especial",
         "Você possui um ancestral de outra raça e eles o consideram como parente",
         "Seu sangue possui tradição em derrotar certo tipo de criatura",
         "Você tem um dom natural para passar emoções distintas com sua voz, seja um grito em batalha, ameaça numa interrogação, ou um galanteio.",
         "Você adquiriu uma simpatia inexplicável de alguém forte e poderoso",
         "Você puxou só o melhor de seus pais! Sua beleza não passa despercebida pelas outras pessoas.",
         "Você teve acesso a uma vasta biblioteca desde pequeno, tendo contato com outras culturas e línguas desde jovem.",
         "Você herdou um verdadeiro estômago de avestruz, e é capaz de comer coisas que fariam a maioria das pessoas passar mal.",
         "Você cresceu num local pouco lúgrube e isso o tornou mais resistente à doenças.",
         "Um grupo religioso/criminoso vê em você o líder ideal para a organização/igreja.",
         "Você cresceu no campo, aprendendo a utilizar a natureza a sua volta para obter informações",
         "Você é realmente muito sortudo. Role duas vezes nesta tabela."]
'''
FAZER
29
'''

tragedia = ["Sua família perdeu tudo devido a uma traição", "Sua família foi dizimada por monstros. Você pode ou não ser o único sobrevivente.",
            "Sua família faliu devido à má administração","Sua família é afligida por algum tipo de doença.","Sua família foi exilada",
            "Sua família foi vitimada por uma epidemia","Sua família está aprisionada em algum lugar.","Sua família foi escravizada","Sua família desapareceu!",
            "Sua família perdeu tudo com dívidas de jogo","Sua família está envolta em uma conspiração","Você adquiriu algum tipo de vício",
            "Sua família é vive em guerra interna por poder","Você herdou dívidas familiares",
            "Você sofreu um acidente que o deixou com sequelas físicas para sempre (olho perdido, maneta, dedos perdidos, manco, cicatrizes, etc)",
            "Você provocou, inadvertidamente, a destruição de sua família","Você é considerado a ovelha negra da família e desacreditado por seus parentes",
            "Sua família é vítima de uma maldição","Você traiu sua família","Sua família está sendo caçada",
            "Você teve contato com um grande horror sobrenatural que o deixou com sequelas mentais. Quase todos (exceto aqueles mais próximos) o consideram louco.",
            "Sua família sofre com perseguições religiosas ou culturais",
            "Você ou sua família descobriu um segredo importante, e alguém quer garantir que isso continue sendo um segredo.",
            "Você foi responsável pela morte de um membro de sua família",
            "Você foi traído. (Role 1d30 para determinar: 1-10-amigo; 11-20-parente; 21-30-colega de trabalho ou integrante do mesmo grupo)",
            "Você teve um(a) amante, amigo ou parente morto.(Par - Você não sabe quem foi, nem tem pistas do assassino; Impar - Você sabe quem foi o responsável, mas precisa de provas)",
            "Você está sendo caçado por uma guilda poderosa(de ladinos, de comerciantes etc) por algo que fez; há provas que apontam sua culpa no caso (Par - Não foi você quem fez, e as provas são forjadas; Impar - Foi você quem fez, e eles tem provas concretas",
            "Você foi acusado de um crime e hoje é considerado fora-da-lei e perseguido pela guarda do reino. (Par – Você é culpado pelo crime; Impar – Você foi acusado injustamente por um crime que não cometeu)",
            "Você já esteve preso por 1d6 meses",
            "Você é do tipo judiado pela vida. Role duas vezes nesta tabela."]
'''
Fazer
24
25
26
27
28
29
'''

def set
statusInicial = ["Escravo","Plebeu", "Nobre"]

profissaoEscravo = ["Camareiro","Pajem","Escravo Sexual","Prostituta","Bufão","Bobo da Corte","Lenhador","Faxineiro","Provador Real","Trabalhador Braçal",
                    "Estivador","Acrobata","Malabarista","Gladiador","Dançarino","Jardineiro","Coveiro","Tratador de Animais","Limpador de Fossas","Marinheiro",
                    "Remador","Carvoeiro","Mineiro","Garimpeiro","Pedreiro","Cozinheiro","Limpador de Chaminés","Servente Doméstico","Fiandeiro","Cordoeiro",
                    "Trabalhador Agrícola","Lavadeira","Eunuco","Cesteiro","Controlador de Pragas","Escriba","Pastor de Animais",
                    "Role a profissão na tabela de PLEBEUS"]
'''
FAZER
ultimo
'''

profissaoPlebeu = ["Role a profissão na tabela de ESCRAVOS","Mendigo","Ferreiro","Taverneiro", "Estalajadeiro","Ceramicista", "Oleiro","Curtidor","Agricultor",
                   "Alfaiate","Sapateiro","Armeiro","Padeiro","Açougueiro","Cirireiro (Fazedor de Velas)","Ator","Ourives", "Joalheiro","Carpinteiro",
                   "Ajudante do Clero","Vendedor","Feirante","Mascate","Dono de Bordel","Capataz","Pescador","Caçador","Peleiro","Herbalista","Apotecario",
                   "Bibliotecário","Copista","Cervejeiro","Vinicultor","Tecelão","Membro do Baixo Clero",
                   "Bandido (Role para determinar: 1 a 6 - batedor de carteiras; 7 a 12 - salteador; 13 a 18 - matador; 19 a 24 – arrombador de casas; 25 a 30 – capanga)",
                   "Soldado (Role para determinar: 1 a 9 - miliciano; 10 a 15 - guarda; 16 a 21 – mercenário; 22 a 26 - soldado profissional; 27 a 30 - veterano de guerra)",
                   "Role a profissão na tabela de NOBRES"]
'''
FAZER
ultimos 3
'''    

profissaoNobre = ["Role a profissão na tabela de PLEBEUS",
                  "Artista (Role para determinar: 1 a 6 – escultor; 7 a 12 – pintor; 13 a 18 – músico; 19 a 24 – escritor; 25 a 30 – poeta)",
                  "Falcoeiro","Escudeiro","Fazendeiro Livre","Conselheiro Religioso","Conselheiro Real", "Magistrado","Coletor de Impostos","Comandante","General",
                  "Membro do Alto Clero","Sábio","Mercador","Capitão de Navio","Navegador","Jogador","Tutor","Escravista","Cavaleiro","Minerador (Dono de Mina)",
                  "Pecuarista (Grande Criador de Animais)","Senhor de Moinho ou Engenho","Embaixador, Arauto ou Diplomata","Astrônomo ou Astrólogo","Médico",
                  "Barbeiro","Cartógrafo","Aprendiz de Feiticeiro","Alquimista","Engenheiro","Guarda-Caça","Guarda Florestal","Lutier"]
'''
FAZER
0
1
'''

def set
amigoInimigo = ["UM INIMIGO","UM AMIGO","VOCÊ FEZ UM AMIGO e VOCÊ FEZ UM INIMIGO","2 de 1 e 1 do outro"]

amigo = ["Um antigo mentor","Um membro do clero","Um colega de armas","Um grande sábio","Um antigo amante", "Um mercador","Um ex-inimigo","Um pirata","Seu patrão",
         "Um empregado","Um filho de seu patrão","Um cavaleiro","Um amigo de infância","O chefe de uma quadrilha de salteadores","Um parente distante",
         "Alguém de uma raça odiada ou pouco comum","O dono da taverna","Um escravista","O ferreiro da cidade","Um mercenário","Um soldado","O capitão de um navio",
         "O chefe da guarda","Um general ou alto comandante militar","Um ladrão","O chefe da guilda de ladrões","Alguém com quem trabalhou","Um mago","Um nobre",
         "O rei"]

origemAmizade = ["Você salvou a vida dele","Ele salvou a sua vida","Ele é como um pai para você","Ele é como um filho para você",
                 "Ele é como se fosse seu irmão mais velho","Ele é como se fosse seu irmão mais novo","Você defendeu a honra dele","Ele defendeu sua honra",
                 "Suas famílias são amigas de longa data","Vocês simplesmente gostam um do outro.","Ele o defendeu em uma briga ou combate",
                 "Você o defendeu em uma briga.","Ele lhe emprestou dinheiro","Você lhe emprestou dinheiro","Vocês tiveram negócios juntos",
                 "Você admira as habilidades dele","Ele admira as suas habilidades","Vocês fizeram um pacto de sangue","Ele ajudou sua família",
                 "Você ajudou a família dele","Vocês trabalharam juntos no passado","Vocês tiveram o mesmo mestre",
                 "Você voluntariamente assumiu a culpa por algo que ele fez","Ele voluntariamente assumiu a culpa por algo que você fez",
                 "Vocês enfrentaram um perigos juntos","Vocês compartilham um segredo","Vocês possuem um forte interesse comum por alguma coisa",
                 "Vocês cresceram juntos","Vocês foram vizinhos","Vocês frequentavam o mesmo local (taverna, igreja, etc.)"]

inimigo = ["Um ex-amante","Um inimigo de infância","Alguém com quem trabalhou","Um membro do clero","Seu ex-patrão","Um filho de seu patrão","Um soldado",
           "Um ex-amigo","Um parente distante","Um ladrão","O ferreiro da cidade","O dono da taverna","O chefe da guarda","Um nobre","Um colega de armas",
           "Um antigo mentor","Um grande sábio","Um mercador","Um pirata","Um empregado","Um cavaleiro","O chefe de uma quadrilha de salteadores",
           "Alguém de uma raça odiada ou pouco comum","Um escravista","Um mercenário","O capitão de um navio","Um general ou alto comandante militar",
           "O chefe da guilda de ladrões","Um mago","O rei"]

causaInimizade = ["Você causou a morte de um ente querido dele (Role para determinar: 1 a 6 - aliado; 7 a 14 - amigo; 15 a 22 - parente; 23 a 30 - amante)",
                  "Ele causou a morte de um ente querido seu (Role para determinar: 1 a 6 - aliado; 7 a 14 - amigo; 15 a 22 - parente; 23 a 30 - amante)",
                  "Você deve dinheiro a ele","Você rejeitou uma proposta dele","Ele deve dinheiro a você","Ele rejeitou uma proposta sua","Você ofendeu sua honra",
                  "Ele o abandonou ou traiu","Ele ofendeu sua honra","Você o abandonou ou traiu","Você tem algo que deveria ter sido dado a ele",
                  "Você humilhou-o publicamente","Ele tem algo que deveria ter sido dado a você","Ele humilhou-o publicamente",
                  "Um amor em comum preferiu ficar com você","Ele fez você perder seu prestígio","Um amor em comum preferiu ficar com ele",
                  "Você fez ele perder seu prestígio","Ele causou-lhe uma deficiência física ou mental","Você causou-lhe uma deficiência física ou mental",
                  "Suas cidades são rivais tradicionais","Você enganou ele numa situação de negócios","Suas famílias são inimigas",
                  "Ele te enganou numa situação de negócios","Ele tem inveja de suas habilidades","Você frustrou os planos dele",
                  "Você tem inveja das habilidades dele","Ele frustrou seus planos","Vocês simplesmente não se gostam, sem maiores razões",
                  "Vocês foram enganados por um terceiro, mas culpam um ao outro"]

consequenciaInimizade = ["Vão se insultar em via pública","Vão jogar pedras um no outro","Você irá partir para cima do outro, que tentará fugir",
                         "Seu inimigo irá partir para cima de você, que tentará fugir","Ambos vão partir um para cima do outro","Um vai ignorar o outro",
                         "Um vai ignorar o outro, mas tentarão se apunhalar depois","Seu inimigo vai chamar um grupo para dar cabo de você",
                         "Seu inimigo irá propor um duelo até a morte","Você irá propor um duelo até a morte","Seu inimigo tentará ridicularizá-lo",
                         "Você tentará ridicularizá-lo","Seu inimigo fará uma armadilha (mortal ou não) para você",
                         "Você fará uma armadilha (mortal ou não) para seu inimigo","Seu inimigo tentará manchar sua honra",
                         "Você tentará manchar a honra de seu inimigo","Seu inimigo espalhará boatos e mentiras sobre você",
                         "Você espalhará boatos e mentiras sobre seu inimigo","Seu inimigo tentará culpá-lo de algum crime",
                         "Você tentará culpar seu inimigo de algum crime","Você tentará prejudicar os negócios ou carreira de seu inimigo",
                         "Seu inimigo tentará prejudicar seus negócios ou sua carreira",
                         "Seu inimigo tentará capturá-lo e mantê-lo prisioneiro, ou vendê-lo como escravo",
                         "Você tentará capturar seu inimigo e mantê-lo prisioneiro, ou vendê-lo como escravo","Você tentará aleijar ou mutilar seu inimigo",
                         "Seu inimigo tentará aleijar ou mutilar você","Você atacará os parentes, amigos ou aliados de seu inimigo",
                         "Seu inimigo atacará seus parentes, amigos ou aliados","Você tentará assassinar seu inimigo","Seu inimigo tentará assassiná-lo"]

def set
vidaAmorosa = ["Nunca se interessou ou nunca teve ninguém.","um CASO AMOROSO TRÁGICO OU PROBLEMÁTICO.",
               "Apenas romances passageiros e pouco dignos de nota","Apenas um, mas um caso feliz e duradouro."]

amorProblematico = ["A família do seu amor odeia você","Suas famílias são rivais ou inimigas declaradas","Sua família odeia seu amor","Vocês são de raças diferentes",
                    "Amigos de seu amor odeiam vocês","Vocês são de classes sociais distintas","Seus amigos odeiam seu amor",
                    "Você foi o responsável pela morte do seu amor, ou pelo menos acredita que sim",
                    "Família ou amigos do seu amor usarão de todos os meios para livrar-se de você",
                    "Seu amor caiu nas graças de outro com quem passou a se relacionar",
                    "Sua família ou amigos usarão de todos os meios para livrar-se de seu amor",
                    "Seu amor desapareceu misteriosamente","Você possui um rival amoroso","A relação simplesmente fracassou",
                    "Seu amor possui um rival amoroso","Algo (como um objetivo pessoal) se interpôs entre vocês",
                    "Magia os separa de alguma forma (ex: ela foi amaldiçoada a ser um falcão de dia e ele um lobo à noite)",
                    "Seu amor foi raptado","Brigas entre vocês são constantes","Seu amor enlouqueceu",
                    "Os amantes são rivais profissionais ou competem de alguma forma, de maneira extremamente acirrada",
                    "Seu amor foi aprisionado ou exilado","Você é extremamente ciumento","Seu amor morreu em um acidente","Seu amor é extremamente ciumento",
                    "Seu amor foi morto em uma luta","Você foi/é alvo da infidelidade de seu amor","Seu amor foi covardemente assassinado",
                    "Seu amor foi/é alvo de sua infidelidade","Seu amor cometeu suicídio"]

def set
tipoReliquea = ["Valiosa", "Mágica", "Especial", "Pessoal/imprestável"]

reliquia = ["Uma arma","Uma ferramenta","Uma peça de roupa","Uma gravura","Um livro","Um diário","Um pergaminho","Uma carta","Um instrumento musical","Uma jóia",
            "Um brinquedo ou jogo","Um chapéu","Uma moeda","Um lenço","Um cantil ou odre","Uma armadura, escudo ou elmo","Uma mochila ou bolsa","Uma gema",
            "Uma pequena escultura","Um símbolo sagrado ou outro objeto religioso","Uma caneca ou taça","Uma pena","Um mapa","Uma chave",
            "Uma pequena caixa, baú, ou porta-jóias","Uma máscara","Um pedaço de um animal ou monstro","Um pedaço de um humano ou humanóide",
            "Um item mágico menor. Talvez você desconheça sua natureza mágica.",
"Um poderoso item mágico inteligente, que vê grande futuro em você, mas o acha pouco experiente ou sábio para usar todo seu poder. Provavelmente nem desconfia disso."]

def set
naoGosta = ["Você não gosta de alguma raça (escolha qual)","Calor","Frio","Um animal comum (cavalos, cachorros,gatos, vacas, camelos, etc.)","Magia","Religião",
            "Você não gosta do odor de alguma coisa (escolha o quê)","Você não gosta do sabor de alguma bebida ou comida (escolha o quê)",
            "Grandes massas d’água","De combates","Crianças","Velhos","Falar em meio a multidões","Do gênero feminino em geral","Do gênero masculino em geral",
            "Lugares altos","Lugares apertados","Política","Sujeira","Mentiras","Do dia","Da noite","De estar sozinho","De estar sóbrio",
            "De algum veículo (escolha qual)","De alguma(s) palavra(s)","De expor o corpo","De não expor o corpo","De aglomerações de pessoas",
            "Role duas vezes nessa tabela"]

'''
FAZER
0
'''

def set
medo = ["Ficar velho e fraco","Ser abandonado por seus entes queridos","Viajar de barco","Um tipo de animal (escolha um)","Um tipo de monstro (escolha um)","Magia",
        "Cair em uma armadilha","Ser devorado vivo","Falhar com seus companheiros ou traí-los","Mortos-vivos","Ser enterrado vivo","Ficar pobre",
        "Perder um membro (escolha qual)","Perder um dos sentidos (escolha qual)","Afogar-se","Ser ignorado para sempre",
        "Perder a memória depois de tornar-se alguém de destaque em sua carreira","De altura","Da morte","Perder-se e acabar num lugar desconhecido",
        "Falhar com seu deus","Ser incapaz de manter-se honrado","Transformar-se em outra criatura ou monstro","Algum deus em específico (escolha um)","Enlouquecer",
        "Ser traído","Ser humilhado publicamente","Perder algo importante (escolha o que)","De um objeto: uma arma, bonecas de louça, crânios, etc (escolha um)",
        "Role duas vezes nessa tabela"]

def set
opiniaoDesconhecidos = ["Você não respeita ninguém que pertença a uma classe social que seja... (Role para determinar: 1 a 10 –inferior à sua própria; 11 a 20 – superior à sua própria; 21 a 30 – diferente da sua própria)",
                        "Neutra em relação a todos. Você espera conhecê-los para julgá-los.",
                        "Favorável em relação a todos. Você gosta de todo mundo antes mesmo de conhecê-los.",
                        "Desfavorável em relação a todos. Você odeia todo mundo antes mesmo de conhecê-los.",
                        "As pessoas são ferramentas que devem ser usadas em prol de seus objetivos","Todas as pessoas são indivíduos de valor",
                        "As pessoas são obstáculos a serem destruídos se atrapalharem seu caminho","Ninguém é confiável, por isso você deve se virar sozinho",
                        "A maioria das pessoas são incompetentes e inúteis, ainda que não sejam pessoas ruins",
                        "Os membros do sexo oposto em geral são indignos de confiança",
                        "Os membros do seu próprio sexo em geral são indignos de confiança",
                        "Os membros do sexo oposto devem ser usados e descartados",
                        "Os membros do seu próprio sexo são apenas ferramentas descartáveis a serem usadas em seus planos",
                        "Você odeia todos os membros de seu próprio sexo","Você odeia todos os membros do sexo oposto",
                        "Os membros do sexo oposto são incompetentes e inúteis, ainda que não sejam pessoas ruins",
                        "Os membros do seu próprio sexo são incompetentes e inúteis, ainda que não sejam pessoas ruins",
                        "As pessoas são como pedras brutas a serem lapidadas por você","Pessoas com pensamentos diferentes do seu não merecem sua atenção",
                        "Pessoas com pensamentos diferentes do seu tem a sua atenção, pois você espera que elas lhe ensinem algo",
                        "Pessoas com pensamentos diferentes do seu recebem sua atenção, mas você não os leva a sério",
"Você é extremamente tolerante, não está nem aí para ninguém, o que pensam sobre você, o que você pensa sobre elas, contanto que você esteja seguro, tudo sempre estará bem",
                        "Os membros de sua própria raça são incompetentes e inúteis, ainda que não sejam pessoas ruins",
                        "Os membros das outras raças são incompetentes e inúteis, ainda que não sejam pessoas ruins",
                        "Os membros de outras raças são apenas ferramentas descartáveis a serem usadas em seus planos",
                        "Os membros de sua própria raça são apenas ferramentas descartáveis a serem usadas em seus planos",
                        "Você odeia todos os membros de sua própria raça","Você odeia todos os membros de outras raças que não a sua",
                        "Os membros de outras raças em geral são indignos de confiança",
                        "Os membros de sua própria raça em geral são indignos de confiança, mas não os de outras raças"]

def set
principalArrependimento = ["Você não se arrepende de nada. Nunca. Talvez você seja egoísta e acredite que está sempre correto.",
                           "Você se arrepende de ter traído seu (a) companheiro (a) com outra pessoa",
"Você se arrepende de ter bebido demais na taverna, ter apagado e acordado no estábulo, nu e sem lembrar do que aconteceu; isso o tornou motivo de boatos e chacotas na cidade",
                           "Você se arrepende de ter confessado seu amor a quem, faz pouco caso e o ignora completamente",
                           "Você se arrepende de ter nascido!","Você se arrepende de nunca tomar as decisões urgentes na velocidade em que precisam ser tomadas",
                           "Você se arrepende de ter confiado seu tesouro a um ex-colega de grupo, que fugiu com o dinheiro",
                           "Você se arrepende de ter contraído AQUELA dívida com um dos comerciantes mais ricos da cidade",
                           "Você se arrepende de estar em dívida com uma perigosa guilda, e convive com o temor de ser morto",
                           "Você sempre se arrepende de ter comido mais um pouco da última vez...",
                           "Você se arrepende de não ter sido capaz de impedir a morte de um companheiro ou ente querido",
                           "Você se arrepende de não ter seguido outra carreira","Você se arrepende de ter dito que iria ajudar",
"Você se arrepende daquela vez na qual uma anã barbuda lhe ofereceu uma bebida e então você não se lembra muito bem do que aconteceu em seguida, ou diz não se lembrar",
                           "Você se arrepende de ter negado ajuda a alguém","Você se arrepende de ter tirado a vida de alguém",
                           "Você se arrepende de ter confiado em alguém","Você se arrepende de ter adquirido algum bem ou objeto (decida com o mestre o que é)",
                           "Você se arrepende de ter feito algo errado/vergonhoso/danoso graças à bebida (ou graças a um vício)",
                           "Você se arrepende por ter contraído um voto ou juramento a uma pessoa ou organização",
                           "Você se arrepende de ter quebrado um voto ou juramento a uma pessoa ou organização",
                           "Você se arrepende de ter assinado um contrato anos atrás (determine com o mestre do que se trata)",
                           "Você se arrepende de ter subido na vida pisando nos outros","Você se arrepende de ter abandonado sua família",
                           "Você se arrepende de ter constituído uma família","Você se arrepende amargamente das brigas que teve com seus pais",
                           "Você se arrepende de não ter pedido perdão a alguém que amava, a quem magoou tremendamente",
                           "Você se arrepende de não ser mais extrovertido","Você se arrepende de ter gostado de quem não deveria, uma vez na vida...",
"Você se arrepende de ter feito um pacto de sua alma com uma entidade demoníaca; após ter obtido seu benefício (defina-o com o mestre), convive com o drama da danação eterna quando morrer"
                           ]

def set
manias = ["Você pratica toda noite (ou dia, ou manhã) para melhorar sua habilidade em alguma coisa","Você enrola seu cabelo ou barba enquanto pensa",
          "Você coleciona troféus de inimigos vencidos","Você mantém um diário onde registra seu dia e faz anotações constantes",
          "Você sempre entra nos locais com o pé direito","Você constantemente afia sua arma",
          "Você abre ou tenta abrir qualquer objeto fechado para ver o que tem dentro","Você bate três vezes em madeira toda vez que alguém diz algo horrível",
          "Você sempre erra o nome das pessoas, ou as chama por apelidos ou por sua profissão",
          "Você é extremamente vaidoso e preocupa-se muito com sua aparência; narcisista",
          "Você faz uma postura ou gesto específico com sua arma antes de entrar em combate","Você vive fazendo trocadilhos",
          "Você repete uma palavra ou uma expressão (“digo”, “né”, “assim”, “ahn”, “por Crom”, etc.)","Você possui um grito de guerra extravagante",
          "Você costuma cuspir o tempo todo","Você gagueja quando encarado(a) pelo sexo oposto (ou mesmo sexo, dependendo de sua preferência)",
          "Você cantarola ou assovia o tempo inteiro","Você costuma empregar expressões altamente heréticas (ex:“Pela sagrada barba fedorenta de Netuno!”)",
          "Você sempre chega adiantado em seus compromissos","Você sempre se atrasa de propósito","Você costuma carregar dois de cada item que tiver por precaução",
          "Você veste-se inteiramente de uma mesma cor",
          "Você costuma dar um nome extravagante para todos os seus objetos importantes, como suas armas e armadura, e talvez até para você mesmo",
          "Você fica dizendo: “Ok! Ok! Perfeito!”, ou outra exclamação de concordância, mas fora isso passa a maior parte do tempo calado",
          "Você tem um tique nervoso (rói unhas, pisca seu olhos inúmeras vezes, força a vista, etc)",
          "Você erra alguma letra (troca r por l, ou r por g)",
          "Você é supersticioso e adquire tudo quanto é tipo de amuleto e badulaques para espantar a má sorte",
          "Você costuma ter vários casos com homens e/ou mulheres em cada cidade ao mesmo tempo, o que pode render situações complicadas e/ou pitorescas",
          "Você tende a ser rude e grosseiro com todos, e se porta de forma inadequada em eventos sociais",
          "Você coleciona alguma coisa: adagas, moedas, anéis, borboletas, mapas, gemas, etc. (escolha o quê)"]

def set
motivacaoAventureira = ["Você é mercenário trabalha por dinheiro","Você procura reencontrar um amor perdido",
                        "Você foi salvo por um aventureiro quando criança e deseja se tornar um",
                        "Você nem sabe porquê, as aventuras simplesmente cruzam seu caminho o tempo todo",
                        "Você possui motivos altruístas e quer ajudar os necessitados", "Você almeja fama e glória, e ter seus feitos cantados pelos bardos",
                        "Você acredita que tem um destino a cumprir","Você pretende atrair a atenção de uma guilda ou pessoa influente",
                        "Você precisa/quer recuperar uma herança perdida, seja porque foi roubada, porque o dono original também desapareceu, etc.",
                        "Você perdeu uma aposta num jogo de bar e agora está fadado a anos de aventuras ao lado do ganhador dessa aposta",
                        "Você pretende limpar o seu nome ou de sua família realizando grandes feitos",
                        "Você pretender gravar seu nome na história e ser lembrado por algo importante","Você gosta de emoções fortes",
                        "Você pretende alcansar o trono por esforço próprio","Você deseja tornar-se um herói",
                        "Você busca um poder/magia/técnica/conhecimento/habilidade (escolha um) que deseja muito conseguir",
                        "Você está buscando tesouros perdidos","Essas aventuras me perseguem! Por mais que eu queira ficar longe!","Você quer conhecer o mundo",
                        "Você busca um artefato de grande poder","Você está em uma missão sagrada","Você busca uma criatura lendária",
                        "Você deseja desvendar os mistérios de uma civilização perdida",
                        "Você pretende ser o indivíduo mais bem sucedido de todos em seu campo de atuação.","Você está numa busca por vingança",
                        "Você busca a imortalidade","Seu pai foi um aventureiro e transmitiu o legado à você","Você quer tornar-se uma divindade",
                        "Você foi colocado nessa vida por outra pessoa, e não sabia exatamente no que estava se metendo",
                        "Você nem se dá conta de que está se aventurando, talvez encare tudo como acontecimentos normais do dia-a-dia."]

def set
feitoNotavel = ["Ajudei a expulsar algumas criaturas de minha cidade e mandá-las de volta para seu covil” (escolha uma criatura",
                "Você é uma pessoa de importância em sua cidade natal. Role três vezes nessa tabela e fique com todos os resultados.",
                "Role duas vezes nessa lista e fique com os dois resultados.",
                "Entrei em uma expedição rumo a uma cripta local com um grupo de aventureiros uma vez. Tudo bem que foi só pra carregar tocha, mas bem...",
                "Certa vez servi como batedor a um grupo que planejava atacar um povoado.",
                "Recebi uma recompensa para ir até um lugar e matar um homem para o meu contratante.",
                "Certo dia, voltando de uma viajem, encontrei uma criança raptada por goblins e a trouxe de volta.",
                "Afugentei um monstro da minha vila junto a uma multidão enfurecida com tochas e garfos de feno.",
                "Certa vez me uni a um grupo de aventureiros como guia e consegui sobreviver a um combate contra bandoleiros me escondendo debaixo da carroça.",
"Uma vez, um líder de nossa aldeia/cidade/vila estava possuído por demônios. Então auxiliei os clérigos locais e um pequeno grupo de aventureiros a conseguir salvá-lo.",
                "Meus pais foram escravizados, quando eu era mais jovem. Alguns anos depois, consegui localizá-los e fugir com eles para longe dos captores.",
                "Encontrei um famoso bandido morto em um beco. Um comerciante passou por ali e achou que eu o tinha matado. Ao menos ele tinha bolsos fartos...",
                "Eu lembro da vez em que aquelas pragas gigantes infestaram o velho moinho. Eu e mais uns camponeses nos armamos e fomos até lá desinfestar o local!",
                "Dois grupos, de mercadores e fazendeiros disputavam o governo na minha cidade natal, e uma das lideranças foi morta. Adivinhe quem foi o responsável?",
                "Certa vez acompanhei uns homens santos em uma peregrinação para espalhar a fé e combater os infiéis.",
                "Certa vez coletei alguns ingredientes estranhos a pedido de um mago. Acho que para uma poção ou feito mágico qualquer.",
                "Presenciei um crime e ajudei o reino entregando informações importantes para os guardas reais.",
                "Ah, eu já invadi um templo/torre/mansão/ castelo e roubei uma jóia que estava lá. Pena que já gastei todo o dinheiro!",
                "Escapei de um covil de kobolds após ficar 5 dias preso.","Fui escudeiro de um cavaleiro que partiu para terras distantes.",
"Certa vez fui preso no calabouço de um mago sem motivo algum, mas consegui fugir depois de um homem chutar a porta da minha cela e me mandar correr pra longe.",
"Um bando de orcs destruiu uma vila em que eu morei. Eu lutei com um deles e consegui escapar juntamente com um pequeno grupo de moradores, antes que eles nos capturassem.",
                "Derrotei um mago sem usar armas.","Escapei de um comboio escravagista.",
                "Estava explorando a floresta e fiquei preso em areia movediça por 2 dias, e me alimentei de uma serpente que alcancei com um galho.",
        "Fui assistente de um mago e vi quando ele trouxe à vida uma criatura feita de pedaços de corpos. Sorte que eu fugi dali antes que fosse devorado também.",
                "Ganhei um concurso de quem bebia mais. Um dos participantes era um anão robusto.", "Liderei a contenção de um incêndio causado por goblinóides.",
                "Já escoltei uma caravana até a cidade vizinha como parte do grupo de segurança.",
                "Ajudei uns caras que exploraram as antigas ruínas carregando uns sacos. Nunca vi tanto ouro na minha vida!"]

def set
criaturas = ["Orcs","Bugbears","Trogloditas","Goblins","Anões","Homens Lagarto","Kobolds","Elfos","Aranhas Gigantes","Trolls","Elfos Negros","Tirano Ocular",
             "Ogros","Banshees","Wargs","Shoggoths","Crias Estelares de Cthulhu","Sátiros","Lobisomens","Doppelgangers","Demônios","Unicórnios","Nagas","Vampiros",
             "Zumbis","Inumanos","Gigantes","Hobgoblins","Esqueletos","Dragões"]

def set
motivoOdioCriatura = ["Uma delas roubou todo o seu tesouro pessoal","Uma delas sequestrou sua família","Uma delas matou um amigo ou aliado seu",
                      "Uma delas o seduziu mudando de forma","Uma delas matou um ente querido seu(esposa, filho, pai, mãe...)",
                      "Uma delas destruiu sua propriedade ou a de sua família","Uma delas o chantageou por conhecer um vergonhoso segredo de seu passado",
                      "Uma pessoa foi devorada por esse tipo de criatura na sua frente!",
                      "Uma delas o induziu a participar de uma missão suicida e você percebeu isso tarde demais",
                      "Você encara essas criaturas como aberrações da natureza que não deveriam existir",
                      "Você tem sonhos recorrentes em que estas criaturas lhe ferem de alguma maneira",
                      "Você entende essas criaturas como ofensivas à sua fé ou ao seu deus de alguma maneira",
                      "Você perdeu para uma destas criaturas numa batalha, de forma vergonhosa e pública",
                      "O povo do local onde você nasceu nutre uma inimizade ancestral contra essas criaturas",
                      "Uma delas detém poder suficiente para dar-lhe ordens (e você deve obedecer)",
                      "O ódio contra estas criaturas é apenas uma forma de descontar suas frustrações de outras origens",
                      "Você acredita que essas criaturas vieram de outro plano ou mundo para invadir este mundo e dominá-lo",
                      "Você foi agredido sem razão aparente por uma dessas criaturas, e foi deixado para morrer, mas para o azar delas, você não morreu",
                      "Alguém lhe ensinou que essas criaturas deveriam ser odiadas, e você simplesmente segue essa filosofia sem nem mesmo pensar a respeito",
                "Uma delas espalhou impropérios a seu respeito nas vilas por onde passou; como resultado, você adquiriu infâmia e quase ninguém confia missões a você",
"Uma vidente previu que você seria morto por uma dessas criaturas, por via das dúvidas você as elimina antes que elas tenham a oportunidade de realizar a visão",
"Quem lhe ensinou os caminhos da vida de aventureiro odiava essa criatura por alguma razão, e passou esse ódio para você, mesmo que você não saiba o porquê",
"Uma delas convenceu um amigo ou aliado importante de que você foi o responsável por algum gesto bárbaro, criminoso, e essa pessoa tornou-se sua inimiga hoje",
"Você acredita que essas criaturas são irremediavelmente malignas, possivelmente mais malignas do que quaisquer outras, e algo tão maligno obviamente precisa ser destruído",
"Você descobriu que uma delas cruelmente mudou temporariamente de forma para ter um filho seu (e hoje você persegue esse filho abominável, que vem trazendo horror, morte e destruição ao reino)",
"Uma dessas criaturas chamou você de “filho de um unicórnio” na frente de dezenas de aventureiros embriagados na taverna mais fedorenta do cais da cidade, e você virou alvo de chacota eterna sempre que vai a essa cidade",
"Você não tem uma razão verdadeira para odiar essa criatura, mas por alguma razão, outros atribuem que você é um caçador profissional desse tipo de criatura; negar essa fama que lhe foi atribuída significaria adquirir infâmia perante seus próximos",
"Odiar? Quem disse que você a odeia? Tudo é uma grande farsa planejada por você com o único propósito de ganhar notoriedade e logicamente fama e dinheiro.",
                      "Nenhuma razão em especial, você apenas acha essas criaturas repugnantes."]


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ROLAGENS xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#introvertido?
'''
Fazer dps
'''

#cor da pele

#cor dos olhos
selectedOlhos = rolarDados.select(corOlhos)
#cor do cabelo
selectedCabeles = rolarDados.select(corCabelos)

'''
Fazer Deficiencia e doença
'''
#probDeficiencia = rolarDados.rolar(100)
#probDoenca = rolarDados.rolar(100) 8%
#deficiencia
#doença


#tipo de cabelo
selectedTypeHair = rolarDados.select(tiposCabelo)

'''
Fazer tipo nascimento
'''
#tipo de nascimento
selectedTypeBirth = "mundano"#rolarDados.select()

#nascimento
selectedNascimento = rolarDados.select(nascimentoEspecial)
if selectedTypeBirth == "mundano"
    selectedNascimento = rolarDados.select(nascimentoMundano)
#pais
selectedSeusPais = rolarDados.select(seusPais)

'''
Fazer Irmaos
'''
# Tem irmãos?
#selectedNascimento = rolarDados.select()
#quantos

#Sorte/Tragedia
selectedSorteTragedia = rolarDados.rolar(4)
selectedSorte = False
selectedTragedia = False
if selectedSorteTragedia == 1:
    selectedSorte = rolarDados.select(sorte)
else if selectedSorteTragedia == 2:
    selectedTragedia = rolarDados.select(tragedia)
else if selectedSorteTragedia == 3:
    selectedSorte = rolarDados.select(sorte)
    selectedTragedia = rolarDados.select(tragedia)
    
#Status Social Inicial
selectedStatus = rolarDados.select(statusInicial)

#Profissão
if selectedStatus == "Escravo":
    selectedProfissao = rolarDados.select(profissaoEscravo)
else if selectedStatus == "Plebeu":
    selectedProfissao = rolarDados.select(profissaoPlebeu)
else if selectedStatus == "Nobre":
    selectedProfissao = rolarDados.select(profissaoNoobre)
    
#Amigos e inimigos
selectedFriendsAndEnemies = rolarDados.rolar(4)
if selectedFriendsAndEnemies == 0:
    selectedInimigo = rolarDados.select(inimigo)
    selectedCausaInimizade = rolarDados.select(causaInimizade)
    selecttedConsequenciaInimizade = rolarDados.selecte(consequenciaInimizade)
else if selectedFriendsAndEnemies == 1:
    selectedAmigo = rolarDados.select(amigo)
    selectedOrigemAmizade = rolarDados.select(origemAmizade)
else if selectedFriendsAndEnemies == 2:
    selectedAmigo = rolarDados.select(amigo)
    selectedOrigemAmizade = rolarDados.select(origemAmizade)
    
    selectedInimigo = rolarDados.select(inimigo)
    selectedCausaInimizade = rolarDados.select(causaInimizade)
    selecttedConsequenciaInimizade = rolarDados.selecte(consequenciaInimizade)
else:
    qtdAmigos = rolarDados.rolar(2)

    if  qtdAmigos == 0:
        selectedAmigo = rolarDados.select(amigo)
        selectedOrigemAmizade = rolarDados.select(origemAmizade)

        selectedAmigo2 = rolarDados.select(amigo)
        selectedOrigemAmizade2 = rolarDados.select(origemAmizade)

        selectedInimigo = rolarDados.select(inimigo)
        selectedCausaInimizade = rolarDados.select(causaInimizade)
        selecttedConsequenciaInimizade = rolarDados.selecte(consequenciaInimizade)
        qtdAmigos = 2
    else:
        selectedAmigo = rolarDados.select(amigo)
        selectedOrigemAmizade = rolarDados.select(origemAmizade)

        selectedInimigo = rolarDados.select(inimigo)
        selectedCausaInimizade = rolarDados.select(causaInimizade)
        selecttedConsequenciaInimizade = rolarDados.selecte(consequenciaInimizade)

        selectedInimigo2 = rolarDados.select(inimigo)
        selectedCausaInimizade2 = rolarDados.select(causaInimizade)
        selecttedConsequenciaInimizade2 = rolarDados.selecte(consequenciaInimizade)
        qtdInimigos = 2
          
#Vida amorosa
selectedVidaAmorosa = rolarDados.rolar(4)
 
if selectedSorteTragedia == 1:
    selectedVidaAmorosa = rolarDados.select(amorProblematico)
else:
    selectedVidaAmorosa = vidaAmorosa[selectedVidaAmorosa]
'''
FAZER Reliqueas DPS

#tem reliquia?
#reliquia
selectedNascimento = rolarDados.select()
'''
#algo q n goste
selectedNaoGosta = rolarDados.select(naoGosta)
#Medo
selectedMedo = rolarDados.select(medo)
#Opinião quanto a desconhecidos
selectedOpiniaoDesconhecidos = rolarDados.select(opiniaoDesconhecidos)


#Tem arrependimento?
selectedArrependimento = rolarDados.select(principalArrependimento)
#tem mania?
#O que fez se aventurar?
selectedMotivacao = rolarDados.select(motivacaoAventureira)
#Feito notável
selectedFeito = rolarDados.select(feitoNotavel)

#odeia quantas criaturas
qtdCriaturas = rolarDados.rolar(4)

if qtdCriaturas == 1:
    selectedCriatura = rolarDados.select(criaturas)
    selectedMotivoCriatura = rolarDados.select(motivoOdioCriatura)
    
else if qtdCriaturas == 2:
    selectedCriatura = rolarDados.select(criaturas)
    selectedMotivoCriatura = rolarDados.select(motivoOdioCriatura)

    selectedCriatura2 = rolarDados.select(criaturas)
    selectedMotivoCriatura2 = rolarDados.select(motivoOdioCriatura)
    
else if qtdCriaturas == 3:
    selectedCriatura = rolarDados.select(criaturas)
    selectedMotivoCriatura = rolarDados.select(motivoOdioCriatura)

    selectedCriatura2 = rolarDados.select(criaturas)
    selectedMotivoCriatura2 = rolarDados.select(motivoOdioCriatura)

    selectedCriatura3 = rolarDados.select(criaturas)
    selectedMotivoCriatura3 = rolarDados.select(motivoOdioCriatura)

