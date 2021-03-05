# Jogo Resilia

def boas_vindas():
    #  Esta função tem como objetivo dar boas vindas ao usuário

    print('-*' * 60)
    print('Bem vindo ao jogo "Volta ao Lar"'.center(120))
    print('-*' * 60)


def selecao_avatar():
    nome = str(input('\nEscolha seu personagem, você tem 3 opções. '
                     '\nDigite [1] para personagem Taliyah, '
                     '[2] para personagem Senna e '
                     '[3] para personagem Nidalee: ')).strip()
    while nome != '1' and nome != '2' and nome != '3':
        nome = str(input(f'\nVocê digitou "{nome}". '
                         'Por favor, tente novamente com '
                         'uma opção válida.'
                         '\nDigite [1] para personagem Taliyah, '
                         '[2] para personagem Senna e '
                         '[3] para personagem Nidalee: ')).strip()
    print('-=' * 60)
    return nome


def escolha_de_personagem(numero_personagem):
    # Essa função tem como objetivo escolher o personagem
    nome = ''
    if numero_personagem == '1':
        nome = 'Taliyah'
    elif numero_personagem == '2':
        nome = 'Senna'
    elif numero_personagem == '3':
        nome = 'Nidalee'
    else:
        print('Você deveria corrigir algo')
    return nome


def explicacao(nome_da_personagem):
    # Essa função tem como objetivo explicar o cenário do jogo

    print('EXPLICAÇÃO E OBJETIVO DO JOGO'.center(120))
    print(f'\nA história acontece no reino de Valoran. Você estará na pele de '
          f'{nome_da_personagem}, uma jovem Shurimane que descobre um poder '
          f'\npotencialmente destrutivo e tenta a todo custo prolongar o dia '
          f'em que vai revelar isso para a sua tribo.'
          '\nSeu objetivo final é aprender a controlar seus poderes, '
          'a qualquer custo, antes que seja tarde.'
          '\nA Grande Tecelã, deusa Shurimane, lhe acompanhará na jornada, '
          'narrando acontecimentos e lhe guiando em seu caminho.'
          '\nBoa sorte.'
          )
    print('-=' * 60)


def escolher_regiao():
    local = str(input(f'{personagem}: Grande Tecelã, me guie. '
                      f'Para onde devemos ir?'
                      f'\nDigite [1] para ir a Noxus e '
                      f'[2] para ir a Ionia: ')).strip()
    while local != '1' and local != '2':
        local = str(input(f'\nVocê digitou "{local}". '
                          f'Por favor, tente novamente com uma opção válida.'
                          f'\nPara onde devemos ir?'
                          f'\nDigite [1] para ir a Noxus e '
                          f'[2] para ir a Ionia: ')).strip()
    return local


def introducao(nome_da_personagem):
    # Esta função introduz o usuário aos primeiros acontecimentos do jogo
    print('INTRODUÇÃO'.center(120))
    print(f'Babajan: {nome_da_personagem}, hora de acordar.'
          f'\n{nome_da_personagem}: Ahh, só mais cinco minutinhos.'
          f'\nBabajan: {nome_da_personagem}...'
          f'\n{nome_da_personagem}: (Isso nunca funciona. '
          f'Nem sei porque ainda tento.) '
          f'\n{nome_da_personagem}: Tá bem...  '
          f'\nBabajan: Hoje é um grande dia minha neta. Hoje vamos conhecer'
          f' seu destino. '
          f'\n{nome_da_personagem}: Vó...'
          f'\n{nome_da_personagem}: Será que...'
          f'\n{nome_da_personagem}: Eu realmente estou pronta?'
          f'\n{nome_da_personagem}: (Não mesmo)'
          f'\nBabajan: Minha querida... Não deve temer seu destino.'
          f'\nBabajan: O seu futuro depende somente de você.'
          f'\n{nome_da_personagem}: (É disso que tenho medo...)'
          f'\nBabajan: Vá se arrumar. Será uma longa noite.'
          f'\n{nome_da_personagem}: Está bem. \n'
          f'\n{nome_da_personagem}: As coisas em Shurima são bem monótonas, '
          f'embora eu ame esse lugar que chamo de lar.'
          f'\nShurima é basicamente um grande deserto. Fomos um império '
          f'triunfante quando ele estava conosco.' '\n'
          f'\n{nome_da_personagem}: Azir. Esse era o nome de nosso imperador. '
          f'Ele era muito adorado por todo o império.'
          f'\nSeu exército mataria e morreria por ele sem pestanejar. '
          f'Meio que isso aconteceu no ritual...' '\n'
          f'\n{nome_da_personagem}: Esse dia está marcado na história '
          f'de Shurima. O ritual de ascensão do imperador.'
          f'\nÉ como se fosse a coroação dada pelos deuses Shurimanes ao'
          f' imperador vigente.'
          f'\nOs sacerdotes e sacerdotisas eram os receptores destas vontades '
          f'divinas e o Disco Solar meio'
          f'\nque o batizava.', end=' '
                                    f'Era pra ser um dia lembrado como o triunfo de Azir, mas acabou '
                                    f'virando o dia de sua queda.' '\n'
                                    f'\n{nome_da_personagem}: Naquele dia, houve um eclipse. Algo deu '
                                    f'errado. Ninguém viu o que aconteceu.'
                                    f'\nQuando o sol voltou, Azir e seu exército não estavam mais ali. '
                                    f'O disco solar desapareceu.'
                                    f'\nTudo que nosso império tinha de mais importante havia '
                                    f'desaparecido.'
                                    f'\nNós, pessoas comuns, ainda estávamos ali. Mas Shurima não '
                                    f'estava mais.\n'
                                    f'\n{nome_da_personagem}: Depois deste fatídico dia, nosso reino '
                                    f'caiu no esquecimento. Mas há uma profecia.'
                                    f'\nO imperador vai retornar com sede de vingança. Revoltado com'
                                    f' seu império.'
                                    f'\nTalvez ele ache que algo foi tramado contra ele. Mas, ele não'
                                    f' vai retornar. Muito menos'
                                    f'\ndizimando Shurima, ou o que sobrou dela.\n\n...\n'
                                    f'\n{nome_da_personagem}: A lua chegou... Eu não sei se... '
                                    f'\nAstra: {nome_da_personagem}! Chegou a hora. Vamos, estou muito '
                                    f'ansiosa!  '
                                    f'\n{nome_da_personagem}: Mãe...  '
                                    f'\nAstra: O que?  '
                                    f'\n{nome_da_personagem}: Deixa pra lá. Vamos.  '
                                    f'\n{nome_da_personagem}: (Eu deveria contar...)  '
                                    f'\nAstra: Está todo mundo te esperando lá fora.\n\n...\n'
                                    f'\n{nome_da_personagem}: O meu destino, ou o fim dele, começa '
                                    f'aqui.\n'
                                    f'\n{nome_da_personagem}: Na minha tribo, todos os jovens quando '
                                    f'são crescidos o suficiente dançam '
                                    f'\nsob a lua cheia; uma manifestação da Grande Tecelã, a deusa '
                                    f'protetora das tribos de Shurima.'
                                    f'\nA dança celebrava talentos natos das crianças e demonstrava '
                                    f'as habilidades que elas '
                                    f'\nagregariam à tribo quando fossem adultas. Esse era o início '
                                    f'de suas jornadas a caminho do'
                                    f'\nreal aprendizado. Nesse momento, as crianças se tornavam '
                                    f'aprendizes de seus professores.\n'
                                    f'\n{nome_da_personagem}: Bem, hora de dançar.\n'
                                    f'\nGrande Tecelã: Então, {nome_da_personagem} começou sua '
                                    f'dança sob o luar. A natureza de seu poder foi revelada.'
                                    f'\nEmbora seja uma suave demonstração, sua tribo não recebeu '
                                    f'muito bem essa informação. '
                                    f'\nGrande Tecelã: Todos estavam assustados com seu poder. '
                                    f'Nenhum jovem na história da tribo havia'
                                    f'\ndemonstrado tais habilidades. \n'
                                    f'\nGrande Tecelã: Quando sua dança acabou e {nome_da_personagem} '
                                    f'abriu os olhos, via olhares de desprezo.'
                                    f'\nA cada virada de rosto era uma repulsa e medo estampado no'
                                    f' rosto de cada um. {nome_da_personagem} correu dali.'
                                    f'\nAssustada e com medo do julgamento de sua tribo, de sua família.'
                                    f'\nSua mãe foi logo atrás dela para tentar acolhê-la, porém '
                                    f'sem sucesso.'
                                    f'\n{nome_da_personagem} se trancou no seu quarto, debulhando-se '
                                    f'em lágrimas e se culpando por ser diferente.\n\n... \n'
                                    f'\nGrande Tecelã: Quando todo mundo adormeceu, {nome_da_personagem}'
                                    f' decidiu sair de seu quarto. '
                                    f'\nEstava decidida a deixar seu lar, por medo de não ser aceita. '
                                    f'Ela escreve um bilhete a sua mãe'
                                    f'\ne parte rumo a decidir seu destino. \n\n'
          )
    print('=-' * 60)


