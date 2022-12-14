#importaçaoes importadas 
from os import system
from time import sleep
import sys
import random

#utilidades-------------------------------------------------------------------------------------------------------------------------
def clear(): system('cls') #função que limpa a tela do terminal

def valInt(texto): #valInt: função que valida um input int (para menus e opçoes e etc) (use como se fosse um input normal)
    while True:
        try:
            valor = int(input(texto)) #voce insere o texto que quiser exibir antes da chamada de input aqui.
            break
        except ValueError:
            input("Opção inválida. Pressione Enter para tentar novamente... ") 
            continue
    return valor

def dotArt(arquivo): #função que lê arquivos .txt (para ler as dot arts)
    arqTxt = open(f'{arquivo}.txt', 'r', encoding='utf-8')
    print(arqTxt.read())

def animar(frase):
    while True:
        for letra in frase:
            print(letra, end='')
            sys.stdout.flush()
            sleep(0.05)
        break

def falas(txt, nome, fala):
    clear()
    dotArt(txt)
    print(f"{nome}")
    animar(fala)
    input()
    clear()

#check dos itens---------------------------------------------------------------------------------------------------------------
temChave = False
temAmuleto = False
temFlor = False
temPena = False
temCristal = False
temMassa = False
ingredientes = 0
ultimoIngrediente = False

if temFlor == True or temPena == True or temCristal == True or temMassa == True:
    ingredientes += 1

ingredientesFalta = 4 - ingredientes

#sistemas-------------------------------------------------------------------------------------------------------------------------

#lutinha piu piu piu kabum

def sorteAtaque():
    listaDano = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4]
    dadinho = (random.randint(0,19))
    if temAmuleto == False:
        animar('Sua sorte foi: ')
        print(dadinho)
    else:
        dadinho = dadinho + 2
        animar('Sua sorte foi: ')
        print(dadinho)
    sleep(0.05)
    dano = listaDano[dadinho]
    animar('Seu dano foi: ')
    print(dano)
    return dano

#uiui covarde fugir

def sortefuga():
    listafug = [False, True]
    dadinho = (random.randint(0,19))
    if temAmuleto == False:
        animar('Sua sorte foi: ')
        print(dadinho)
    else:
        dadinho = dadinho + 2
        animar('Sua sorte foi: ')
        print(dadinho)
    if dadinho >= 9:
        fug = listafug[1]
    else:
        fug = listafug[0]
    if fug == True:
        animar('Sucesso!')
    else:
        animar('Falha!')
    return fug

def ataquePudim():
    
    pass
def ataqueInimigo(inimigo):

    pass
#menus-------------------------------------------------------------------------------------------------------------------------

def chamarMapaInicial():
    mapaTxt = open("txtes\mapainicial.txt", 'r', encoding='utf-8')
    print(mapaTxt.read())
    while True:
        mapaOpcao = valInt("Insira onde quer ir: ")
        match mapaOpcao:
            case 0:
                animar("Não é hora de voltar ainda!")
                input()
                clear()
                continue
            case 1:
                clear()
                import torre
            case 2:
                animar('Você tem que resgatar o Grande Mago, foco!')
                input()
                clear()
                continue
            case 3:
                animar('Você tem que resgatar o Grande Mago, foco!')
                input()
                clear()
                continue
            case 4:
                animar('Você tem que resgatar o Grande Mago, foco!')
                input()
                clear()
                continue
            case 5:
                animar('Você tem que resgatar o Grande Mago, foco!')
                input()
                clear()
                continue
            case _:
                animar('Opção inválida')
                input()
                clear()
                continue


