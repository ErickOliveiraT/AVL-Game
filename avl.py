from random import randint
import sys
import os
import time

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

def jogar(pre, pos, em, players):
	if players == 1:
		print("\n")
		inicio = time.time()
		pre_ = input("Pré ordem: ")
		pos_ = input("Pós ordem: ")
		em_ = input("Em ordem: ")
		fim = time.time()
		tempo = fim - inicio

		print("\nPré ordem: ", end="")
		if pre == pre_:
			print("Acertou!")
		else:
			print("Errou")

		print("Pós ordem: ", end="")
		if pos == pos_:
			print("Acertou!")
		else:
			print("Errou")

		print("Em ordem: ", end="")
		if em == em_:
			print("Acertou!")
		else:
			print("Errou!")

		print("\nTempo: " + str(tempo) + ' s')

		return tempo
	else: #2 jogadores
		ptos_j1 = 0
		ptos_j2 = 0
		temp_j1 = 0
		temp_j2 = 0

		print("\n")
		inicio = time.time()
		pre_ = input("Pré ordem: ")
		pos_ = input("Pós ordem: ")
		em_ = input("Em ordem: ")
		fim = time.time()
		tempo = fim - inicio

		print("\nPré ordem: ", end="")
		if pre == pre_:
			print("Acertou!")
			ptos_j1 += 1
		else:
			print("Errou")

		print("Pós ordem: ", end="")
		if pos == pos_:
			print("Acertou!")
			ptos_j1 += 1
		else:
			print("Errou")

		print("Em ordem: ", end="")
		if em == em_:
			print("Acertou!")
			ptos_j1 += 1
		else:
			print("Errou!")

		print("\nTempo: " + str(tempo) + ' s')
		temp_j1 = tempo
		print('\n\n')
		pause()

		clear()
		print("Vez do jogador 2:\n")
		pause()

		print("\n")
		inicio = time.time()
		pre_ = input("Pré ordem: ")
		pos_ = input("Pós ordem: ")
		em_ = input("Em ordem: ")
		fim = time.time()
		tempo = fim - inicio

		print("\nPré ordem: ", end="")
		if pre == pre_:
			print("Acertou!")
			ptos_j2 += 1
		else:
			print("Errou")

		print("Pós ordem: ", end="")
		if pos == pos_:
			print("Acertou!")
			ptos_j2 += 1
		else:
			print("Errou")

		print("Em ordem: ", end="")
		if em == em_:
			print("Acertou!")
			ptos_j2 += 1
		else:
			print("Errou!")

		print("\nTempo: " + str(tempo) + ' s')
		temp_j2 = tempo
		print('\n\n')
		pause()

		clear()
		print("\t Resumo da rodada\n")
		print("Pontos do jogador 1: " + str(ptos_j1))
		print("Tempo do jogador 1: " + str(temp_j1) + ' s')
		print("\nPontos do jogador 2: " + str(ptos_j2))
		print("Tempo do jogador 2: " + str(temp_j2) + ' s')

		if ptos_j1 > ptos_j2:
			vencedor = 1
		elif ptos_j1 < ptos_j2:
			vencedor = 2
		elif ptos_j1 == ptos_j2:
			if temp_j1 < temp_j2:
				vencedor = 1
			else: 
				vencedor = 2

		if vencedor == 1:
			print("\nVencedor: Jogador 1")
		else:
			print("\nVencedor: Jogador 2")

		print("\n\n\t O que deseja fazer?\n")
		print(" 1 - Nova rodada")
		print(" 2 - Voltar ao menu")
		print(" 3 - Sair\n")
		op = int(input(" Opção desejada: "))

		if op == 1:
			clear()
			percorrer_2()
		elif op == 2:
			clear()
			menu()
		elif op == 3:
			sys.exit()
		return 0

def carrega1(players):
	pre = '9 6 1 12 11 17'
	pos = '1 6 11 17 12 9'
	em = '1 6 9 11 12 17'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega2(players):
	pre = '24 13 12 9 21 43 36 34 50'
	pos = '9 12 21 13 34 36 50 43 24'
	em = '9 12 13 21 24 34 36 43 50'
	tempo = jogar(pre,pos,em,players)
	return tempo
	