def primeira_decisao(destino, nome_da_personagem):
    # Essa função tem como objetivo dar rumo a história
    # com base na decisão do usuário
    decisao = ''
    if destino == '1':
        decisao = 'Noxus'
        print('=-' * 60)
        print('NOXUS'.center(120))
        print(f'\n{nome_da_personagem}: Dizem que Noxus é um bom lugar para '
              f'se tornar forte. Devemos seguir para lá. \n'
              f'\nGrande Tecelã: Então, seguindo seus instintos, '
              f'{nome_da_personagem} rumou em direção a Noxus.'
              f'\nNoxus é um império em que só os fortes prevalecem. Se você '
              f'tem força, você faz parte do império.'
              f'\nSe você é fraco, você é inútil. '
              f'\nEm Noxus havia muito preconceito em relação '
              f'a mulheres fortes e fracas. '
              f'\nPara ser uma mulher em local de destaque, você teria que '
              f'ser o quintúplo de um homem.'
              f'\nCaso você fosse fraca, você seria invisível na sociedade. '
              f'\nCinco vezes mais que um homem fraco.'
              f'\n{nome_da_personagem} não '
              f'conhecia muito bem sobre Noxus.'
              f'\nNoxus tem um grande plano de expansão do império. O maior '
              f'objetivo é reunir o melhor e maior exército'
              f'\npara invadir e conquistar outros territórios. Shurima um '
              f'dia poderia ser um alvo, ou talvez não.'
              f'\n \nGrande Tecela: Ao longo da viagem, {nome_da_personagem}'
              f' conhece o Capitão Gangplank.'
              f'\nGangplank é um capitão decadente que perdeu seu cargo de '
              f'poder em Noxus e quer reconquistá-lo.'
              f'\n{nome_da_personagem} cria certa confiança em Gangplank, '
              f'conta sua história e lhe mostra seu poder.'
              f'\nEle vê nela uma oportunidade de ter seu lugar de volta em '
              f'Noxus, embora {nome_da_personagem} não saiba disso.'
              f'\nEle propôs a {nome_da_personagem} ensinar a usar seus '
              f'poderes em uma terra desabitada no outro lado do oceano.'
              f'\nA proposta foi aceita pela jovem. Treinar em um lugar '
              f'afastado das pessoas seria perfeito.'
              f'\nDepois de controlar seu poder, ela se tornaria parte '
              f'do exército de Noxus. \n'
              f'\nGrande Tecelã: Mas, {nome_da_personagem} não sabe '
              f'o verdadeiro propósito da missão.\n'
              f'\nGrande Tecelã: Gangplank, seu pequeno exército '
              f'e Taliyah zarparam rumo a Ionia.'
              f'\nDias e noites se passaram, tempestades viram e foram.'
              f'\nPoucas horas antes de chegar ao destino, Gangplank revelou '
              f'a verdade à {nome_da_personagem}.'
              f'\nEla teria que soterrar uma cidade com seu povo dormindo.'
              f'\nGangplank explica que o povo de Ionia já atacou Noxus '
              f'desta mesma maneira.'
              f'\n{nome_da_personagem} se vê sem escolhas, mas tem que tomar uma '
              f'decisão.\n'
              )
        print('=-' * 60)
    elif destino == '2':
        decisao = 'Ionia'
        print('=-' * 60)
        print('IONIA'.center(120))
        print(f'\n{nome_da_personagem}: Dizem que Ionia é um bom lugar para '
              f'se conhecer melhor.Devemos seguir para lá. \n'
              f'\nGrande Tecelã: Então, seguindo seus instintos, '
              f'{nome_da_personagem} rumou em direção a Ionia.'
              f'\nIonia é um local onde muitos magos vão para se conhecer '
              f'melhor.'
              f'\nÉ uma região naturalmente mágica e as pessoas se sentem '
              f'atraída por ela. '
              f'\n{nome_da_personagem} não sabia muito sobre Ionia.'
              f'\nPara chegar em Ionia, {nome_da_personagem} precisa passar '
              f'pelas Florestas Kumungu e suas montanhas invernais.'
              f'\nDizem que essa floresta é abençoada por magia.\n'
              f'\nGrande Tecelã: Ao descansar durante uma tempestade invernal,'
              f' {nome_da_personagem} começa a brincar com seus poderes.'
              f'\nA brincadeira foi se tornando algo grande e incontrolável. '
              f'{nome_da_personagem} queria parar mas seus poderes '
              f'não a obedeciam. '
              f'\nSem querer, ela inicia uma avalanche mas consegue parar.'
              f'\nEntretanto, ela não sabe que havia alguém perto...\n'
              f'\nHomem desconhecido: SOCORRO! ALGUÉM ME AJUDA!'
              f'\n{nome_da_personagem}: (ouvindo um ruído longe)'
              f'\n{nome_da_personagem}: Acho que estou ouvindo alguém.\n'
              f'\nGrande Tecelã: {nome_da_personagem} descobre que '
              f'machucou alguém. '
              f'\nO nome desse homem é Yasuo. Ele é um espadachin ioniano.'
              f'\nSua habilidade com a espada transcende a linha entre '
              f'o físico e a magia. '
              f'\nEle sabe como controlar o vento '
              f'através de seus golpes com a espada. \n'
              f'\nGrande Tecelã: {nome_da_personagem} cuida dele '
              f'até a tempestade '
              f'passar e os dois contam suas histórias.'
              f'\nYasuo se sensibiliza com a história de {nome_da_personagem} '
              f'e decide ensiná-la a controlar seus poderes.\n'
              f'\nGrande Tecelã: Alguns dias se passaram '
              f'e {nome_da_personagem} aprendeu um pouco com seu mestre. '
              f'\nYasuo diz a sua aprendiz que precisam ir ao Placídio '
              f'de Navori para ele apresentá-la a Karma.'
              f'\nKarma é a maior entidade espiritual de Ionia. '
              f'Ela iria auxiliar {nome_da_personagem} em sua jornada de '
              f'autoconhecimento.'
              f'\n{nome_da_personagem} fica pensativa na proposta e pensa '
              f'bastante antes de respondê-lo.\n'
              )
        print('=-' * 60)
    return decisao