def chamarMapa():
    while True:
        mapaTxt = open("txtes\mapa.txt", 'r', encoding='utf-8')
        print(mapaTxt.read())
        mapaOpcao = valInt("Insira onde quer ir: ")
        match mapaOpcao:
            case 0:
                if temCristal and temFlor and temMassa and temPena == True:
                    clear()
                    import miauderijo
                else:
                    animar("Não seria legal voltar de patas vazias!")
                    input()
                    clear()     
            case 1:
                animar("Não há mais o que fazer na torre, precisamos dos ingreditentes!")
                input()
                clear()
            case   2:
                if temFlor == False:
                    clear()
                    import floresta
                else:
                    animar('Não há mais o que fazer aqui! ')
                    continue
            case 3:
                if temCristal == False:
                    clear()
                    import mina
                else:
                    animar('Não há mais o que fazer aqui! ')
                    continue
            case 4:
                if temMassa ==  False:
                    clear()
                    import italiano
                else:
                    animar('Não há mais o que fazer aqui! ')
                    continue
            case 5:
                if temAmuleto ==  False:
                    clear()
                    import casa_misteriosa
                else:
                    animar('Não há mais o que fazer aqui! ')
                    continue
            case _:
                animar('Opção inválida')
                input()
                clear()
                continue 

def menu_luta(inimigo, txt): #menu principal quando começam encontros com inimigos
    clear()
    while True:
        dotArt(txt)
        animar(inimigo['chamada'])
        print(f"\n----------------------------------\
        \n1 - Atacar\
        \n2 - Pudim\
        \n3 - Checar Inimigo")
        menuOpcao = valInt("Insira opção: ")
        match menuOpcao:
            case 1:
                while inimigo['hp'] >= 0:
                    animar("Pudim prepara sua espada para um golpe!")
                    input('Pressione Enter para atacar!')
                    sleep(0.25)
                    dano = sorteAtaque()
                    if dano <= 0:
                        animar("Erro crítico! Pudim erra o inimigo!")
                    elif dano >= 4:
                        animar("Acerto crítico! Pudim acerta em cheio!")
                    inimigo['hp'] -= dano
                    animar(f"O HP do {inimigo['nome']} é {inimigo['hp']}!")
                animar('Sucesso!')
                break        
            case 2:
                pudim(inimigo, txt)
            case 3: 
                dotArt(txt)
                print('')
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue


def pudim(inimigo, txt = None): #menu do inventario do pudim
    clear()
    while True:
        dotArt('txtes/pudim')
        print(f"Pudim\
            \n------------------\
            \n1 - Checar o Pudim \
            \n2 - Itens do Pudim\
            \n3 - Retornar")
        menuPudim = valInt("Insira opção: ")
        match menuPudim:
            case 1:
                clear()
                dotArt('txtes/pudim')
                print("Pudim - sobrenome: de Limão\
                    \n-----------------------------\
                    \nHP: 20 - Não deixe chegar a 0\
                    \nForça: 3 - Bem forte, para um gatinho\
                    \nAtaque: 5 - Sua espada é sua maior aliada\
                    \nAgilidade: 6 - Jovem e flexível, um felino admirável")
                if temAmuleto == True:
                    print("Sorte: 10 - Pudim tem certeza que é o gato mais sortudo de Miaudade")
                else:
                    print("Sorte: 8 - Pudim está se sentindo sortudo hoje")
                input()
                continue
            case 2:
                clear()
                print(f"1 - {inventario.espada['nome']}")
                if temChave == True:
                    print("2 - Chave Brilhante")
                if temAmuleto == True:
                    print(f"3 - {inventario.amuleto['nome']}")
                if temFlor == True:
                    print(f"4 - {inventario.flor['nome']}")
                if temPena == True:
                    print(f"5 - {inventario.pena['nome']}")
                if temCristal == True:
                    print(f"6 - {inventario.cristal['nome']}")
                if temMassa == True:
                    print(f"7 - {inventario.massa['nome']}")
                print("Pressione 0 para voltar")
                itemOpcao = valInt("Insira Opção: ")
                clear()
                if itemOpcao == 1:
                    inventario.chamarItem(inventario.espada)
                    continue
                if itemOpcao == 2 and temChave == True:
                    inventario.chamarItem(inventario.chave)
                    continue
                if itemOpcao == 3 and temAmuleto == True :
                    inventario.chamarItem(inventario.amuleto)
                    continue
                if itemOpcao == 4 and temFlor == True:
                    inventario.chamarItem(inventario.flor)
                    continue
                if itemOpcao == 5 and temPena == True:
                    inventario.chamarItem(inventario.pena)
                    continue
                if itemOpcao == 6 and temCristal == True:
                    inventario.chamarItem(inventario.cristal)
                    continue
                if itemOpcao == 7 and temMassa == True:
                    inventario.chamarItem(inventario.massa)
                    continue
                else:
                    continue
            case 3:
                clear()
                menu_luta(inimigo, txt)
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue

