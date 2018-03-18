class Personagem:
    '''
    #################################################################### ATRIBUTOS ####################################################################
    classe
    genero
    sexualidade
    raca
    personalidade
    introvertido
    pele
    corOlhos
    corCabelos
    tipoCabelos
    nascimento
    pais
    irmaos
    sorteTragedia
    statusInicial
    profissao
    amigosInimigos
    vidaAmorosa
    naoGosta
    medo
    opiniaoDesconhecidos
    arrependimento
    mania
    motivacaoAventureira
    feitoNotavel
    criaturasOdiadas
    deficiencia
    doenteCronico
    reliquia
    '''

######################################################################### SETS #######################################################################
    #def sets():
        
    def setClasse(self, classe):
        self.classe = classe
        
    def setGenero(self, genero):
        self.genero = genero
        
    def setSexualidade(self, sexualidade):
        self.sexualidade = sexualidade
        
    def setRaca(self, raca):
        self.raca = raca
        
    def setPersonalidade(self, personalidade):
        self.personalidade = personalidade
        
    def setIntrovertido(self, introvertido):
        self.introvertido = introvertido
        
    def setPele(self, pele):
        self.pele = pele
        
    def setCorOlhos(self, corOlhos):
        self.corOlhos = corOlhos
        
    def setCorCabelos(self, corCabelos):
        self.corCabelos = corCabelos
        
    def setTipoCabelos(self, tipoCabelos):
        self.tiposCabelos = tiposCabelos
        
    def setNascimento(self, nascimento):
        self.nascimento = nascimento
        
    def setPais(self, pais):
        self.pais = pais
        
    def setIrmaos(self, irmaos):
        self.irmaos = irmaos
        
    def setSorteTragedia(self, sorteTragedia):
        self.sorteTragedia = sorteTragedia
        
    def setStatusInicial(self, statusInicial):
        self.statusInicial = statusInicial
        
    def setProfissao(self, profissao):
        self.profissao = profissao
        
    def setAmigosInimigos(self, amigosInimigos):
        self.amigosInimigos = amigosInimigos
        
    def setVidaAmorosa(self, vidaAmorosa):
        self.vidaAmorosa = vidaAmorosa
        
    def setNaoGosta(self, naoGosta):
        self.naoGosta = naoGosta
        
    def setMedo(self, medo):
        self.medo = medo
        
    def setOpiniaoDesconhecidos(self, opiniaoDesconhecidos):
        self.opiniaoDesconhecidos = opiniaoDesconhecidos
        
    def setArrependimento(self, arrependimento):
        self.arrependimento = arrependimento
        
    def setMania(self, mania):
        self.mania = mania
        
    def setMotivacaoAventureira(self, motivacaoAventureira):
        self.motivacaoAventureira = motivacaoAventureira
        
    def setFeitoNotavel(self, feitoNotavel):
        self.feitoNotavel = feitoNotavel
        
    def setCriaturasOdiadas(self, criaturasOdiadas):
        self.criaturasOdiadas = criaturasOdiadas
        
    def setDeficiencia(self, deficiencia):
        self.deficiencia = deficiencia
        
    def setDoenteCronico(self, doenteCronico):
        self.doenteCronico =doenteCronico
        
    def setReliquia(self, reliquia):
        self.reliquia = reliquia


######################################################################### Construtor #######################################################################
    def __init__(self, classe, genero, sexualidade, raca, personalidade, introvertido, pele, corOlhos, corCabelos, tipoCabelos, nascimento, pais, irmaos,
                 sorteTragedia, statusInicial, profissao, amigosInimigos, vidaAmorosa, naoGosta, medo, opiniaoDesconhecidos, arrependimento, mania,
                 motivacaoAventureira, feitoNotavel, criaturasOdiadas, deficiencia, doenteCronico, reliquia):

        self.classe = classe
        self.genero = genero
        self.sexualidade = sexualidade
        self.raca = raca
        self.personalidade = personalidade
        self.introvertido = introvertido
        self.pele = pele
        self.corOlhos = corOlhos
        self.corCabelos = corCabelos
        self.tipoCabelos = tipoCabelos
        self.nascimento = nascimento
        self.pais = pais
        self.irmaos = irmaos
        self.sorteTragedia = sorteTragedia
        self.statusInicial = statusInicial
        self.profissao = profissao
        self.amigosInimigos = amigosInimigos
        self.vidaAmorosa = vidaAmorosa
        self.naoGosta = naoGosta
        self.medo = medo
        self.opiniaoDesconhecidos = opiniaoDesconhecidos
        self.arrependimento = arrependimento
        self.mania = mania
        self.motivacaoAventureira = motivacaoAventureira
        self.feitoNotavel = feitoNotavel
        self.criaturasOdiadas = criaturasOdiadas
        self.deficiencia = deficiencia
        self.doenteCronico = doenteCronico
        self.reliquia = reliquia
        
        ''' ESSA CARALHA NAO FUNCIONOU, FICA FALANDO QUE set* não esta definido
        setClasse(classe)
        setGenero(genero)
        setSexualidade(sexualidade)
        setRaca(raca)
        setPersonalidade(personalidade)
        setIntrovertido(introvertido)
        setPele(pele)
        setCorOlhos(corOlhos)
        setCorCabelos(corCabelos)
        setTipoCabelos(tipoCabelos)
        setNascimento(nascimento)
        setPais(pais)
        setIrmaos(irmaos)
        setSorteTragedia(sorteTragedia)
        setStatusInicial(statusInicial)
        setProfissao(profissao)
        setAmigosInimigos(amigosInimigos)
        setVidaAmorosa(vidaAmorosa)
        setNaoGosta(naoGosta)
        setMedo(medo)
        setOpiniaoDesconhecidos(opiniaoDesconhecidos)
        setArrependimento(arrependimento)
        setMania(mania)
        setMotivacaoAventureira(motivacaoAventureira)
        setFeitoNotavel(feitoNotavel)
        setCriaturasOdiadas(criaturasOdiadas)
        setDeficiencia(deficiencia)
        setDoenteCronico(doenteCronico)
        setReliquia(reliquia)
        '''