def segunda_decisao(resultado_decisao_local, nome_da_personagem):
    # Essa função tem como objetivo dar ao usuário as opções
    # de acordo com a primeira decisão realizada,
    # retorna o valor "acao" para ser usado em outras funções
    # E executa a função da história de acordo com a escolha
    acao = ''
    if resultado_decisao_local == 'Noxus':
        acao = str(input(f'{nome_da_personagem}: O que devemos fazer? '
                         '\nDigite [1] para soterrar a cidade '
                         'e [2] para não soterrar: ')).strip()
        while acao != '1' and acao != '2':
            acao = str(input(f'\nVocê digitou "{acao}". Por favor, '
                             f'tente novamente com uma opção válida.'
                             f'\nDigite [1] para soterrar a cidade '
                             f'e [2] para não soterrar: ')).strip()
        print('=-' * 60)
        if acao == '1':
            historia_noxus_primeiro_fluxo(nome_da_personagem)
        elif acao == '2':
            historia_noxus_segundo_fluxo(nome_da_personagem)

    elif resultado_decisao_local == 'Ionia':
        acao = str(input(f'{nome_da_personagem}: O que devemos fazer?'
                         f'\nDigite [1] para seguir com Yasuo e '
                         f'[2] para seguir jornada sozinha: ')).strip()
        while acao != '1' and acao != '2':
            acao = str(input(f'\nVocê digitou "{acao}". Por favor, '
                             f'tente novamente com uma opção válida.'
                             f'\nDigite [1] para seguir com Yasuo '
                             f'e [2] para seguir jornada sozinha: ')).strip()
        print('=-' * 60)
        if acao == '1':
            historia_ionia_primeiro_fluxo(nome_da_personagem)
        elif acao == '2':
            historia_ionia_segundo_fluxo(nome_da_personagem)
    else:
        print('Você deveria corrigir algo')
    return acao