def carrega3(players):
	pre = '37 30 17 16 22 30 46 45 50'
	pos = '16 22 17 30 30 45 50 46 37'
	em = '16 17 22 30 30 37 45 46 50'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega4(players):
	pre = '66 50 14 95 68'
	pos = '14 50 68 95 66'
	em = '14 50 66 68 95'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega5(players):
	pre = '72 9 1 46 12 90 80 700'
	pos = '1 12 46 9 80 700 90 72'
	em = '1 9 12 46 72 80 90 700'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega6(players):
	pre = '25 15 6 1 17 20 18 16 19 30'
	pos = '1 6 20 17 15 26 30 29 28 25'
	em = '1 6 15 17 20 25 26 28 29 30'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega7(players):
	pre = '42 27 17 8 18 33 29 64 49 63 93 99'
	pos = '8 18 17 29 33 27 63 49 99 93 64 42'
	em = '8 17 18 27 29 33 42 49 63 64 93 99'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega8(players):
	pre = '72 31 29 25 69 95 82 103'
	pos = '25 29 69 31 82 103 95 72'
	em = '25 29 31 69 72 82 95 103'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega9(players):
	pre = '85 41 39 44 99 94 102'
	pos = '39 44 41 94 102 99 85'
	em = '39 41 44 85 94 99 102'
	tempo = jogar(pre,pos,em,players)
	return tempo

def carrega10(players):
	pre = '76 59 12 34 64 73 90 86 132 1985'
	pos = '34 12 73 64 59 86 1985 132 90 76'
	em = '12 34 59 64 73 76 86 90 132 1985'
	tempo = jogar(pre,pos,em,players)
	return tempo

def percorrer_1():
	print("\t Observe a árvore e digite as sequências pedidas:\n ")
	
	#Abrindo uma árvore aleatoriamente
	time.sleep(1)
	rd = randint(1,10)
	folder = str(rd)+'.jpg'
	os.system(folder)
	pause()
	
	if rd == 1:
		carrega1(1)
	elif rd == 2:
		carrega2(1)
	elif rd == 3:
		carrega3(1)
	elif rd == 4:
		carrega4(1)
	elif rd == 5:
		carrega5(1)
	elif rd == 6:
		carrega6(1)
	elif rd == 7:
		carrega7(1)
	elif rd == 8:
		carrega8(1)
	elif rd == 9:
		carrega9(1)
	elif rd == 10:
		carrega10(1)
	
	print("\n\n\t O que deseja fazer?\n")
	print(" 1 - Nova rodada")
	print(" 2 - Voltar ao menu")
	print(" 3 - Sair\n")
	op = int(input(" Opção desejada: "))

	if op == 1:
		clear()
		percorrer_1()
	elif op == 2:
		clear()
		menu()
	elif op == 3:
		sys.exit()

def percorrer_2():
	print("Vez do jogador 1:\n")
	print("\t Observe a árvore e digite as sequências pedidas:\n ")
	
	#Abrindo uma árvore aleatoriamente
	time.sleep(1)
	rd = randint(1,10)
	folder = str(rd)+'.jpg'
	os.system(folder)
	pause()
	
	if rd == 1:
		carrega1(2)
	elif rd == 2:
		carrega2(2)
	elif rd == 3:
		carrega3(2)
	elif rd == 4:
		carrega4(2)
	elif rd == 5:
		carrega5(2)
	elif rd == 6:
		carrega6(2)
	elif rd == 7:
		carrega7(2)
	elif rd == 8:
		carrega8(2)
	elif rd == 9:
		carrega9(2)
	elif rd == 10:
		carrega10(2)
	
