import random
try:
	from colorama import Fore,Style
except ModuleNotFoundError:
	print('Please install the colorama module')
	print('pip install colorama')
	quit()
from time import time

def RPS():
	draws = 0
	wins = 0
	loses = 0

	choices = 'RPS'
	losing_caes = ['RP','RS','SP']
	start = time()
	try:
		t = int(input(Fore.YELLOW+'How many times you would like to play : '+Style.RESET_ALL))
	except ValueError:
		print('Please enter a valid integer > 0')
		quit()
	try:
		for _ in range(t):
			while True:
				c = input(Fore.YELLOW+'Choose [R]ock [P]aper [S]cissors : '+Style.RESET_ALL).upper()
				if len(c) == 0 or c not in choices:
					continue
				else:
					break
			bot = random.choice(choices)
			tmp = bot+c
			if c == bot:
				print(Fore.BLUE+'DRAW'.center(25,'~')+Style.RESET_ALL)
				draws += 1
			elif tmp in losing_caes:
				print(Fore.RED+'YOU LOST :('.center(25,'~')+Style.RESET_ALL)
				loses += 1
			else:
				print(Fore.GREEN+'YOU WON :)'.center(25,'~')+Style.RESET_ALL)
				wins +=  1
	except KeyboardInterrupt:
			print(Style.BRIGHT+Fore.LIGHTWHITE_EX+'\nCome Back Later :) !')
	print(Fore.LIGHTMAGENTA_EX+'\nSTATS :'+Style.RESET_ALL)
	print(Fore.LIGHTCYAN_EX+f'### You Played {t} times ###\nYour winning percentage is {(wins*100)/t}%\nYou Lost {loses} games\nwith {draws} draws'+Style.RESET_ALL)
	print(Fore.LIGHTRED_EX+f'Your session lasted {int(time()-start)} seconds'+Style.RESET_ALL)
RPS()