def historia_noxus_primeiro_fluxo(nome_do_personagem):
    print(f'\nGrande Tecelã: {nome_do_personagem} decide seguir as '
          f'ordens de Gangplank, mas somente aceita por medo de '
          f'sofrer consequências. '
          f'\nQuando chegam em Ionia, {nome_do_personagem} tenta destruir a '
          f'cidade, mas não consegue.'
          f'\nSeus poderes não estão respondendo a seus comandos. '
          f'De fato, ela veio para aprender a controlá-los.'
          f'\nO máximo que ela consegue é mexer em algumas pedras no chão '
          f'e nos morros e montanhas em volta. \nTalvez tenha assustado '
          f'algum cidadão.\n'
          f'\nGrande Tecelã: Gangplank decide cancelar a missão. '
          f'\nDepois da tentativa falha de {nome_do_personagem}, ele não tem '
          f'mais coragem de fazer por si próprio, \nou mandar seu exército '
          f'fazer por ele.'
          f'\nGangplank não é uma pessoa má, somente conheceu as pessoas '
          f'erradas, nas hora erradas \ne acabou fazendo coisas erradas. '
          f'{nome_do_personagem} consegue ver isso.\n\n...\n'
          f'\nGrande Tecelã: A tripulação está pronta para viajar de volta à '
          f'Noxus. \n{nome_do_personagem} conversam brevemente '
          f'antes de zarpar.\n'
          f'\nGangplank: {nome_do_personagem}, não tenho como te ajudar '
          f'com seus poderes. '
          f'\nSe você voltar a Noxus comigo, você não será ninguém.'
          f'\nÉ difícil ser uma mulher naquele lugar.'
          f'\n{nome_do_personagem}: Imagino que sim.'
          f'\nGangplank: Mas eu não voltarei à Noxus.'
          f'\nMinha tripulação rumará à Águas de Sentina. Uma região '
          f'litorânea que reúne muitos piratas, caçadores de tesouro '
          f'e afins. '
          f'\nJá tenho meu pequeno exército e um navio, então tenho o '
          f'necessário.'
          f'\nGangplank: Você gostaria de vir comigo?'
          f'\nGangplank: Talvez alguém lá possa te ajudar.'
          f'\nGangplank: De qualquer forma, em Ionia há pessoas como você.'
          f'\nGangplank: Talvez seja melhor ficar. '
          f'\nGangplank: Você decide.\n\n...\n'
          f'\nGrande Tecelã: Então, {nome_do_personagem} deve escolher entre '
          f'ir com Gangplank ou ficar em Ionia.\n'
          )
    print('=-' * 40)


def historia_noxus_segundo_fluxo(nome_do_personagem):
    print(f'\nGrande Tecela: {nome_do_personagem} decide se negar a usar '
          f'seus poderes para praticar esse genocídio.'
          f'\nEla comunica isso ao capitão. '
          f'Gangplank apenas concorda com sua escolha.\n'
          f'\nGrande Tecelã: Ao anoitecer, {nome_do_personagem} foi deitar '
          f'e adormeceu.'
          f'\nEla acorda rapidamente, assustada. Ela percebe que os '
          f'soldados de Gangplank estão a carregando.'
          f'\nEla tenta se soltar porém está completamente amarrada. \n\n...\n'
          f'\n{nome_do_personagem}: O que estão fazendo?'
          f'\n{nome_do_personagem}: ME SOLTEM!'
          f'\nGangplank: (se aproxima rindo)'
          f'\nGangplank: Desculpe {nome_do_personagem}, aqui neste navio '
          f'não possúimos vagas para mulheres fracas. '
          f'\nGangplank: Joguem ela ao mar. \n\n... \n... \n...\n'
          f'\nGrande Tecelã: {nome_do_personagem} foi jogada ao mar. '
          f'\nNum momento de desespero, ela começa a gritar por socorro, '
          f'já se afogando.'
          f'\nInvoluntariamente, seus poderes começam a agir. '
          f'\nSeus poderes conseguem controlar uma pedra com o dobro do '
          f'tamanho dela para levá-la a superfície.\n'
          f'\nGrande Tecelã: Com o auxílio de seu poder e nadando um pouco '
          f'ela consegue chegar a areia. '
          f'\nUm homem com uma espada na cintura passa perto e a vê.\n\n...\n'
          f'\nHomem desconhecido: Você parece exausta, está tudo bem?'
          f'\n{nome_do_personagem}: Sim, eu estava nadando e quase me afoguei.'
          f'\nHomem desconhecido: Para uma jovem da sua idade, você mente bem.'
          f'\n\n... \n'
          f'\nGrande Tecelã: {nome_do_personagem} então decide contar sua '
          f'jornada para o homem desconhecido. \nSeu nome é Yasuo. '
          f'Ele é um espadachin ioniano.'
          f'\nEle diz que pode ajudá-la com seu dom e que em Ionia há outras '
          f'pessoas como ela.'
          f'\nKarma, a maior entidade espiritual de Ionia poderia ajudá-la '
          f'nessa jornada de autoconhecimento.\n\n...\n'
          f'\nYasuo: Posso te levar ao Placídio de Navori e lá treinaremos '
          f'seu dom.'
          f'\nYasuo: Mas, se não quiser minha ajuda, pode ir ao Monte Targon '
          f'e você conseguirá algumas respostas com os Solari.'
          f'\nYasuo: Alguns Solaris são magos como você. '
          f'Eles são um grupo religioso '
          f'que cultua o sol. \n\n...\n'
          f'\nGrande Tecelã: {nome_do_personagem} se mostra meio receosa com '
          f'uma nova ajuda, mas ela sabe que precisa de alguém para guiá-la.\n'
          f'\nGrande Tecelã: Então, {nome_do_personagem} tem que tomar '
          f'uma decisão:'
          f'\nIr com Yasuo conhecer Karma ou ir ao Monte Targon conhecer os '
          f'Solari.'
          )
    print('=-' * 60)


def terceira_decisao_noxus(escolha_primeira_decisao, escolha_segunda_decisao, nome_do_personagem):
    destino = ''
    if escolha_primeira_decisao == 'Noxus':
        if escolha_segunda_decisao == '1':
            destino = str(input(f'{nome_do_personagem}: Para onde '
                                f'devemos ir?'
                                f'\nDigite [1] para ir a Águas de Sentina e '
                                f'[2] para seguir em Ionia: ')).strip()
            while destino != '1' and destino != '2':
                destino = str(input(f'\nVocê digitou "{destino}". '
                                    f'Por favor, tente novamente com uma opção válida.'
                                    f'\nPara onde devemos ir?'
                                    f'\nDigite [1] para ir a Águas de Sentina e '
                                    f'[2] para seguir em Ionia: ')).strip()
            print('=-' * 60)
            if destino == '1':
                destino = 'Águas de Sentina'
            elif destino == '2':
                destino = 'Ionia'

        elif escolha_segunda_decisao == '2':
            destino = str(input(f'{nome_do_personagem}: Para onde devemos ir?'
                                f'\nDigite [1] para ir ao Monte Targon e '
                                f'[2] para seguir ao Placídio de Navori: ')).strip()
            while destino != '1' and destino != '2':
                destino = str(input(f'\nVocê digitou "{destino}". '
                                    f'Por favor, tente novamente com uma opção válida.'
                                    f'\nPara onde devemos ir?'
                                    f'\nDigite [1] para ir ao Monte Targon e '
                                    f'[2] para seguir ao Placídio de Navori: ')).strip()
            print('=-' * 60)
            if destino == '1':
                destino = 'Monte Targon'
            elif destino == '2':
                destino = 'Placídio de Navori'
    return destino