######################################################################### GETS #######################################################################
    def getClasse(self):
        return self.classe
    
    def getGenero(self):
        return self.genero
    
    def getSexualidade(self):
        return self.sexualidade
    
    def getRaca(self, raca):
        return self.raca
    
    def getPersonalidade(self):
        return self.personalidade
    
    def getIntrovertido(self):
        return self.introvertido
    
    def getPele(self):
        return self.pele
    
    def getCorOlhos(self):
        return self.corOlhos
    
    def getCorCabelos(self):
        return self.corCabelos
    
    def getTipoCabelos(self):
        return self.tiposCabelos
    
    def getNascimento(self):
        return self.nascimento
    
    def getPais(self):
        return self.pais
    
    def getIrmaos(self):
        return self.irmaos
    
    def getSorteTragedia(self):
        return self.sorteTragedia
    
    def getStatusInicial(self):
        return self.statusInicial
    
    def getProfissao(self):
        return self.profissao
    
    def getAmigosInimigos(self):
        return self.amigosInimigos
    
    def getVidaAmorosa(self):
        return self.vidaAmorosa
    
    def getNaoGosta(self):
        return self.naoGosta
    
    def getMedo(self):
        return self.medo
    
    def getOpiniaoDesconhecidos(self):
        return self.opiniaoDesconhecidos
    
    def getArrependimento(self):
        return self.arrependimento
    
    def getMania(self):
        return self.mania
    
    def getMotivacaoAventureira(self):
        return self.motivacaoAventureira
    
    def getFeitoNotavel(self):
        return self.feitoNotavel
    
    def getCriaturasOdiadas(self):
        return self.criaturasOdiadas
    
    def getDeficiencia(self):
        return self.deficiencia
    
    def getDoenteCronico(self):
        return self.doenteCronico
                         
    def getReliquia(self):
        return self.reliquia

######################################################################### Outros Métodos ######################################################################

    def toString(self):#Estão TODOS COM STR() PQ JA DEU MUITO BUG HJ TO DE CABEÇA CHEIA PARA MECHER COM ISSO AGORA!!!
        personagem = "Classe: %s\nGênero: %s\nSexualidade: %s\nRaça: %s\nPersonalidade: %s\nIntrovertido: %s\nPele: %s\nCor dos olhos: %s\nCor do Cabelo: %s\nTipo de cabelo: %s\nNascimento: %s\nPais: %s\nIrmãos: %s\nSorte ou Tragédia: %s\nStatus Inicial: %s\nProfissão: %s\nAmigos e Inimigos: %s\nVida Amorosa: %s\nNão gosta de: %s\nMedo: %s\nOpinião sobre desconhecidos: %s\nArrependimento: %s\nMania: %s\nMotivação Aventureira: %s\nPrimeiro Feito notável: %s\nCriaturas Odiadas: %s\nPortador de deficiência: %s\nDoente Crônico: %s\nReliquia: %s\n" % (
            str(self.classe), str(self.genero),
        str(self.sexualidade),str(self.raca), str(self.personalidade), str(self.introvertido), str(self.pele), str(self.corOlhos), str(self.corCabelos),
        str(self.tipoCabelos), str(self.nascimento), str(self.pais), str(self.irmaos), str(self.sorteTragedia), str(self.statusInicial), str(self.profissao),
        str(self.amigosInimigos), str(self.vidaAmorosa), str(self.naoGosta), str(self.medo), str(self.opiniaoDesconhecidos), str(self.arrependimento),
        str(self.mania), str(self.motivacaoAventureira), str(self.feitoNotavel), str(self.criaturasOdiadas),str(self.deficiencia), str(self.doenteCronico),
        str(self.reliquia))
        
        return personagem
