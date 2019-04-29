from random import choice
from rollDices import RollDices

class Character:

    # ############################## CLASS VARIABLES ##########################
    dice = RollDices()

    classes = ['bardo', 'druida', 'espadachim', 'feiticeiro', 'barbaro', 'xamã',
               'ladino', 'paladino', 'patrulheiro', 'rúnico', 'sacerdote']

    generos = ['homem', 'mulher']

    sexualidade = ['homo', 'bi', 'a', 'pan', 'demi']

    racas = [
        'aesir', 'anã', 'elfica', 'faen', 'fauno', 'fira', 'humana', 'ratling',
        'juban', 'levent', 'mahok', 'tailox', 'aquila', 'drow', 'minotauro',
        'reptiliano', 'naga', 'bearos', 'centauro', 'draconiano/a', 'náiade',
        'equiceph', 'genasi', 'groton', 'globin', 'halfling', 'lige', 'orc']

    tiposPsicologicos = [
        'reformador(a)', 'sedutor(a)', 'competidor(a)', 'dominador(a)',
        'individualista', 'investigador(a)', 'diplomata', 'controlador(a)',
        'entusiasta']

    corPele = [
        'Azeviche', 'Negra', 'Mulata', 'Parda', 'Bronzeada', 'Sardenta',
        'Branca', 'Branca pálida', 'Amarela', 'Trigueira', 'Vermelha', 'Amarela',
        'Negra', 'Branca', 'Branca pálida', 'Trigueira', 'Negra', 'Vermelha',
        'Bronzeada', 'Branca', 'Mulata', 'Parda', 'Azeviche', 'Branca', 'Negra',
        'Albino', 'Cicatrizes', 'Tatuagens', 'Marca de Nascença', 'Pele manchada']

    corOlhos = [
        'Negro', 'Castanho', 'Castanho claro', 'Castanho escuro', 'Cinzento',
        'Castanho esverdeado', 'Verde', 'Verde esmeralda', 'Cinza prateado',
        'Verde acinzentado', 'Azul claro', 'Azul escuro', 'mel', 'Violeta',
        'Cor de avelã', 'Azul acinzentado', 'Vermelho(albino)', 'Dourado',
        'Âmbar', 'Azul', 'Castanho', 'Castanho claro', 'Castanho escuro',
        'Verde oliva', 'Caramelo', 'Olheiras', 'Esclera com veios de sangue',
        'Esclera amarelada', 'Caolho', 'Um olho de cada cor']

    corCabelos = [
        'Preto', 'Castanho escuro', 'Castanho', 'Castanho claro',
        'Castanho avermelhado', 'Vermelho', 'Ruivo', 'Acobreado',
        'Louro arruivado', 'Louro-platinado', 'Louro claro', 'Louro',
        'Louro acinzentado', 'Louro escuro', 'Louro dourado',
        'Castanho claro', 'Castanho', 'Castanho escuro', 'Preto',
        'Louro escuro', 'Louro', 'Louro claro', 'Cinzento',
        'Branco prateado', 'Branco', 'Têmporas grisalhas','Grisalho',
        'Calvo', 'Careca']

    tiposCabelo = [
        'Cabelos longos', 'Cabelos curtos', 'Cabelo volumoso',
        'Cabelo ralo', 'Cabelo raspado', 'Cabelo liso',
        'Cabelo cacheado', 'Cabelo crespo', 'Costeletas longas',
        'Suíças proeminentes', 'Tranças nos cabelos', 'Dreadlocks',
        'Moicano longo', 'Moicano curto', 'Bigode curto',
        'Bigode longo', 'Bigode fino', 'Cavanhaque sem bigode',
        'Cavanhaque e bigode', 'Tranças no cavanhaque',
        'Barba por fazer', 'Barba rala', 'Barba curta',
        'Barba crespa', 'Barba longa', 'Tranças na barba',
        'Sobrancelhas finas', 'Sobrancelhas grossas',
        'Sobrancelhas unidas', 'Sobrancelhas hirsutas']

    nascimentoMundano = [
        'Em uma área montanhosa', 'Em um pântano',
        'Em um casebre no meio do nada', 'Em um vilarejo',
        'Em um navio', 'Em uma floresta', 'Em uma caverna',
        'Em uma cidade portuária', 'Em uma fortaleza anã',
        'Em um grande centro urbano', 'Em uma fazenda',
        'Em uma aldeia élfica', 'Em uma comunidade halfling',
        'Em um monastério ou templo clerical', 'Em uma ilha',
        'Em um reino distante', 'Durante uma viagem',
        'Você não sabe nada sobre seu nascimento',
        'Em um acampamento de salteadores', 'Em um circo',
        'Em uma cidade de porte médio', 'Em um cemitério',
        'Em um campo de batalha', 'Em um acampamento cigano',
        'No subterrâneo', 'Na capital do reino',
        'Em uma cela de prisão', 'No palácio real',
        'Em um deserto', 'Em um local completamente destruído']

    nascimentoEspecial = [
        'Durante um equinócio', 'Durante um solstício',
        'Durante um ataque de mortos vivos',
        'Durante o ataque de um dragão',
        'Em uma importante data religiosa', 'Prematuramente',
        'Durante uma terrível tempestade',
        'Durante a passagem de um cometa',
        'Em uma construção sobre as nuvens',
        'Nas condições de uma antiga profecia',
        'Em uma ilha que afundou',
        'Durante uma chuva de estrelas cadentes',
        'Em um ritual arcano', 'Durante um eclipse solar',
        'Durante uma aurora boreal/austral',
        'Você não nasceu, foi “construído” ou “criado”',
        'Durante um terremoto', 'Durante um ataque de orcs',
        'Você não sabe nada sobre seu nascimento',
        'Durante um eclipse lunar',
        'Durante a queda de um meteoro',
        'Em um outro plano de existência',
        'No momento da erupção de um vulcão',
        'Debaixo d’água, ou em um reino submerso',
        'Em um barco voador, ou aparato aéreo',
        'Durante uma grande epidemia',
        'No dia extra de um ano bissexto',
        'Role uma vez nesta tabela e outra na de nascimento mundano',
        'Em outro planeta ou corpo celeste',
        'Role duas vezes nesta tabela']

    seusPais = [
        'Seus pais eram moradores de rua, a classe social mais baixa do populacho',
        'Você é completamente órfão e cresceu nas ruas ou em um orfanato',
        'Seus pais são nobres', 'Seus pais são mercadores/comerciantes',
        'Seus pais são ladrões/piratas/foragidos', 'Seus pais são aventureiros',
        'Seus pais são artistas/artesãos', 'Seus pais são escravos/servos',
        'Você foi adotado por uma raça diferente da sua', 'Seus pais são camponeses',
        'Você foi adotado por uma Instituição Religiosa', 'Sua mãe é uma rainha',
        'Você foi adotado por uma Guilda de Ladrões/Mercantes',
        'Seus pais são uma união de duas famílias inimigas',
        'Você é fruto de uma relação incestuosa', 'Você é um filho bastardo',
        'Sua mãe não sabe que você ainda vive', 'Seu pai é um rei',
        'Seu pai não sabe que você existe/ainda vive',
        'Você foi abandonado à própria sorte e não sabe nada sobre seus pais',
        'Ambos os seus pais são de outro plano/mundo',
        'Seus pais são separados e você tem madrasta e padrasto',
        'Você é filho de um ser de outro plano/mundo com um habitante deste mundo.',
        'Órfão de um, mas criado pelo outro. (Role para determinar qual morreu: par - pai; impar - mãe)',
        'Um de seus pais é membro do clero (Role para determinar quem: par - pai; impar - mãe)',
        'Seus pais são separados (Role para determinar quem lhe criou: par - pai; impar - mãe)',
        'Um de seus pais é nobre (Role para determinar: par - pai; impar - mãe)',
        'Órfão de pai e mãe, mas criado por outros (par - parentes. ímpar - não parentes)',
        'Seus pais são vivos, mas lhe deram para ser criado por outros (Role: par - parentes; impar - não parentes)',
        'Um de seus pais morreu e você tem uma madrasta ou padrasto (Role: par - padrasto; impar - madrasta)']

    sorte = [
        'Você herdou bens familiares (uma casa, terras,cavalo, dinheiro, armas, etc.)',
        'Sua infância foi próxima a circos/estábulos/afins e aprendeu coisas que acalmam os animais.',
        'Você ou sua família encontrou um item muito poderoso e desejado.',
        'Independente de seu status social, você conviveu com nobres na corte, e você acabou recebendo educação para se portar entre eles',
        'Você encontrou um mestre que lhe ensinou uma técnica/segredo profissional importante e fenomenal.',
        'Você ou sua família descobriu um segredo importante que pode beneficiá-lo de alguma forma muito vantajosa.',
        'Uma pessoa de poder político ou econômico no reino lhe deve um favor',
        'Você encontrou um mapa que pode guiá-lo a um grande tesouro que pode existir ou não.',
        'Uma criatura poderosa (ex: um gênio, um dragão, uma fada, etc.) lhe deve um favor',
        'Você e sua família estão em boas graças com o clero local. Além disso, você fosse muito bem educado nas tradições religiosas.',
        'Você ou sua família fez um contato poderoso nos altos escalões de governo do reino (um conselheiro/regente/ministro).',
        'Você nasceu em um dia iluminado, e os animais selvagens tendem a reagir positivamente na sua presença e tentativa de contatos.',
        'Você ganhou a confiança de uma guilda ou grupo comum. (de ladrões, de artífices, de mercadores, etc.)',
        'Você tornou-se próximo de membros de uma comunidade de uma outra raça e eles lhe consideram um amigo de seu povo.',
        'Você ganhou a confiança da guilda (de ladrões, de artífices, de mercadores, etc.) mais poderosa do reino',
        'Você tem uma facilidade natural para línguas, podendo aprender qualquer uma (desde que haja alguém com quem aprender).',
        'Sua família está envolvida em uma conspiração, em uma posição confortável',
        'Sua família descende de um grande e famoso herói, e seu sobrenome é muito reconhecido.',
        'Sua família recebeu algum tipo de benção divina ou dom especial',
        'Você possui um ancestral de outra raça e eles o consideram como parente',
        'Seu sangue possui tradição em derrotar certo tipo de criatura',
        'Você tem um dom natural para passar emoções distintas com sua voz, seja um grito em batalha, ameaça numa interrogação, ou um galanteio.',
        'Você adquiriu uma simpatia inexplicável de alguém forte e poderoso',
        'Você puxou só o melhor de seus pais! Sua beleza não passa despercebida pelas outras pessoas.',
        'Você teve acesso a uma vasta biblioteca desde pequeno, tendo contato com outras culturas e línguas desde jovem.',
        'Você herdou um verdadeiro estômago de avestruz, e é capaz de comer coisas que fariam a maioria das pessoas passar mal.',
        'Você cresceu num local pouco lúgrube e isso o tornou mais resistente à doenças.',
        'Um grupo religioso/criminoso vê em você o líder ideal para a organização/igreja.',
        'Você cresceu no campo, aprendendo a utilizar a natureza a sua volta para obter informações',
        'Você é realmente muito sortudo. Role duas vezes nesta tabela.']

    tragedia = [
        'Sua família perdeu tudo devido a uma traição',
        'Sua família foi dizimada por monstros. Você pode ou não ser o único sobrevivente.',
        'Sua família faliu devido à má administração',
        'Sua família é afligida por algum tipo de doença.',
        'Sua família foi exilada',
        'Sua família foi vitimada por uma epidemia',
        'Sua família está aprisionada em algum lugar.',
        'Sua família foi escravizada', 'Sua família desapareceu!',
        'Sua família perdeu tudo com dívidas de jogo',
        'Sua família está envolta em uma conspiração',
        'Você adquiriu algum tipo de vício',
        'Sua família é vive em guerra interna por poder',
        'Você herdou dívidas familiares',
        'Você sofreu um acidente que o deixou com sequelas físicas para sempre (olho perdido, maneta, dedos perdidos, manco, cicatrizes, etc)',
        'Você provocou, inadvertidamente, a destruição de sua família',
        'Você é considerado a ovelha negra da família e desacreditado por seus parentes',
        'Sua família é vítima de uma maldição',
        'Você traiu sua família', 'Sua família está sendo caçada',
        'Você teve contato com um grande horror sobrenatural que o deixou com sequelas mentais. Quase todos (exceto aqueles mais próximos) o consideram louco.',
        'Sua família sofre com perseguições religiosas ou culturais',
        'Você ou sua família descobriu um segredo importante, e alguém quer garantir que isso continue sendo um segredo.',
        'Você foi responsável pela morte de um membro de sua família',
        'Você já esteve preso por 1d6 meses',
        'Você foi traído. (Role 1d30 para determinar: 1-2-amigo; 3-4-parente; 5-6-colega de trabalho ou integrante do mesmo grupo)',
        'Você teve um(a) amante, amigo ou parente morto.(Par - Você não sabe quem foi, nem tem pistas do assassino; Impar - Você sabe quem foi o responsável, mas precisa de provas)',
        'Você está sendo caçado por uma guilda poderosa(de ladinos, de comerciantes etc) por algo que fez; há provas que apontam sua culpa no caso (Par - Não foi você quem fez, e as provas são forjadas; Impar - Foi você quem fez, e eles tem provas concretas',
        'Você foi acusado de um crime e hoje é considerado fora-da-lei e perseguido pela guarda do reino. (Par – Você é culpado pelo crime; Impar – Você foi acusado injustamente por um crime que não cometeu)',
        'Você é do tipo judiado pela vida. Role duas vezes nesta tabela.']

    statusInicial = ['Escravo', 'Plebeu', 'Nobre']

    profissaoEscravo = [
        'Camareiro', 'Pajem', 'Escravo Sexual', 'Prostituta',
        'Bufão', 'Bobo da Corte', 'Lenhador', 'Provador Real',
        'Faxineiro', 'Trabalhador Braçal', 'Malabarista',
        'Estivador', 'Acrobata', 'Marinheiro', 'Garimpeiro',
        'Gladiador', 'Dançarino', 'Jardineiro', 'Coveiro',
        'Tratador de Animais', 'Limpador de Fossas', 'Remador',
        'Carvoeiro', 'Mineiro', 'Pastor de Animais',
        'Pedreiro', 'Cozinheiro', 'Limpador de Chaminés',
        'Servente Doméstico', 'Fiandeiro', 'Cordoeiro',
        'Trabalhador Agrícola', 'Lavadeira', 'Eunuco',
        'Cesteiro', 'Controlador de Pragas', 'Escriba',
        'Role a profissão na tabela de PLEBEUS']

    profissaoPlebeu = ['Role a profissão na tabela de ESCRAVOS', 'Mendigo',
                       'Ferreiro', 'Taverneiro', 'Estalajadeiro',
                       'Ceramicista', 'Oleiro', 'Curtidor', 'Agricultor',
                       'Alfaiate', 'Sapateiro', 'Armeiro', 'Padeiro',
                       'Açougueiro', 'Cirireiro (Fazedor de Velas)',
                       'Ator', 'Ourives', 'Joalheiro', 'Carpinteiro',
                       'Ajudante do Clero', 'Vendedor', 'Feirante',
                       'Mascate', 'Dono de Bordel', 'Capataz', 'Pescador',
                       'Caçador', 'Peleiro', 'Herbalista', 'Apotecario',
                       'Bibliotecário', 'Copista', 'Cervejeiro',
                       'Vinicultor', 'Tecelão', 'Membro do Baixo Clero',
                       'Bandido (Role para determinar: 1-batedor de carteiras; 2-salteador; 3-matador; 4–arrombador de casas; 5–capanga)',
                       'Soldado (Role para determinar: 1-miliciano; 2-guarda; 3–mercenário; 4-soldado profissional; 5-veterano de guerra)',
                       'Role a profissão na tabela de NOBRES']

    profissaoNobre = ['Role a profissão na tabela de PLEBEUS',
                      'Artista (Role para determinar: 1–escultor; 2–pintor; 3–músico; 4–escritor; 5-poeta)',
                      'Falcoeiro', 'Escudeiro', 'Fazendeiro Livre', 'Médico',
                      'Conselheiro Religioso', 'Conselheiro Real', 'General',
                      'Magistrado', 'Coletor de Impostos', 'Comandante',
                      'Membro do Alto Clero', 'Sábio', 'Mercador',
                      'Capitão de Navio', 'Navegador', 'Jogador', 'Tutor',
                      'Escravista', 'Cavaleiro', 'Senhor de Moinho ou Engenho',
                      'Minerador (Dono de Mina)', 'Astrônomo ou Astrólogo',
                      'Pecuarista (Grande Criador de Animais)', 'Lutier',
                      'Embaixador, Arauto ou Diplomata', 'Guarda Florestal',
                      'Barbeiro', 'Cartógrafo', 'Aprendiz de Feiticeiro',
                      'Alquimista', 'Engenheiro', 'Guarda-Caça']

    amigo = ['Um antigo mentor', 'Um membro do clero', 'Um amigo de infância',
             'Um colega de armas', 'Um grande sábio', 'Um antigo amante',
             'Um mercador', 'Um ex-inimigo', 'Um pirata', 'Seu patrão',
             'Um empregado', 'Um filho de seu patrão', 'Um cavaleiro',
             'O chefe de uma quadrilha de salteadores', 'Um parente distante',
             'Alguém de uma raça odiada ou pouco comum', 'Um mago', 'Um nobre',
             'O dono da taverna', 'Um escravista', 'O ferreiro da cidade',
             'Um mercenário', 'Um soldado', 'O capitão de um navio',
             'O chefe da guarda', 'Um general ou alto comandante militar',
             'Um ladrão', 'O chefe da guilda de ladrões',
             'Alguém com quem trabalhou', 'O rei']

    origemAmizade = ['Você salvou a vida dele', 'Ele salvou a sua vida',
                     'Ele é como um pai para você',
                     'Ele é como um filho para você',
                     'Ele é como se fosse seu irmão mais velho',
                     'Ele é como se fosse seu irmão mais novo',
                     'Você defendeu a honra dele',
                     'Ele defendeu sua honra',
                     'Suas famílias são amigas de longa data',
                     'Vocês simplesmente gostam um do outro.',
                     'Ele o defendeu em uma briga ou combate',
                     'Você o defendeu em uma briga.',
                     'Ele lhe emprestou dinheiro',
                     'Você lhe emprestou dinheiro',
                     'Vocês tiveram negócios juntos',
                     'Você admira as habilidades dele',
                     'Ele admira as suas habilidades',
                     'Vocês fizeram um pacto de sangue',
                     'Ele ajudou sua família',
                     'Você ajudou a família dele',
                     'Vocês trabalharam juntos no passado',
                     'Vocês tiveram o mesmo mestre',
                     'Você voluntariamente assumiu a culpa por algo que ele fez',
                     'Ele voluntariamente assumiu a culpa por algo que você fez',
                     'Vocês enfrentaram um perigos juntos',
                     'Vocês compartilham um segredo',
                     'Vocês possuem um forte interesse comum por alguma coisa',
                     'Vocês cresceram juntos', 'Vocês foram vizinhos',
                     'Vocês frequentavam o mesmo local (taverna, igreja, etc.)']

    inimigo = ['Um ex-amante', 'Um inimigo de infância', 'Um membro do clero',
               'Alguém com quem trabalhou', 'Um nobre', 'Um colega de armas',
               'Seu ex-patrão', 'Um filho de seu patrão', 'Um soldado','O rei',
               'Um ex-amigo', 'Um parente distante', 'Um ladrão','Um mercador',
               'O ferreiro da cidade', 'O dono da taverna','O chefe da guarda',
               'Um empregado', 'O chefe de uma quadrilha de salteadores',
               'Um antigo mentor','Um grande sábio','Um pirata','Um cavaleiro',
               'Alguém de uma raça odiada ou pouco comum', 'Um escravista',
               'Um mercenário', 'O capitão de um navio',
               'Um general ou alto comandante militar',
               'O chefe da guilda de ladrões', 'Um mago']

    causaInimizade = [
        'Você causou a morte de um ente querido dele (Role para determinar: 1-aliado; 2-amigo; 3-parente; 4-amante)',
        'Ele causou a morte de um ente querido seu (Role para determinar: 1-aliado; 2-amigo; 3-parente; 4-amante)',
        'Você deve dinheiro a ele', 'Você rejeitou uma proposta dele',
        'Ele deve dinheiro a você', 'Ele rejeitou uma proposta sua',
        'Você ofendeu sua honra',
        'Ele o abandonou ou traiu', 'Ele ofendeu sua honra',
        'Você o abandonou ou traiu',
        'Você tem algo que deveria ter sido dado a ele',
        'Você humilhou-o publicamente',
        'Ele tem algo que deveria ter sido dado a você',
        'Ele humilhou-o publicamente',
        'Um amor em comum preferiu ficar com você',
        'Ele fez você perder seu prestígio',
        'Um amor em comum preferiu ficar com ele',
        'Você fez ele perder seu prestígio',
        'Ele causou-lhe uma deficiência física ou mental',
        'Você causou-lhe uma deficiência física ou mental',
        'Suas cidades são rivais tradicionais',
        'Você enganou ele numa situação de negócios',
        'Suas famílias são inimigas',
        'Ele te enganou numa situação de negócios',
        'Ele tem inveja de suas habilidades',
        'Você frustrou os planos dele',
        'Você tem inveja das habilidades dele', 'Ele frustrou seus planos',
        'Vocês simplesmente não se gostam, sem maiores razões',
        'Vocês foram enganados por um terceiro, mas culpam um ao outro']

    consequenciaInimizade = [
        'Vão se insultar em via pública', 'Vão jogar pedras um no outro',
        'Você irá partir para cima do outro, que tentará fugir',
        'Seu inimigo irá partir para cima de você, que tentará fugir',
        'Ambos vão partir um para cima do outro', 'Um vai ignorar o outro',
        'Um vai ignorar o outro, mas tentarão se apunhalar depois',
        'Seu inimigo vai chamar um grupo para dar cabo de você',
        'Seu inimigo irá propor um duelo até a morte',
        'Você irá propor um duelo até a morte', 'Você tentará ridicularizá-lo',
        'Seu inimigo tentará ridicularizá-lo',
        'Seu inimigo fará uma armadilha (mortal ou não) para você',
        'Você fará uma armadilha (mortal ou não) para seu inimigo',
        'Seu inimigo tentará manchar sua honra',
        'Você tentará manchar a honra de seu inimigo',
        'Seu inimigo espalhará boatos e mentiras sobre você',
        'Você espalhará boatos e mentiras sobre seu inimigo',
        'Seu inimigo tentará culpá-lo de algum crime',
        'Você tentará culpar seu inimigo de algum crime',
        'Você tentará prejudicar os negócios ou carreira de seu inimigo',
        'Seu inimigo tentará prejudicar seus negócios ou sua carreira',
        'Seu inimigo tentará capturá-lo e mantê-lo prisioneiro, ou vendê-lo como escravo',
        'Você tentará capturar seu inimigo e mantê-lo prisioneiro, ou vendê-lo como escravo',
        'Você tentará aleijar ou mutilar seu inimigo',
        'Seu inimigo tentará aleijar ou mutilar você',
        'Você atacará os parentes, amigos ou aliados de seu inimigo',
        'Seu inimigo atacará seus parentes, amigos ou aliados',
        'Você tentará assassinar seu inimigo',
        'Seu inimigo tentará assassiná-lo']

    vidaAmorosaList = ['Nunca se interessou ou nunca teve ninguém.',
                   'um CASO AMOROSO TRÁGICO OU PROBLEMÁTICO.',
                   'Apenas romances passageiros e pouco dignos de nota',
                   'Apenas um, mas um caso feliz e duradouro.']

    amorProblematico = [
        'A família do seu amor odeia você',
        'Suas famílias são rivais ou inimigas declaradas',
        'Sua família odeia seu amor',
        'Vocês são de raças diferentes',
        'Amigos de seu amor odeiam vocês',
        'Vocês são de classes sociais distintas',
        'Seus amigos odeiam seu amor',
        'Você foi o responsável pela morte do seu amor, ou pelo menos acredita que sim',
        'Família ou amigos do seu amor usarão de todos os meios para livrar-se de você',
        'Seu amor caiu nas graças de outro com quem passou a se relacionar',
        'Sua família ou amigos usarão de todos os meios para livrar-se de seu amor',
        'Seu amor desapareceu misteriosamente',
        'Você possui um rival amoroso',
        'A relação simplesmente fracassou',
        'Seu amor possui um rival amoroso',
        'Algo (como um objetivo pessoal) se interpôs entre vocês',
        'Magia os separa de alguma forma (ex: ela foi amaldiçoada a ser um falcão de dia e ele um lobo à noite)',
        'Seu amor foi raptado',
        'Brigas entre vocês são constantes',
        'Seu amor enlouqueceu',
        'Os amantes são rivais profissionais ou competem de alguma forma, de maneira extremamente acirrada',
        'Seu amor foi aprisionado ou exilado',
        'Você é extremamente ciumento',
        'Seu amor morreu em um acidente',
        'Seu amor é extremamente ciumento',
        'Seu amor foi morto em uma luta',
        'Você foi/é alvo da infidelidade de seu amor',
        'Seu amor foi covardemente assassinado',
        'Seu amor foi/é alvo de sua infidelidade',
        'Seu amor cometeu suicídio']

    reliquias = [
        'Uma arma', 'Uma ferramenta', 'Uma peça de roupa', 'Uma gema',
        'Uma gravura', 'Um livro', 'Um diário', 'Um pergaminho', 'Uma carta',
        'Um instrumento musical', 'Uma jóia', 'Um cantil ou odre', 'Uma chave',
        'Um brinquedo ou jogo', 'Um chapéu', 'Uma moeda',
        'Uma armadura, escudo ou elmo', 'Uma mochila ou bolsa', 'Um lenço',
        'Um símbolo sagrado ou outro objeto religioso',
        'Uma pequena caixa, baú, ou porta-jóias', 'Uma máscara', 'Um mapa',
        'Um pedaço de um animal ou monstro', 'Uma caneca ou taça', 'Uma pena',
        'Um pedaço de um humano ou humanóide', 'Uma pequena escultura',
        'Um item mágico menor. Talvez você desconheça sua natureza mágica.',

        'Um poderoso item mágico inteligente, que vê grande futuro em você, '
        'mas o acha pouco experiente ou sábio para usar todo seu poder.'
        ' Provavelmente nem desconfia disso.']

    naoGosta = [
        'Você não gosta de alguma raça (escolha qual)', 'Calor','Frio',
        'Um animal comum (cavalos, cachorros,gatos, vacas, camelos, etc.)',
        'Magia', 'Religião', 'Do gênero feminino em geral', 'Do dia',
        'Você não gosta do odor de alguma coisa (escolha o quê)', 'Velhos',
        'Você não gosta do sabor de alguma bebida ou comida (escolha o quê)',
        'Grandes massas d’água', 'De combates', 'Crianças', 'Da noite',
        'Do gênero masculino em geral', 'Falar em meio a multidões', 'Sujeira',
        'Lugares altos', 'Lugares apertados', 'Política', 'Mentiras',
        'De estar sozinho', 'De estar sóbrio', 'De aglomerações de pessoas',
        'De algum veículo (escolha qual)', 'De alguma(s) palavra(s)',
        'De expor o corpo', 'De não expor o corpo',
        'Role duas vezes nessa tabela']

    medo = [
        'Ficar velho e fraco',
        'Ser abandonado por seus entes queridos', 'Viajar de barco', 'Magia',
        'Um tipo de animal (escolha um)', 'Ser ignorado para sempre',
        'Um tipo de monstro (escolha um)', 'Ser humilhado publicamente',
        'Cair em uma armadilha', 'Ser devorado vivo', 'Ficar pobre',
        'Falhar com seus companheiros ou traí-los', 'Mortos-vivos', 'Da morte',
        'Perder um membro (escolha qual)', 'Ser enterrado vivo', 'De altura',
        'Perder um dos sentidos (escolha qual)', 'Afogar-se', 'Ser traído',
        'Perder a memória depois de tornar-se alguém de destaque em sua carreira',
        'Perder-se e acabar num lugar desconhecido', 'Enlouquecer',
        'Falhar com seu deus', 'Ser incapaz de manter-se honrado',
        'Transformar-se em outra criatura ou monstro',
        'Algum deus em específico (escolha um)',
        'Perder algo importante (escolha o que)',
        'De um objeto: uma arma, bonecas de louça, crânios, etc (escolha um)',
        'Role duas vezes nessa tabela']

    opiniaoDesconhecidos = [
        'Você não respeita ninguém que pertença a uma classe social que seja inferior à sua',
        'Você não respeita ninguém que pertença a uma classe social que seja superior à sua',
        'Você não respeita ninguém que pertença a uma classe social que seja diferente da sua',
        'Neutra em relação a todos. Você espera conhecê-los para julgá-los.',
        'Favorável em relação a todos. Você gosta de todo mundo antes mesmo de conhecê-los.',
        'Desfavorável em relação a todos. Você odeia todo mundo antes mesmo de conhecê-los.',
        'As pessoas são ferramentas que devem ser usadas em prol de seus objetivos',
        'Todas as pessoas são indivíduos de valor',
        'As pessoas são obstáculos a serem destruídos se atrapalharem seu caminho',
        'Ninguém é confiável, por isso você deve se virar sozinho',
        'A maioria das pessoas são incompetentes e inúteis, ainda que não sejam pessoas ruins',
        'Os membros do sexo oposto em geral são indignos de confiança',
        'Os membros do seu próprio sexo em geral são indignos de confiança',
        'Os membros do sexo oposto devem ser usados e descartados',
        'Os membros do seu próprio sexo são apenas ferramentas descartáveis a serem usadas em seus planos',
        'Você odeia todos os membros de seu próprio sexo',
        'Você odeia todos os membros do sexo oposto',
        'Os membros do sexo oposto são incompetentes e inúteis, ainda que não sejam pessoas ruins',
        'Os membros do seu próprio sexo são incompetentes e inúteis, ainda que não sejam pessoas ruins',
        'As pessoas são como pedras brutas a serem lapidadas por você',
        'Pessoas com pensamentos diferentes do seu não merecem sua atenção',
        'Pessoas com pensamentos diferentes do seu tem a sua atenção, pois você espera que elas lhe ensinem algo',
        'Pessoas com pensamentos diferentes do seu recebem sua atenção, mas você não os leva a sério',
        'Você é extremamente tolerante, não está nem aí para ninguém, o que pensam sobre você, o que você pensa sobre elas, contanto que você esteja seguro, tudo sempre estará bem',
        'Os membros de sua própria raça são incompetentes e inúteis, ainda que não sejam pessoas ruins',
        'Os membros das outras raças são incompetentes e inúteis, ainda que não sejam pessoas ruins',
        'Os membros de outras raças são apenas ferramentas descartáveis a serem usadas em seus planos',
        'Os membros de sua própria raça são apenas ferramentas descartáveis a serem usadas em seus planos',
        'Você odeia todos os membros de sua própria raça',
        'Você odeia todos os membros de outras raças que não a sua',
        'Os membros de outras raças em geral são indignos de confiança',
        'Os membros de sua própria raça em geral são indignos de confiança, mas não os de outras raças']

    principalArrependimento = [
        'Você não se arrepende de nada. Nunca. Talvez você seja egoísta e acredite que está sempre correto.',
        'Você se arrepende de ter traído seu (a) companheiro (a) com outra pessoa',
        'Você se arrepende de ter bebido demais na taverna, ter apagado e acordado no estábulo, nu e sem lembrar do que aconteceu; isso o tornou motivo de boatos e chacotas na cidade',
        'Você se arrepende de ter confessado seu amor a quem, faz pouco caso e o ignora completamente',
        'Você se arrepende de ter nascido!',
        'Você se arrepende de nunca tomar as decisões urgentes na velocidade em que precisam ser tomadas',
        'Você se arrepende de ter confiado seu tesouro a um ex-colega de grupo, que fugiu com o dinheiro',
        'Você se arrepende de ter contraído AQUELA dívida com um dos comerciantes mais ricos da cidade',
        'Você se arrepende de estar em dívida com uma perigosa guilda, e convive com o temor de ser morto',
        'Você sempre se arrepende de ter comido mais um pouco da última vez...',
        'Você se arrepende de não ter sido capaz de impedir a morte de um companheiro ou ente querido',
        'Você se arrepende de não ter seguido outra carreira',
        'Você se arrepende de ter dito que iria ajudar',
        'Você se arrepende daquela vez na qual uma anã barbuda lhe ofereceu uma bebida e então você não se lembra muito bem do que aconteceu em seguida, ou diz não se lembrar',
        'Você se arrepende de ter negado ajuda a alguém',
        'Você se arrepende de ter tirado a vida de alguém',
        'Você se arrepende de ter confiado em alguém',
        'Você se arrepende de ter adquirido algum bem ou objeto (decida com o mestre o que é)',
        'Você se arrepende de ter feito algo errado/vergonhoso/danoso graças à bebida (ou graças a um vício)',
        'Você se arrepende por ter contraído um voto ou juramento a uma pessoa ou organização',
        'Você se arrepende de ter quebrado um voto ou juramento a uma pessoa ou organização',
        'Você se arrepende de ter assinado um contrato anos atrás (determine com o mestre do que se trata)',
        'Você se arrepende de ter subido na vida pisando nos outros',
        'Você se arrepende de ter abandonado sua família',
        'Você se arrepende de ter constituído uma família',
        'Você se arrepende amargamente das brigas que teve com seus pais',
        'Você se arrepende de não ter pedido perdão a alguém que amava, a quem magoou tremendamente',
        'Você se arrepende de não ser mais extrovertido',
        'Você se arrepende de ter gostado de quem não deveria, uma vez na vida...',
        'Você se arrepende de ter feito um pacto de sua alma com uma entidade demoníaca; após ter obtido seu benefício (defina-o com o mestre), convive com o drama da danação eterna quando morrer'
    ]

    manias = [
        'Você pratica toda noite (ou dia, ou manhã) para melhorar sua habilidade em alguma coisa',
        'Você enrola seu cabelo ou barba enquanto pensa',
        'Você coleciona troféus de inimigos vencidos',
        'Você mantém um diário onde registra seu dia e faz anotações constantes',
        'Você sempre entra nos locais com o pé direito',
        'Você constantemente afia sua arma',
        'Você abre ou tenta abrir qualquer objeto fechado para ver o que tem dentro',
        'Você bate três vezes em madeira toda vez que alguém diz algo horrível',
        'Você sempre erra o nome das pessoas, ou as chama por apelidos ou por sua profissão',
        'Você é extremamente vaidoso e preocupa-se muito com sua aparência; narcisista',
        'Você faz uma postura ou gesto específico com sua arma antes de entrar em combate',
        'Você vive fazendo trocadilhos',
        'Você repete uma palavra ou uma expressão (“digo”, “né”, “assim”, “ahn”, “por Crom”, etc.)',
        'Você possui um grito de guerra extravagante',
        'Você costuma cuspir o tempo todo',
        'Você gagueja quando encarado(a) pelo sexo oposto (ou mesmo sexo, dependendo de sua preferência)',
        'Você cantarola ou assovia o tempo inteiro',
        'Você costuma empregar expressões altamente heréticas (ex:“Pela sagrada barba fedorenta de Netuno!”)',
        'Você sempre chega adiantado em seus compromissos',
        'Você sempre se atrasa de propósito',
        'Você costuma carregar dois de cada item que tiver por precaução',
        'Você veste-se inteiramente de uma mesma cor',
        'Você costuma dar um nome extravagante para todos os seus objetos importantes, como suas armas e armadura, e talvez até para você mesmo',
        'Você fica dizendo: “Ok! Ok! Perfeito!”, ou outra exclamação de concordância, mas fora isso passa a maior parte do tempo calado',
        'Você tem um tique nervoso (rói unhas, pisca seu olhos inúmeras vezes, força a vista, etc)',
        'Você erra alguma letra (troca r por l, ou r por g)',
        'Você é supersticioso e adquire tudo quanto é tipo de amuleto e badulaques para espantar a má sorte',
        'Você costuma ter vários casos com homens e/ou mulheres em cada cidade ao mesmo tempo, o que pode render situações complicadas e/ou pitorescas',
        'Você tende a ser rude e grosseiro com todos, e se porta de forma inadequada em eventos sociais',
        'Você coleciona alguma coisa: adagas, moedas, anéis, borboletas, mapas, gemas, etc. (escolha o quê)']

    motivacaoAventureira = [
        'Você é mercenário trabalha por dinheiro', 'Você busca a imortalidade',
        'Você procura reencontrar um amor perdido',
        'Você foi salvo por um aventureiro quando criança e deseja se tornar um',
        'Você nem sabe porquê, as aventuras simplesmente cruzam seu caminho o tempo todo',
        'Você possui motivos altruístas e quer ajudar os necessitados',
        'Você almeja fama e glória, e ter seus feitos cantados pelos bardos',
        'Você acredita que tem um destino a cumprir',
        'Você pretende atrair a atenção de uma guilda ou pessoa influente',
        'Você precisa/quer recuperar uma herança perdida, seja porque foi roubada, porque o dono original também desapareceu, etc.',
        'Você perdeu uma aposta num jogo de bar e agora está fadado a anos de aventuras ao lado do ganhador dessa aposta',
        'Você pretende limpar o seu nome ou de sua família realizando grandes feitos',
        'Você pretender gravar seu nome na história e ser lembrado por algo importante',
        'Você gosta de emoções fortes', 'Você quer conhecer o mundo',
        'Você pretende alcansar o trono por esforço próprio',
        'Você deseja tornar-se um herói', 'Você está em uma missão sagrada',
        'Você busca um poder/magia/técnica/conhecimento/habilidade (escolha um) que deseja muito conseguir',
        'Você está buscando tesouros perdidos',
        'Essas aventuras me perseguem! Por mais que eu queira ficar longe!',
        'Você busca um artefato de grande poder',
        'Você busca uma criatura lendária',
        'Você deseja desvendar os mistérios de uma civilização perdida',
        'Você pretende ser o indivíduo mais bem sucedido de todos em seu campo de atuação.',
        'Você está numa busca por vingança',
        'Seu pai foi um aventureiro e transmitiu o legado à você',
        'Você quer tornar-se uma divindade',
        'Você foi colocado nessa vida por outra pessoa, e não sabia exatamente no que estava se metendo',
        'Você nem se dá conta de que está se aventurando, talvez encare tudo como acontecimentos normais do dia-a-dia.']

    feitoNotavel = [
        'Ajudei a expulsar algumas criaturas de minha cidade e mandá-las de volta para seu covil” (escolha uma criatura',
        'Você é uma pessoa de importância em sua cidade natal. Role três vezes nessa tabela e fique com todos os resultados.',
        'Role duas vezes nessa lista e fique com os dois resultados.',
        'Entrei em uma expedição rumo a uma cripta local com um grupo de aventureiros uma vez. Tudo bem que foi só pra carregar tocha, mas bem...',
        'Certa vez servi como batedor a um grupo que planejava atacar um povoado.',
        'Recebi uma recompensa para ir até um lugar e matar um homem para o meu contratante.',
        'Certo dia, voltando de uma viajem, encontrei uma criança raptada por goblins e a trouxe de volta.',
        'Afugentei um monstro da minha vila junto a uma multidão enfurecida com tochas e garfos de feno.',
        'Certa vez me uni a um grupo de aventureiros como guia e consegui sobreviver a um combate contra bandoleiros me escondendo debaixo da carroça.',
        'Uma vez, um líder de nossa aldeia/cidade/vila estava possuído por demônios. Então auxiliei os clérigos locais e um pequeno grupo de aventureiros a conseguir salvá-lo.',
        'Meus pais foram escravizados, quando eu era mais jovem. Alguns anos depois, consegui localizá-los e fugir com eles para longe dos captores.',
        'Encontrei um famoso bandido morto em um beco. Um comerciante passou por ali e achou que eu o tinha matado. Ao menos ele tinha bolsos fartos...',
        'Eu lembro da vez em que aquelas pragas gigantes infestaram o velho moinho. Eu e mais uns camponeses nos armamos e fomos até lá desinfestar o local!',
        'Dois grupos, de mercadores e fazendeiros disputavam o governo na minha cidade natal, e uma das lideranças foi morta. Adivinhe quem foi o responsável?',
        'Certa vez acompanhei uns homens santos em uma peregrinação para espalhar a fé e combater os infiéis.',
        'Certa vez coletei alguns ingredientes estranhos a pedido de um mago. Acho que para uma poção ou feito mágico qualquer.',
        'Presenciei um crime e ajudei o reino entregando informações importantes para os guardas reais.',
        'Ah, eu já invadi um templo/torre/mansão/ castelo e roubei uma jóia que estava lá. Pena que já gastei todo o dinheiro!',
        'Escapei de um covil de kobolds após ficar 5 dias preso.',
        'Fui escudeiro de um cavaleiro que partiu para terras distantes.',
        'Certa vez fui preso no calabouço de um mago sem motivo algum, mas consegui fugir depois de um homem chutar a porta da minha cela e me mandar correr pra longe.',
        'Um bando de orcs destruiu uma vila em que eu morei. Eu lutei com um deles e consegui escapar juntamente com um pequeno grupo de moradores, antes que eles nos capturassem.',
        'Derrotei um mago sem usar armas.',
        'Escapei de um comboio escravagista.',
        'Estava explorando a floresta e fiquei preso em areia movediça por 2 dias, e me alimentei de uma serpente que alcancei com um galho.',
        'Fui assistente de um mago e vi quando ele trouxe à vida uma criatura feita de pedaços de corpos. Sorte que eu fugi dali antes que fosse devorado também.',
        'Ganhei um concurso de quem bebia mais. Um dos participantes era um anão robusto.',
        'Liderei a contenção de um incêndio causado por goblinóides.',
        'Já escoltei uma caravana até a cidade vizinha como parte do grupo de segurança.',
        'Ajudei uns caras que exploraram as antigas ruínas carregando uns sacos. Nunca vi tanto ouro na minha vida!']

    criaturas = [
        'Orcs', 'Bugbears', 'Trogloditas', 'Goblins', 'Anões','Homens Lagarto',
        'Kobolds', 'Elfos', 'Aranhas Gigantes', 'Trolls', 'Elfos Negros',
        'Tirano Ocular', 'Ogros', 'Banshees', 'Wargs', 'Shoggoths', 'Sátiros',
        'Crias Estelares de Cthulhu',  'Lobisomens', 'Doppelgangers',
        'Demônios', 'Unicórnios', 'Nagas', 'Vampiros', 'Zumbis', 'Inumanos',
        'Gigantes', 'Hobgoblins', 'Esqueletos', 'Dragões']

    motivoOdioCriatura = [
        'Uma delas roubou todo o seu tesouro pessoal',
        'Uma delas sequestrou sua família',
        'Uma delas matou um amigo ou aliado seu',
        'Uma delas o seduziu mudando de forma',
        'Uma delas matou um ente querido seu(esposa, filho, pai, mãe...)',
        'Uma delas destruiu sua propriedade ou a de sua família',
        'Uma delas o chantageou por conhecer um vergonhoso segredo de seu passado',
        'Uma pessoa foi devorada por esse tipo de criatura na sua frente!',
        'Uma delas o induziu a participar de uma missão suicida e você percebeu isso tarde demais',
        'Você encara essas criaturas como aberrações da natureza que não deveriam existir',
        'Você tem sonhos recorrentes em que estas criaturas lhe ferem de alguma maneira',
        'Você entende essas criaturas como ofensivas à sua fé ou ao seu deus de alguma maneira',
        'Você perdeu para uma destas criaturas numa batalha, de forma vergonhosa e pública',
        'O povo do local onde você nasceu nutre uma inimizade ancestral contra essas criaturas',
        'Uma delas detém poder suficiente para dar-lhe ordens (e você deve obedecer)',
        'O ódio contra estas criaturas é apenas uma forma de descontar suas frustrações de outras origens',
        'Você acredita que essas criaturas vieram de outro plano ou mundo para invadir este mundo e dominá-lo',
        'Você foi agredido sem razão aparente por uma dessas criaturas, e foi deixado para morrer, mas para o azar delas, você não morreu',
        'Alguém lhe ensinou que essas criaturas deveriam ser odiadas, e você simplesmente segue essa filosofia sem nem mesmo pensar a respeito',
        'Uma delas espalhou impropérios a seu respeito nas vilas por onde passou; como resultado, você adquiriu infâmia e quase ninguém confia missões a você',
        'Uma vidente previu que você seria morto por uma dessas criaturas, por via das dúvidas você as elimina antes que elas tenham a oportunidade de realizar a visão',
        'Quem lhe ensinou os caminhos da vida de aventureiro odiava essa criatura por alguma razão, e passou esse ódio para você, mesmo que você não saiba o porquê',
        'Uma delas convenceu um amigo ou aliado importante de que você foi o responsável por algum gesto bárbaro, criminoso, e essa pessoa tornou-se sua inimiga hoje',
        'Você acredita que essas criaturas são irremediavelmente malignas, possivelmente mais malignas do que quaisquer outras, e algo tão maligno obviamente precisa ser destruído',
        'Você descobriu que uma delas cruelmente mudou temporariamente de forma para ter um filho seu (e hoje você persegue esse filho abominável, que vem trazendo horror, morte e destruição ao reino)',
        'Uma dessas criaturas chamou você de “filho de um unicórnio” na frente de dezenas de aventureiros embriagados na taverna mais fedorenta do cais da cidade, e você virou alvo de chacota eterna sempre que vai a essa cidade',
        'Você não tem uma razão verdadeira para odiar essa criatura, mas por alguma razão, outros atribuem que você é um caçador profissional desse tipo de criatura; negar essa fama que lhe foi atribuída significaria adquirir infâmia perante seus próximos',
        'Odiar? Quem disse que você a odeia? Tudo é uma grande farsa planejada por você com o único propósito de ganhar notoriedade e logicamente fama e dinheiro.',
        'Nenhuma razão em especial, você apenas acha essas criaturas repugnantes.']

    nivelPerdaAuditiva = [
        'Apresenta leve perda auditiva', 'Apresenta moderada perda auditiva',
        'Apresenta grave perda auditiva', 'Apresenta profunda perda auditiva']

    perdaMemoria = ['Não se lembra do passado.', 'Só lembra do passado.']

    # ############################## CONSTRUCTORS #############################
    def __init__(self):

        self.classe = self.setClass()
        self.genero = self.setGenero()
        self.sexualidade = self.setSexualidade()
        self.raca = self.setRacas()
        self.personalidade = self.setPersonalidade()
        self.introvertido = self.setIntrovertido()
        self.pele = self.setPele()
        self.corOlhos = self.setCorOlhos()
        self.corCabelos = self.setCorCabelos()
        self.tipoCabelos = self.setTiposCabelos()
        self.pais = self.setPais()
        self.naoGosta = self.setNaoGosta()
        self.medo = self.setMedo()
        self.opiniaoDesconhecidos = self.setOpiniaoDesconhecidos()
        self.arrependimento = self.setArrependimento()
        self.mania = self.setManias()
        self.motivacaoAventureira = self.setMotivacaoAventureira()
        self.feitoNotavel = self.setFeitoNotavel()

        # tipo de nascimento
        if self.dice.parImpar() < 2:
            self.nascimento = self.setNascimentoMundano()
        else:
            self.nascimento = self.setNascimentoEspecial()

        # irmãos?
        if self.dice.parImpar() < 2:
            self.irmaos = "Filho único"
        else:
            self.irmaos = str(self.dice.rolar(12) + 1)

        # Sorte/Tragedia
        self.sorteTragedia = self.dice.rolar(4)
        if self.sorteTragedia == 1:
            self.sorteTragedia = self.setTragedia()

        elif self.sorteTragedia == 2:
            self.sorteTragedia = self.setSorte()

        elif self.sorteTragedia == 3:
            self.sorteTragedia = self.setSorte() + " " + self.setTragedia()

        else:
            self.sorteTragedia = "Vida monótona"

        # Status Social Inicial
        self.statusInicial = self.setStatusInicial()

        # Profissão
        if self.statusInicial == "Escravo":
            self.profissao = self.setEscravo()

        elif self.statusInicial == "Plebeu":
            self.profissao = self.setPlebeu()

        elif self.statusInicial == "Nobre":
            self.profissao = self.setNobre()

        # Amigos e inimigos
        self.amigosInimigos = self.dice.rolar(4)

        if self.amigosInimigos == 0:
            self.amigosInimigos = self.setInimigo() + "\n" + self.setCausaInimizade() + "\n" + self.setConsequenciaInimizade()

        elif self.amigosInimigos == 1:
            self.amigosInimigos = self.setAmigo() + "\n" + self.setOrigemAmizade()

        elif self.amigosInimigos == 2:
            self.amigosInimigos = self.setAmigo() + "\n" + self.setOrigemAmizade() + "\n\n"
            self.amigosInimigos += self.setInimigo() + "\n" + self.setCausaInimizade() + "\n" + self.setConsequenciaInimizade()

        else:
            if self.dice.parImpar() < 2:
                self.amigosInimigos = self.setAmigo() + "\n" + self.setOrigemAmizade() + "\n\n" + \
                                      self.setAmigo() + "\n" + self.setOrigemAmizade() + "\n\n"
                self.amigosInimigos += self.setInimigo() + "\n" + self.setCausaInimizade() + "\n" + self.setConsequenciaInimizade()

            else:
                self.amigosInimigos = self.setAmigo() + "\n" + self.setOrigemAmizade() + "\n\n"
                self.amigosInimigos += self.setInimigo() + "\n" + self.setCausaInimizade() + "\n" + self.setConsequenciaInimizade() + "\n\n"
                self.amigosInimigos += self.setInimigo() + "\n" + self.setCausaInimizade() + "\n" + self.setConsequenciaInimizade()

        # Vida amorosa
        self.vidaAmorosa = self.dice.rolar(4)

        if self.vidaAmorosa == 1:
            self.vidaAmorosa = self.setAmorProblematico()
        else:
            self.vidaAmorosa = self.setVidaAmorosa(self.vidaAmorosa)

        # odeia quantas criaturas
        qtdCriaturas = self.dice.rolar(3) + 1
        self.criaturasOdiadas = ""
        counter = 0

        while counter < qtdCriaturas:
            self.criaturasOdiadas += self.setCriaturas() + "\n" + self.setMotivoOdioCriatura() + "\n\n"
            counter += 1

        # Deficiente
        self.deficiencia = self.dice.probabilidade(14, 100)

        if self.deficiencia:
            self.deficiencia = self.dice.rolar(8) + 1

            if self.deficiencia < 2:
                self.deficiencia = "Portador de autismo. "

            elif self.deficiencia < 3:
                self.deficiencia = self.setProblemaAuditivo()

            elif self.deficiencia < 4:
                self.deficiencia = "Deficiência Intelectual. "

            elif self.deficiencia < 5:
                self.deficiencia = self.setPerdaMemoria()

            elif self.deficiencia < 6:
                self.deficiencia = "Doença Mental "

            elif self.deficiencia < 7:
                self.deficiencia = "Deficiência Física "

            elif self.deficiencia < 8:
                self.deficiencia = "Problema na fala "

            else:
                self.deficiencia = "Problema na visão "

        else:
            self.deficiencia = "Não possui deficiência."

        # Doença Cronica
        self.doenteCronico = self.dice.probabilidade(8, 100)

        if self.doenteCronico:
            self.doenteCronico = "Possui doença crônica."
        else:
            self.doenteCronico = "Não é doente crônico."

        # Reliquia
        self.reliquia = self.dice.probabilidade(10, 100)

        if not self.reliquia:
            self.reliquia = "Não tem relíquia."

        else:
            self.reliquia = self.dice.rolar(100) + 1

            if self.reliquia < 26:
                self.reliquia = "Valiosa, "
            elif self.reliquia < 36:
                self.reliquia = "Mágica, "
            elif self.reliquia < 51:
                self.reliquia = "Especial, "
            else:
                self.reliquia = "Pessoal/imprestável, "

            self.reliquia += self.setReliquia()

    # ######################## PRINTING #######################################
    def __str__(self):
        return (
            '\nClasse: ' + self.classe +
            '\nRaça: ' + self.raca +
            '\n\nGênero: ' + self.genero +
            '\nOpção Sexual: ' + self.sexualidade +
            '\nPersonalidade: ' + self.personalidade +
            '\nIntro - Extro versão: ' + self.introvertido +
            '\n\nPele: ' + self.pele +
            '\nOlhos: ' + self.corOlhos +
            '\nCabelos: ' + self.corCabelos +
            '\nTipo de cabelo: ' + self.tipoCabelos +
            '\n\nNascimento: ' + self.nascimento +
            '\nPais: ' + self.pais +
            '\nIrmãos: ' + self.irmaos +
            '\n\nSorte - Tragédia: ' + self.sorteTragedia +
            '\n\nStatus inicial: ' + self.statusInicial +
            '\nProfissão: ' + self.profissao +
            '\n\nAmigos e Inimigos: ' + self.amigosInimigos +
            '\n\nVida Amorosa: ' + self.vidaAmorosa +
            '\n\nNão gosta de: ' + self.naoGosta +
            '\n\nMedo: ' + self.medo +
            '\n\nOpinião sobre desconhecidos: ' + self.opiniaoDesconhecidos +
            '\n\nArrependimento: ' + self.arrependimento +
            '\n\nMania: ' + self.mania +
            '\n\nMotivação Aventureira: ' + self.motivacaoAventureira +
            '\n\nPrimeiro Feito Notável: ' + self.feitoNotavel +
            '\n\nCriaturas odiadas: ' + self.criaturasOdiadas +
            '\n\nDeficiência: ' + self.deficiencia +
            '\nTêm alguma doença crônica? ' + self.doenteCronico +
            '\nRelíquia pessoal: ' + self.reliquia
        )

    # ############################## SETS #####################################
    def setClass(self):
        return choice(self.classes)

    def setGenero(self):
        selectedGender = choice(self.generos)

        # probabilidade de ser uma mulher trans é de 5 em 75.000
        trans = self.dice.probabilidade(5, 75000)
        if selectedGender == 'homem':
            # mas se for homem é de 5 em 25.000
            trans = self.dice.probabilidade(5, 25000)

        hermafrodita = self.dice.probabilidade(1, 25000)

        if trans:
            selectedGender += ' trans'
        if hermafrodita:
            selectedGender += ' hermafrodita'
        return selectedGender

    def setSexualidade(self):
        selectedSexualidade = 'hetero'

        if self.dice.probabilidade(5, 100):
            selectedSexualidade = choice(self.sexualidade)
        return selectedSexualidade

    def setRacas(self):
        return choice(self.racas)

    def setPersonalidade(self):
        qtd = self.dice.rolar(3) + 1
        x = 0
        selectedPersonalidade = ''

        while x != qtd:
            selectedPersonalidade += choice(self.tiposPsicologicos) + ' '
            x += 1
        return selectedPersonalidade

    def setPele(self):
        def cicatrizes(selectedPele, corPele, auxPele):
            if corPele[auxPele] == 'Cicatrizes':
                selectedPele += ' ' + corPele[auxPele]
                if self.dice.parImpar() % 2 == 0:
                    selectedPele += ' comuns'
                else:
                    selectedPele += ' ritualisticas'

                return selectedPele

            return selectedPele

        def tatuagens(selectedPele, corPele, auxPele):
            if corPele[auxPele] == 'Tatuagens':
                selectedPele += ' ' + corPele[auxPele]

            return selectedPele

        def marca(selectedPele, corPele, auxPele):
            if corPele[auxPele] == 'Marca de Nascença':
                selectedPele += ' ' + corPele[auxPele]

            return selectedPele

        def mancha(selectedPele, corPele, auxPele):
            if corPele[auxPele] == 'Pele manchada':
                if self.dice.parImpar() % 2 == 0:
                    selectedPele += ' mancha na pele mais clara que a pele'
                else:
                    selectedPele += ' mancha na pele mais escura que a pele'

            return selectedPele

        auxPele = self.dice.rolar(len(self.corPele))
        selectedPele = ''
        counter = 1

        while auxPele > 25:

            selectedPele += cicatrizes(selectedPele, self.corPele, auxPele)
            selectedPele += tatuagens(selectedPele, self.corPele, auxPele)
            selectedPele += marca(selectedPele, self.corPele, auxPele)
            selectedPele += mancha(selectedPele, self.corPele, auxPele)

            auxPele = self.dice.rolar(len(self.corPele))

        # A linha de baixo coloca valor ou completa o valor de selectedPele
        return selectedPele + ' ' + self.corPele[auxPele]

    def setCorOlhos(self):
        auxCorOlhos = self.dice.rolar(len(self.corOlhos))
        selectedCorOlhos = ''

        while auxCorOlhos > 24:
            selectedCorOlhos += self.corOlhos[auxCorOlhos] + ' '
            auxCorOlhos = self.dice.rolar(len(self.corOlhos))

        return selectedCorOlhos + self.corOlhos[auxCorOlhos]

    def setCorCabelos(self):
        auxCorCabelos = self.dice.rolar(len(self.corCabelos))
        selectedCorCabelos = ''

        if self.corCabelos[auxCorCabelos] == 'Careca':
            if self.dice.parImpar() % 2 == 0:
                return 'Careca porque raspa'
            else:
                return 'Naturalmente careca'

        while auxCorCabelos > 24 and auxCorCabelos < 28:
            selectedCorCabelos += self.corCabelos[auxCorCabelos] + ' '
            auxCorCabelos = self.dice.rolar(len(self.corCabelos))

        return selectedCorCabelos + self.corCabelos[auxCorCabelos]

    def setTiposCabelos(self):
        return choice(self.tiposCabelo)

    def setNascimentoMundano(self):
        return choice(self.nascimentoMundano)

    def setNascimentoEspecial(self):
        def NascimentoDuasTabelas(nascimentoEspecial, auxNascimentoEspecial):
            nascimentoEspecial.remove(
                nascimentoEspecial[auxNascimentoEspecial])
            auxNascimentoEspecial = self.dice.rolar(len(nascimentoEspecial))
            selectedNascimentoEspecial = nascimentoEspecial[
                auxNascimentoEspecial]
            selectedNascimentoEspecial += ' ' + self.setNascimentoMundano()
            return selectedNascimentoEspecial

        auxNascimentoEspecial = self.dice.rolar(len(self.nascimentoEspecial))
        selectedNascimentoEspecial = ''

        if self.nascimentoEspecial[
            auxNascimentoEspecial] == 'Role duas vezes nesta tabela':
            self.nascimentoEspecial.remove(
                self.nascimentoEspecial[auxNascimentoEspecial])

            for x in range(0, 2, 1):
                auxNascimentoEspecial = self.dice.rolar(
                    len(self.nascimentoEspecial))

                if self.nascimentoEspecial[
                    auxNascimentoEspecial] == 'Role uma vez nesta tabela e outra na de nascimento mundano':
                    selectedNascimentoEspecial += NascimentoDuasTabelas(
                        self.nascimentoEspecial, auxNascimentoEspecial) + ' '
                else:
                    selectedNascimentoEspecial += self.nascimentoEspecial[
                                                      auxNascimentoEspecial] + ' '

        elif self.nascimentoEspecial[
            auxNascimentoEspecial] == 'Role uma vez nesta tabela e outra na de nascimento mundano':
            selectedNascimentoEspecial += NascimentoDuasTabelas(
                self.nascimentoEspecial, auxNascimentoEspecial) + ' '
        else:
            selectedNascimentoEspecial += self.nascimentoEspecial[
                                              auxNascimentoEspecial] + ' '

        return selectedNascimentoEspecial

    def setPais(self):
        selectedPais = self.dice.rolar(30)
        aux = ''

        if selectedPais > 22:
            aux = self.dice.parImpar()

            if aux % 2 == 0:
                if selectedPais < 27:
                    aux = ', pai'
                if selectedPais < 29:
                    aux = ', parentes'
                if selectedPais < 30:
                    aux = ', padastro'
            else:
                if selectedPais < 27:
                    aux = ', mãe'
                if selectedPais < 29:
                    aux = ', não parentes'
                if selectedPais < 30:
                    aux = ', madastra'

        return self.seusPais[selectedPais] + aux

    def setSorte(self):
        selectedSorte = choice(self.sorte)

        if selectedSorte == 'Você é realmente muito sortudo. Role duas vezes nesta tabela.':
            self.sorte.remove(
                'Você é realmente muito sortudo. Role duas vezes nesta tabela.')
            selectedSorte = choice(self.sorte)
            self.sorte.remove(selectedSorte)
            selectedSorte += ' e ' + choice(self.sorte)
            return selectedSorte
        return selectedSorte

    def setTragedia(self):
        selectedTragedia = choice(self.tragedia)

        if selectedTragedia == 'Você é do tipo judiado pela vida. Role duas vezes nesta tabela.':
            self.tragedia.remove(selectedTragedia)
            auxTragedia1 = ''
            auxTragedia2 = ''
            while auxTragedia1 == auxTragedia2:
                auxTragedia1 = choice(self.tragedia)
                auxTragedia2 = choice(self.tragedia)

            if 23 < self.tragedia.index(auxTragedia1) < 26 and 23 < self.tragedia.index(
                    auxTragedia2) < 26:
                # Os 2 no D6
                auxTragedia1 += ' Resultado: ' + str(self.dice.rolar(6) + 1)
                auxTragedia2 += ' Resultado: ' + str(self.dice.rolar(6) + 1)

            elif 25 < self.tragedia.index(
                    auxTragedia1) < 29 and 25 < self.tragedia.index(
                    auxTragedia2) < 29:
                # Os 2 no par impar
                auxTragedia1 += ' Resultado: ' + str(self.dice.parImpar())
                auxTragedia2 += ' Resultado: ' + str(self.dice.parImpar())

            elif 25 < self.tragedia.index(
                    auxTragedia1) < 29 and 23 < self.tragedia.index(
                    auxTragedia2) < 26:
                # Um no par impar outro no D6
                auxTragedia1 += ' Resultado: ' + str(self.dice.parImpar())
                auxTragedia2 += ' Resultado: ' + str(self.dice.rolar(6) + 1)

            elif 23 < self.tragedia.index(
                    auxTragedia1) < 26 and 25 < self.tragedia.index(
                    auxTragedia2) < 29:
                # Um no D6 outro no par impar
                auxTragedia1 += ' Resultado: ' + str(self.dice.rolar(6) + 1)
                auxTragedia2 += ' Resultado: ' + str(self.dice.parImpar())

            elif 25 < self.tragedia.index(auxTragedia1) < 29 and self.tragedia.index(
                    auxTragedia2) < 24:
                # Um no par impar outro no nada
                auxTragedia1 += ' Resultado: ' + str(self.dice.parImpar())

            elif self.tragedia.index(auxTragedia1) < 24 and 25 < self.tragedia.index(
                    auxTragedia2) < 29:
                # Um no nada outro par impar

                auxTragedia2 += ' Resultado: ' + str(self.dice.parImpar())

            elif 23 < self.tragedia.index(auxTragedia1) < 26 and self.tragedia.index(
                    auxTragedia2) < 24:
                # Um no D6 outro no nada
                auxTragedia1 += ' Resultado: ' + str(self.dice.rolar(6) + 1)

            elif self.tragedia.index(auxTragedia1) < 24 and 23 < self.tragedia.index(
                    auxTragedia2) < 26:
                # Um no nada outro no D6

                auxTragedia2 += ' Resultado: ' + str(self.dice.rolar(6) + 1)

            return auxTragedia1 + ' ' + auxTragedia2

        if self.tragedia.index(selectedTragedia) < 24:
            return selectedTragedia
        elif self.tragedia.index(selectedTragedia) < 26:
            return selectedTragedia + ' Resultado: ' + str(self.dice.rolar(6) + 1)
        else:
            return selectedTragedia + ' Resultado: ' + str(self.dice.parImpar())

    def setStatusInicial(self):
        return choice(self.statusInicial)

    def setEscravo(self):
        selectedEscravo = choice(self.profissaoEscravo)

        if selectedEscravo == 'Role a profissão na tabela de PLEBEUS':
            return 'Escravo como plebeu ' + self.setPlebeu()

        return 'Escravo ' + selectedEscravo

    def setPlebeu(self):
        auxPlebeu = self.dice.rolar(len(self.profissaoPlebeu))
        if auxPlebeu == 0:
            return 'Plebeu como escravo ' + self.setEscravo()
        elif auxPlebeu == 29:
            return 'Plebeu como nobre ' + self.setNobre()
        elif auxPlebeu > 26:
            auxPlebeu = self.profissaoPlebeu[auxPlebeu] + ' ' + str(
                self.dice.rolar(5) + 1)
            return auxPlebeu
        else:
            return self.profissaoPlebeu[auxPlebeu]

    def setNobre(self):
        auxNobre = self.dice.rolar(len(self.profissaoNobre))
        if auxNobre == 0:
            return 'Nobre como plebeu ' + self.setPlebeu()
        elif auxNobre == 1:
            auxNobre = self.profissaoNobre[auxNobre] + ' ' + str(
                self.dice.rolar(5) + 1)
            return auxNobre
        else:
            return self.profissaoNobre[auxNobre]

    def setAmigo(self):
        return 'Amigo:\n' + choice(self.amigo)

    def setOrigemAmizade(self):
        return choice(self.origemAmizade)

    def setInimigo(self):
        return choice(self.inimigo)

    def setCausaInimizade(self):
        auxCausaInimizade = self.dice.rolar(len(self.causaInimizade))

        if auxCausaInimizade < 2:
            return (self.causaInimizade[auxCausaInimizade] + ' '
                    + str(self.dice.rolar(4) + 1))
        else:
            return self.causaInimizade[auxCausaInimizade]

    def setConsequenciaInimizade(self):
        return choice(self.consequenciaInimizade)

    def setVidaAmorosa(self, numero):
        return self.vidaAmorosaList[numero]

    def setAmorProblematico(self):
        return choice(self.amorProblematico)

    def setReliquia(self):
        return choice(self.reliquias)

    def setNaoGosta(self):
        auxNaoGosta = self.dice.rolar(len(self.naoGosta))
        if auxNaoGosta == 0:
            return 'Você não gosta da raça: ' + self.setRacas()

        return choice(self.naoGosta)

    def setMedo(self):
        auxMedo = self.dice.rolar(len(self.medo))
        selectedMedo = ''

        if auxMedo == 29:
            self.medo.remove(self.medo[29])
            for x in range(0, 2, 1):
                auxMedo = self.dice.rolar(len(self.medo))
                selectedMedo += self.medo[auxMedo] + ' '
                self.medo.remove(self.medo[auxMedo])
            return selectedMedo

        return choice(self.medo)

    def setOpiniaoDesconhecidos(self):
        return choice(self.opiniaoDesconhecidos)

    def setArrependimento(self):
        return choice(self.principalArrependimento)

    def setManias(self):
        return choice(self.manias)

    def setMotivacaoAventureira(self):
        return choice(self.motivacaoAventureira)

    def setFeitoNotavel(self):
        return choice(self.feitoNotavel)

    def setCriaturas(self):
        return choice(self.criaturas)

    def setMotivoOdioCriatura(self):
        return choice(self.motivoOdioCriatura)

    def setIntrovertido(self):
        auxIntrovertido = self.dice.rolar(3) + 1
        if auxIntrovertido < 3:
            return 'Ambivertido'
        else:
            if self.dice.parImpar() % 2 == 0:
                return 'Extrovertido'
            return 'Introvertido'

    def setProblemaAuditivo(self):
        return choice(self.nivelPerdaAuditiva)

    def setPerdaMemoria(self):
        return choice(self.perdaMemoria)