def terceira_decisao_ionia(escolha_primeira_decisao, escolha_segunda_decisao, nome_do_personagem):
    destino = ''
    if escolha_primeira_decisao == 'Ionia':
        if escolha_segunda_decisao == '1':
            destino = str(input(f'\n{nome_do_personagem}: Para onde devemos ir?'
                                f'\nDigite [1] para seguir no Placídio de Navori'
                                f' e '
                                f'[2] para ir a Águas de Sentina: ')).strip()
            while destino != '1' and destino != '2':
                destino = str(input(f'\nVocê digitou "{destino}". '
                                    f'Por favor, tente novamente com uma '
                                    f'opção válida.'
                                    f'\nPara onde devemos ir?'
                                    f'\nDigite [1] para seguir no Placídio '
                                    f'de Navori e '
                                    f'[2] para ir a Águas de Sentina: ')).strip()
            print('=-' * 60)
            if destino == '1':
                destino = 'Placídio de Navori'
            elif destino == '2':
                destino = 'Águas de Sentina'
        elif escolha_segunda_decisao == '2':
            destino = str(input(f'{nome_do_personagem}: Para onde devemos ir?'
                                f'\nDigite [1] para seguir ao Monte Targon e '
                                f'[2] para ir a Águas de Sentina: ')).strip()
            while destino != '1' and destino != '2':
                destino = str(input(f'\nVocê digitou "{destino}". '
                                    f'Por favor, tente novamente com uma opção válida.'
                                    f'\nPara onde devemos ir?'
                                    f'\nDigite [1] para seguir ao Monte Targon e '
                                    f'[2] para  a Águas de Sentina: ')).strip()
            print('=-' * 60)
            if destino == '1':
                destino = 'Monte Targon'
            elif destino == '2':
                destino = 'Águas de Sentina'
    print(destino)
    return destino


def terceira_decisao_escolha(decisao_um, decisao_dois, nome_do_personagem):
    resultado_decisao_tres = ''
    if decisao_um == 'Noxus':
        resultado_decisao_tres = terceira_decisao_noxus(decisao_um, decisao_dois, nome_do_personagem)
    elif resultado_primeira_decisao == 'Ionia':
        resultado_decisao_tres = terceira_decisao_ionia(decisao_um, decisao_dois, nome_do_personagem)
    return resultado_decisao_tres


def historia_ionia_primeiro_fluxo(nome_da_personagem):
    print(f'\nGrande Tecelã: {nome_da_personagem} decide seguir com Yasuo '
          f'para o Placídio. {nome_da_personagem} finalmente conhece Karma.'
          f'\n\n...\n'
          f'\nKarma: É um prazer conhecê-lá {nome_da_personagem}. '
          f'\nKarma: Sabia que você viria.'
          f'\n{nome_da_personagem}: (como ela sabia que eu viria?)'
          f'\n{nome_da_personagem}: O prazer é todo meu.'
          f'\nKarma: Sei que têm passado por período tempestuoso, espero '
          f'que possa ajudá-la na sua jornada.\n\n...\n'
          f'\nGrande Tecelã: {nome_da_personagem} passa um tempo no Placídio '
          f'treinando com Karma e Yasuo. '
          f'\nEla já consegue controlar as pedras a sua maneira.'
          f'\nO equilíbrio entre o treino espiritual e prático estão sendo '
          f'fundamentais para que ela alcance seu objetivo.\n'
          f'\nGrande Tecelã: Karma conta para ela que ao redor do mundo '
          f'existem muitas outras pessoas como ela.'
          f'\nEssas pessoas geralmente são rejeitadas pelos seus '
          f'semelhantes ou usadas para fins maiores, como a guerra.'
          f'\nMuitos magos escolhem o lado mais fácil da aceitação, e viram '
          f'armas de guerra usados pelos reinos em suas sangrentas batalhas.'
          f'\nOutros, para serem aceitos, juram que nunca mais iriam utilizar '
          f'magia. '
          f'\nAté procuram outras pessoas que dizem ter a cura para anular '
          f'a magia dentro si.\n'
          f'\nGrande Tecelã: Na contramão desses casos, temos o caso de '
          f'{nome_da_personagem}.'
          f'\nEla foi rejeitada, mas queria entender o que estava '
          f'dentro de si.'
          f'\nE ela buscou ajuda para auxiliá-la em sua jornada de '
          f'autoconhecimento.\n\n\n... \n'
          f'\nGrande Tecelã: Depois de algum tempo, {nome_da_personagem} '
          f'já se sente preparada para continuar sua jornada sozinha.'
          f'\nEmbora não controle seus poderes em 100% e seja muito '
          f'agradecida a Karma e Yasuo, \nela sente que precisa conhecer o '
          f'mundo em sua volta. '
          )
    print('=-' * 40)