def balancear_1():
	print("\t Observe a árvore e digite o que se pede:\n ")
	
	#Abrindo uma árvore aleatoriamente
	time.sleep(1)
	rd = randint(1,10)
	folder = 'a'+str(rd)+'.jpg'
	os.system(folder)
	pause()

	flag = 0
	res = input('\nBalanceada? ')
	if res == 'S' or res == 's' or res == 'sim' or res == 'Sim' or res == 'sim' or res == 'yes' or res == 'Yes' or res == 'YES' or res == 'y' or res == 'Y' or res == '1' or res == 'true' or res == 'TRUE' or res == 'True':
		if rd >= 1 and rd <= 5: #Está balanceada
			print('\nCorreto!\n')
		else: #Não está balanceada
			print('\nVocê errou.\n')
	else:
		if rd >= 1 and rd <= 5: #Está balanceada
			print('\nVocê errou.\n')
		else: #Não está balanceada
			print('\nCorreto!\n')
			flag = 1
	
	if flag == 1:
		res = int(input("\nQual é o nó com o grau de equilíbrio mais crítico? "))
		if rd == 6:
			x = 40
		elif rd == 7:
			x = 27
		elif rd == 8:
			x = 28
		elif rd == 9:
			x = 22
		elif rd == 10:
			x = 83
		if res == x:
			print('\nCorreto!\n')
		else:
			print('\nVocê errou.\n')

	print("\n\n\t O que deseja fazer?\n")
	print(" 1 - Nova rodada")
	print(" 2 - Voltar ao menu")
	print(" 3 - Sair\n")
	op = int(input(" Opção desejada: "))

	if op == 1:
		clear()
		balancear_1()
	elif op == 2:
		clear()
		menu()
	elif op == 3:
		sys.exit()

def vouf():
	ptos = 0
	print('\tResponda V ou F para cada afirmativa\n')
	print("As árvores AVL são baseadas nas árvores binárias de busca ", end="")
	res = input()
	if res == 'v' or res == 'V':
		ptos += 1
	print("A inserção no melhor caso tem complexidade O(log n) ", end="")
	res = input()
	if res == 'v' or res == 'V':
		ptos += 1
	print("A inserção no pior caso tem complexidade O(n*log n) ", end="")
	res = input()
	if res == 'f' or res == 'F':
		ptos += 1
	print("O grau de liberdade dos nós a calculado com a formula: altura esquerda - altura direita ", end="")
	res = input()
	if res == 'f' or res == 'F':
		ptos += 1
	print("Ao inserirmos os elementos 10, 5, 20, 25 e 30 a árvore deverá ser balanceada ", end="")
	res = input()
	if res == 'v' or res == 'V':
		ptos += 1
	print("Cada nó armazena uma chave e um ponteiro para seu pai ", end="")
	res = input()
	if res == 'f' or res == 'F':
		ptos += 1
	print("A remoção é recursiva e a inserção é iterativa ", end="")
	res = input()
	if res == 'f' or res == 'F':
		ptos += 1
	print("A árvore AVL pode ser usada também na geometria computacional por ser uma estrutura muito rápida ", end="")
	res = input()
	if res == 'v' or res == 'V':
		ptos += 1
	print("Embora sejam rápidas, as árvores AVL são tão rápidas para buscas quanto as Rubro-Negras ", end="")
	res = input()
	if res == 'f' or res == 'F':
		ptos += 1
	print("O balanceamento é feito por meio de rotações ", end="")
	res = input()
	if res == 'v' or res == 'V':
		ptos += 1

	print("\nAcertos: " + str(ptos) + "/10")

	print("\n\n\t O que deseja fazer?\n")
	print(" 1 - Nova rodada")
	print(" 2 - Voltar ao menu")
	print(" 3 - Sair\n")
	op = int(input(" Opção desejada: "))

	if op == 1:
		clear()
		vouf()
	elif op == 2:
		clear()
		menu()
	elif op == 3:
		sys.exit()

def menu():
	print("\t Selecione o modo de jogo\n")
	print(" 1 - Percorrendo árvores (1 player)")
	print(" 2 - Percorrendo árvores (2 players)")
	print(" 3 - Equilíbrio de árvores AVL")
	print(" 4 - Verdadeiro ou falso")
	print(" 5 - Sair\n")
	op = int(input(" Opção desejada: "))

	if op == 1:
		clear()
		percorrer_1()
	elif op == 2:
		clear()
		percorrer_2()
	elif op == 3:
		clear()
		balancear_1()
	elif op == 4:
		clear()
		vouf()
	elif op == 5:
		sys.exit()

menu()