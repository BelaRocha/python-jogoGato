#menu inicial

from time import sleep
import sys
import data

data.clear()

def animar():
	while True:
		for letra in frase:
			print(letra, end='')
			sys.stdout.flush()
			sleep(0.08)
		break

data.dotArt('txtes/pata')
sleep (1.0)
print(' _______  __                   __            __\n|   |   ||__|.---.-..--.--..--|  |.---.-..--|  |.-----.\n|       ||  ||  _  ||  |  ||  _  ||  _  ||  _  ||  -__|\n|__|_|__||__||___._||_____||_____||___._||_____||_____|')
sleep(0.5)
option= int(input('\n \n      1- Jogar            2- Creditos\n                    '))
data.clear()
while True:
    match option:
        case 1:
            frase = '   Os gatos viviam felizes há muito tempo em Miaudade, onde tinham comida e camas quentinhas para dormirem o dia todo. Um dia, os soldados do Rato Reiqueijão \ninvadiram e ocuparama cidade, expulsando todos os gatos. O Rei Rato sabia que o único felino que poderia tira-lo do poder era o Mago Bola de Pelos e então, por medo, ele o aprisionou em uma torre perto da Floresta Macabra. Os gatos felizmente conseguiram  construir um esconderijo não muito longe da cidade, onde também tinham camas quentinhas, por isso muitos gatos perderam a vontade de lutar e decidiram continuar se escondendo...'
            animar()
            data.clear()
            import inicio
        case 2:
            frase = 'Feito por Izabela e Álvaro'
            animar()
            continue