def historia_ionia_segundo_fluxo(nome_da_personagem):
    print('=-' * 40)
    print(f'\nGrande Tecelã: {nome_da_personagem} segue sua jornada sozinha.'
          f'\nEla decide ir em direção ao Monte Targon.'
          f'\nO Monte Targon é conhecido como um monte onde '
          f'só os mais fortes conseguem subir no topo.\n'
          f'\nGrande Tecelã: {nome_da_personagem} meio que se sente atraída '
          f'por essa terra. Ela sente que deve ir para lá.\n'
          f'\nGrande Tecelã: Durante o caminho, {nome_da_personagem} encontra '
          f'um acampamento. \nHavia um homem em frente a fogueira.'
          f'\nEla decide parar e perguntar sobre o Monte.\n\n... \n'
          f'\n{nome_da_personagem}: Senhor...?'
          f'\nHomem desconhecido: Pois não...?'
          f'\n{nome_da_personagem}: Eu preciso ir ao Monte Targon, '
          f'estou indo na direção correta?'
          f'\nHomem desconhecido: O que uma jovem shurimane quer fazer '
          f'no Monte Targon?'
          f'\nHomem desconhecido: Lá é um lugar para homens extremamente '
          f'fortes.'
          f'\n{nome_da_personagem}: A terra me chama. Devo responder '
          f'ao chamado.'
          f'\n{nome_da_personagem}: Não preciso ser homem para subir uma '
          f'montanha.'
          f'\nHomem desconhecido: Não lhe subestimei, minha jovem. '
          f'\nHomem desconhecido: É um local muito perigoso. '
          f'\nAphelios: Não me apresentei, meu nome é Aphelios.'
          f'\nAphelios: Sou da tribo Solari.'
          f'\n{nome_da_personagem}: (Solari... aqueles que cultuam o sol? '
          f'\n{nome_da_personagem}: {nome_da_personagem}.'
          f'\nAphelios: Você está no caminho certo.'
          f'\nAphelios: No topo da montanha, os Solari se reúnem.'
          f'\nAphelios: Estou indo para lá. '
          f'\nAphelios: Pode me acompanhar se quiser.'
          f'\n{nome_da_personagem}: (será que devo?)'
          f'\n{nome_da_personagem}: Taaalvez...'
          f'\nAphelios: Sinto algo diferente em você... '
          f'\nAphelios: Você é...uma maga?'
          f'\n{nome_da_personagem}: ...'
          f'\n{nome_da_personagem}: (como ele sabe?)'
          f'\n{nome_da_personagem}: Ahn... Sim. Descobrindo meus poderes.'
          f'\nAphelios: No topo da montanha há grandes revelações para '
          f'pessoas como você.'
          f'\nAphelios: Venha comigo.\n'
          f'\nGrande Tecelã: {nome_da_personagem} fica pensativa com o que '
          f'Aphelios disse. \nNão sabe se deve acompanhá-lo ou desistir e ir '
          f'para outro lugar.'
          f'\nTalvez desistir de tudo e ir a Águas de Sentina, '
          f'onde os piratas '
          f'e mercenários se encontram não seja uma má ideia.'
          f'\nTrocar a pedra pelo mar talvez faça mais sentido.'
          )
    print('=-' * 40)


def final_do_jogo(decisao_um, decisao_dois, decisao_tres, nome_da_personagem):
    if decisao_um == 'Noxus':
        condicoes_final_jogo_noxus(decisao_dois, decisao_tres, nome_da_personagem)
    elif decisao_um == 'Ionia':
        condicoes_final_jogo_ionia(decisao_dois, decisao_tres, nome_da_personagem)
    else:
        print('final_do_jogo corrigir')


def condicoes_final_jogo_noxus(decisao_dois, decisao_tres, nome_da_personagem):
    if decisao_dois == '1' and decisao_tres == 'Águas de Sentina':
        print(f'\nGrance Tecelã: {nome_da_personagem} então se junta '
              f'a Gangplank e ambos vão para Águas de Sentina.'
              f'\nDepois de um tempo, já estabelecidos, {nome_da_personagem} '
              f'vira também uma capitã com seu próprio navio e tripulação. '
              f'\nEla meio que esquece que é uma maga.\n'
              f'\nGrande Tecelã: Certo dia, {nome_da_personagem} estava em '
              f'seu navio e ouviu a conversa de dois de seus tripulantes.'
              f'\n\n...\n'
              f'\nTripulante 1: Você ouviu os boatos vindo de Shurima?'
              f'\nTripulante 2: Boatos sobre o que?'
              f'\nTripulante 1: Dizem que o imperador Azir retornou.'
              f'\nTripulante 2: Isso é impossível.'
              f'\nTripulante 2: Você já tá crescido demais pra acreditar '
              f'nessas mentiras.'
              f'\nTripulante 1: Tenho meus informantes lá.'
              f'\nTripulante 1: Não deve ser mentira. Shurima é um lugar '
              f'cheio de mistérios.\n\n...\n'
              f'\n{nome_da_personagem} não dá liga muito para conversa '
              f'e logo se afasta dos tripulantes.'
              )
        mensagem_perdeu_jogo()
        print(f'\nInfelizmente, {nome_da_personagem} não voltou para casa '
              f'e você não concluiu o objetivo do jogo. ')

    elif decisao_dois == '1' and decisao_tres == 'Ionia':
        print(f'\nGrande Tecelã: {nome_da_personagem} decide seguir em Ionia. '
              f'\nEla acredita que precisa se entender melhor e em Ionia isso '
              f'será possível.'
              f'\nIonia é uma região muito aberta a estrangeiros e um lugar '
              f'naturalmente mágico.'
              f'\nMas pouco se sabe sobre seu povo e cultura.\n'
              f'\nGrande Tecelã: {nome_da_personagem} caminha por dias até '
              f'chegar no Placídio de Navori. \nNo Placídio fica o templo de '
              f'Karma, a maior entitade espiritual de Ionia.'
              f'\nEla acumula o conhecimento de gerações e sempre guia os '
              f'perdidos até o seu objetivo.'
              f'\nKarma aceita guiar {nome_da_personagem} em sua jornada.\n'
              f'\nGrande Tecelã: depois de meses treinando seu espírito '
              f'e praticando seus poderes, {nome_da_personagem} finalmente '
              f'podia respirar aliviada.\n\n...\n'
              f'\nKarma: {nome_da_personagem}, você evoluiu muito desde '
              f'que chegou aqui.'
              f'\n{nome_da_personagem}: Eu não seria nada sem você. '
              f'\n{nome_da_personagem}: Agora eu posso mover montanhas!'
              f'\n{nome_da_personagem}: Isso é incrível!'
              f'\nKarma: Seu dom é uma dádiva, use-o com cautela e para '
              f'coisas boas.'
              f'\n...'
              f'\nKarma: {nome_da_personagem}, preciso te contar uma '
              f'algo importante.'
              f'\nKarma: Acho que você precisa saber.'
              f'\nKarma: Azir retornou.'
              f'\nKarma: Não se sabe qual seu objetivo, mas ele e seu '
              f'exército retornaram a vida.'
              f'\nKarma: {nome_da_personagem}, hora de ir para casa.'
              f'Karma: Você está pronta. '
              f'\n\n...\n'
              f'\nGrande Tecelã: {nome_da_personagem} decide então '
              f'voltar a Shurima, agora uma nova mulher. Uma maga.'
              f'Uma shurimane.'
              )
        mensagem_venceu_jogo()
        print('Parabéns, você concluiu o objetivo do jogo e voltou para casa!')

    elif decisao_dois == '2' and decisao_tres == 'Monte Targon':
        print(f'\nGrande Tecelã: {nome_da_personagem} decide ir ao '
              f'Monte Targon.'
              f'\nNo caminho, ela conhece um Solari chamado Aphelios.'
              f'Ele promete ajudá-la em sua jornada junto com os Solari.'
              f'\nGrande Tecelã: Então {nome_da_personagem} e Aphelios '
              f'sobem o Monte Targon.'
              f'\nPara muitos, a subida levaria meses. Para eles, '
              f'alguns minutos de caminhada. '
              f'\nO monte escolhe quem é digno de subí-lo.'
              f'\nEles se encontram com os outros Solari '
              f'e {nome_da_personagem} é apresentada a todos.'
              f'\nEntre os Solari haviam alguns magos, então não foi '
              f'difícil para ela se identificar com o grupo.\n'
              f'\nGrande Tecelã: Meses depois, {nome_da_personagem} já '
              f'estava fazendo o Monte Targon tremer, literalmente.'
              f'\nSua magia havia alcançado um nível explêndido.'
              f'\nMas {nome_da_personagem} precisava saber de uma coisa.'
              f'\n\n...\n'
              f'\nAphelios: {nome_da_personagem}, preciso te falar algo.'
              f'\nAphelios: Ouvimos rumores de Shurima. '
              f'\nAphelios: Azir retornou.'
              f'\nAphelios: Acredito que você esteja pronta pra isso.'
              f'\nAphelios: {nome_da_personagem}, hora de voltar pra casa.'
              )
        mensagem_venceu_jogo()
        print('Parabéns, você concluiu o objetivo do jogo e voltou para casa!')

    elif decisao_dois == '2' and decisao_tres == 'Placídio de Navori':
        print(f'\nGrande Tecelã: {nome_da_personagem} decide seguir ao '
              f'Placídio de Navori com Yasuo. '
              f'Lá ela conhece Karma. \nKarma e Yasuo vão auxiliar '
              f'{nome_da_personagem} em sua jornada.\n'
              f'\nGrande Tecelã: A jovem passa meses treinando com eles '
              f'mas acaba não evoluindo muito em relação ao seu poder.\n'
              f'Nem mesmo em maturidade. Talvez ela sinta falta de casa.\n'
              f'\nGrande Tecelã: Do outro lado de Valoran, o impossível '
              f'acontece. '
              f'\nAzir e seu exército retornaram. Não se sabe o porquê '
              f'e nem qual objetivo o imperador tem.\n'
              f'\nGrande Tecelã: {nome_da_personagem} não tem notícias de '
              f'Shurima e não aprende a controlar seus poderes. '
              )
        mensagem_perdeu_jogo()
        print(f'\nInfelizmente, {nome_da_personagem} não voltou para casa '
              f'e você não concluiu o objetivo do jogo. ')

    else:
        print('condicoes_final_jogo_noxus corrigir')


