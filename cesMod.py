en_alf = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
ru_alf = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)]
alf = 0

while alf != 1 and alf != 2:
	alf = int(input('For englshi press : 1\nЕсли хотите продолить на русском нажмите: 2\n'))

if alf == 1:
	alf, m = en_alf, 26
	word = input('Write a word: ')
elif alf == 2:
	alf, m = ru_alf, 32
	word = input('Введите слово: ')

def shifr(word, alf):
	for q in word.split():
		k = len([i for i in q if i.isalpha()])
		for i in q:
			if i not in alf:
			 	print(i, end = '')
			if i in alf:
				if i == i.upper():
					print(alf[((alf.index(i) + k) % m) + m], end = '')
				else:
					print(alf[(alf.index(i) + k) % m], end = '')	
		print(' ', end = '')
shifr(word, alf)