class inventario:

    def chamarItem(item):
        dotArt(item['txt'])
        print(f"{item['nome']}\n-----------------------------\n{item['descricao']}")
        input()
    chave = {
        'txt': 'txtes/chave',
        'nome': 'Chave Brilhante',
        'descricao': 'Uma chave dourada e brilhante, difícil de tirar os olhos.'
    }
    espada = {
        'txt':'txtes/espada',
        'nome':'Espada Velha',
        'descricao':'Uma espada enferrujada e antiga.'
    }
    amuleto = { 
        'txt':'txtes/amuleto', 
        'nome': 'Amuleto Misterioso da Sorte',
        'descricao': 'Um amuleto estranho que Pudim conseguiu de uma casa misteriosa.\
                    \nVocê se sente mais sortudo usando ele. Adiciona +2 Sorte'
    }
    flor = {
        'txt':'txtes/flor',
        'nome': 'Flor Ancestral',
        'descricao': 'Uma belissima flor de tempos ancestrais. Emana uma fragância distinta, mas agrádavel.\
                    \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
    }
    pena = {
        'txt':'txtes/pena',
        'nome': 'Pena Suja',
        'descricao': 'Uma pena um pouco suja, retirada da plumagem de um pombo despercebido.\
                    \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
    }
    cristal = {
        'txt':'txtes/cristal',
        'nome': 'Cristal Reluzente',
        'descricao': 'Um cristal encantador que emana uma luz fraca.\
                    \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
    }
    massa = {
        'txt':'txtes/macarrao',
        'nome': 'Massa Sagrada',
        'descricao': 'Uma massa italiana da mais alta qualidade. A obra prima da vida do Doguitaliano.\
                    \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
    }

#inimigos

soldadoRato = {
    'nome': 'Soldado Rato',
    'descricao': 'Um grande e forte soldado rato. Parece que não vão muito com a sua cara.',
    'chamada': 'Um Soldado Rato ergue-se na sua frente! Cuidado Pudim!',
    'atk': 4,
    'hp': 30
}
ratão = {
    'nome': 'Ratão',
    'descricao': 'Um ratazana enorme, tanto para cima quanto pros lados. Parece muito perigosa.',
    'chamada': 'O Ratão pisoteia a frente! Cuidado Pudim!',
    'atk': 6,
    'hp': 40
}

ratãoFinal = {
    'nome': 'Ratão: o Grande Rato',
    'descricao': 'O Ratão retorna. Ele parece nervoso e inspirado, sua força é maior do que antes.',
    'chamada': 'O chão treme sob as patas do Ratão! Muito cuidado Pudim!',
    'atk': 10,
    'hp': 80
}

dinoPlanta = {
    'nome': 'Dinoplanta: a Planta Ancestral',
    'descricao': 'Uma planta carnívora de eras antepassadas. Nos tempos antigos, plantas dinossauro alimentavam-se de felinos.',
    'chamada': 'A Planta Ancestral estica suas vinhas! Muito cuidado Pudim!',
    'atk': 7,
    'hp': 50
}

monstroLago = {
    'nome' : 'Monstro Cristalino: o Protetor das Jóias',
    'descricao': 'Um monstro misterioso que se camufla perfeitamente nas cavernas da mina. Extremamente perigoso.',
    'chamada': 'A olhos do monstro brilham o mesmo azul que cintila dos cristais nas suas costas. Muito cuidado Pudim!',
    'atk': 8,
    'hp': 60
}