def condicoes_final_jogo_ionia(decisao_dois, decisao_tres, nome_da_personagem):
    if decisao_dois == '1' and decisao_tres == 'Placídio de Navori':
        print(f'\nGrande Tecelã: {nome_da_personagem} decide ficar no '
              f'Placídio e treinar por mais um tempo.\n\n...\n'
              f'\nGrande Tecelã: Depois de algum tempo, {nome_da_personagem} '
              f'já consegue fazer coisas incríveis com sua magia.\n\n...\n'
              f'\nKarma: Você dominou a si mesma {nome_da_personagem}, parabéns.'
              f'\n{nome_da_personagem}: Obrigado Karma. Sem vocês isso '
              f'não seria possível. '
              f'\nKarma: Fico feliz em ajudar. '
              f'\nKarma: Tenho que te contar sobre algo.'
              f'\nKarma: Ouvimos boatos de Shurima.'
              f'\nKarma: Parece que o imperador Azir retornou.'
              f'\nKarma: Não sabemos como e nem porquê.'
              f'\nKarma: {nome_da_personagem}, hora de voltar para casa.'
              )
        mensagem_venceu_jogo()
        print('Parabéns, você concluiu o objetivo do jogo e voltou para casa!')

    elif decisao_dois == '1' and decisao_tres == 'Águas de Sentina':
        print(f'\nGrance Tecelã: {nome_da_personagem} decide ir a '
              f' Águas de Sentina.'
              f'\nDepois de um tempo, já estabelecida, {nome_da_personagem} '
              f'vira uma capitã com seu próprio navio e tripulação. '
              f'\nEla meio que esquece que é uma maga.\n'
              f'\nGrande Tecelã: Certo dia, {nome_da_personagem} estava em '
              f'seu navio e ouviu a conversa de dois de seus tripulantes.'
              f'\n\n...\n'
              f'\nTripulante 1: Você ouviu os boatos vindo de Shurima?'
              f'\nTripulante 2: Boatos sobre o que?'
              f'\nTripulante 1: Dizem que o imperador Azir retornou.'
              f'\nTripulante 2: Isso é impossível.'
              f'\nTripulante 2: Você já tá crescido demais pra acreditar '
              f'nessas mentiras.'
              f'\nTripulante 1: Tenho meus informantes lá.'
              f'\nTripulante 1: Não deve ser mentira. Shurima é um lugar '
              f'cheio de mistérios.\n\n...\n'
              f'\n{nome_da_personagem} não dá liga muito para conversa '
              f'e logo se afasta dos tripulantes.'
              )
        mensagem_perdeu_jogo()
        print(f'\nInfelizmente, {nome_da_personagem} não voltou para casa '
              f'e você não concluiu o objetivo do jogo. ')

    elif decisao_dois == '2' and decisao_tres == 'Águas de Sentina':
        print(f'\nGrance Tecelã: {nome_da_personagem} decide ir a '
              f' Águas de Sentina.'
              f'\nDepois de um tempo, já estabelecida, {nome_da_personagem} '
              f'vira também uma capitã com seu próprio navio e tripulação. '
              f'\nEla ainda sentia a terra chamar.\n'
              f'\nGrande Tecelã: Por sorte do destino, ela encontra uma '
              f'maga em Sentina. '
              f'\nEla se chama Nami. Ela consegue controlar a água. '
              f'\n{nome_da_personagem} e Nami passam muito tempo juntas '
              f'e ambas se tornam grandes amigas'
              f'\nDessa amizade entre magas, {nome_da_personagem} consegue '
              f'aprimorar seu controle sobre seu poderes de forma natural.\n'
              f'\nGrande Tecelã: Certo dia, {nome_da_personagem} estava em '
              f'seu navio e ouviu a conversa de dois de seus tripulantes.'
              f'\n\n...\n'
              f'\nTripulante 1: Você ouviu os boatos vindo de Shurima?'
              f'\nTripulante 2: Boatos sobre o que?'
              f'\nTripulante 1: Dizem que o imperador Azir retornou.'
              f'\nTripulante 2: Isso é impossível.'
              f'\nTripulante 2: Você já tá crescido demais pra acreditar '
              f'nessas mentiras.'
              f'\nTripulante 1: Tenho meus informantes lá.'
              f'\nTripulante 1: Não deve ser mentira. Shurima é um lugar '
              f'cheio de mistérios.\n\n...\n'
              f'\nGrande Tecelã: {nome_da_personagem} ouve a conversa e vai '
              f'procurar Nami para conversar.\n\n...\n'
              f'\n{nome_da_personagem}: Será que ele realmente voltou?'
              f'\nNami: Tem essa chance.'
              f'\nNami: Se ele desapareceu e ninguém sabe como, ele pode '
              f'ressurgir da mesma forma.'
              f'\nNami: {nome_da_personagem}, hora de voltar pra casa. '
              )
        mensagem_venceu_jogo()
        print('Parabéns, você concluiu o objetivo do jogo e voltou para casa!')

    elif decisao_dois == '2' and decisao_tres == 'Monte Targon':
        print(f'\nGrande Tecelã: Então {nome_da_personagem} e Aphelios '
              f'sobem o Monte Targon.'
              f'\nPara muitos, a subida levaria meses. Para eles, '
              f'alguns minutos de caminhada. '
              f'\nO monte escolhe quem é digno de subí-lo.'
              f'\nEles se encontram com os outros Solari '
              f'e {nome_da_personagem} é apresentada a todos.'
              f'\nEntre os Solari haviam alguns magos, então não foi '
              f'difícil dela se identificar com o grupo.\n'
              f'\nGrande Tecelã: Meses depois, {nome_da_personagem} não '
              f'havia amadurecido seu poder. Algo não estava certo.'
              f'\nMas ela gostava de estar ali.\n'
              f'\nGrande Tecelã: Aphelios ouviu rumores sobre o retorno'
              f'do imperador Azir em Shurima, mas decide não falar com '
              f'{nome_da_personagem} sobre isso. '
              f'\nGrande Tecelã: Ele sente que ela está feliz com a '
              f'nova família e que ela não está pronta pra voltar. '
              )
        mensagem_perdeu_jogo()
        print(f'\nInfelizmente, {nome_da_personagem} não voltou para casa '
              f'e você não concluiu o objetivo do jogo. ')

    else:
        print('condicoes_final_jogo_ionia corrigir')


def mensagem_perdeu_jogo():
    print('''
                   _____                                                            
                  / ____|                                                           
                 | |  __    __ _   _ __ ___     ___      ___   __   __   ___   _ __ 
                 | | |_ |  / _` | | '_ ` _ \   / _ \    / _ \  \ \ / /  / _ \ | '__|
                 | |__| | | (_| | | | | | | | |  __/   | (_) |  \ V /  |  __/ | |   
                  \_____|  \__,_| |_| |_| |_|  \___|    \___/    \_/    \___| |_|'''
          )


def mensagem_venceu_jogo():
    print('''

                                 __      ___      _                   
                                 \ \    / (_)    | |                  
                                  \ \  / / _  ___| |_ ___  _ __ _   _ 
                                   \ \/ / | |/ __| __/ _ \| '__| | | |
                                    \  /  | | (__| || (_) | |  | |_| |
                                     \/   |_|\___|\__\___/|_|   \__, |
                                                                 __/ |
                                                                |___/       
        ''')


def menu():
    opcao = ''
    escolha = ''
    print('=-' * 60)
    print('Jogar novamente?'.center(120))
    opcao = str(input('\nDigite [1] para Jogar Novamente'
                      '\nDigite [2] para Encerrar Jogo: '))
    while opcao != '1' and opcao != '2':
        opcao = str(input(f'\nVocê digitou {opcao}. Tente novamente.'
                          f'\nDigite [1] para Jogar Novamente'
                          f'\nDigite [2] para Encerrar Jogo: '))
    print('\n')
    if opcao == '1':
        escolha = True

    if opcao == '2':
        escolha = False
        print('Encerrando jogo.')
        print('Obrigado por jogá-lo!')
    return escolha


jogar = True

while jogar:
    boas_vindas()

    nome = selecao_avatar()  # Seleção do personagem

    personagem = escolha_de_personagem(nome)  # Nome do personagem

    explicacao(personagem)  # Explicação do jogo

    introducao(personagem)  # Introdução a história do jogo

    local = escolher_regiao()  # Usário escolhe para qual região ele vai viajar

    resultado_primeira_decisao = primeira_decisao(local, personagem)

    resultado_segunda_decisao = segunda_decisao(resultado_primeira_decisao, personagem)

    resultado_terceira_decisao = terceira_decisao_escolha(resultado_primeira_decisao, resultado_segunda_decisao,
                                                          personagem)

    final_do_jogo(resultado_primeira_decisao, resultado_segunda_decisao, resultado_terceira_decisao, personagem)

    jogar = menu()











