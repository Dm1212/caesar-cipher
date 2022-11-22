en_alf = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
ru_alf = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)]

# alf = int(input())

# if alf == 1:
# 	alf, m = en_alf, 26
# else:
# 	alf, m = ru_alf, 32

cmd = 'Day, mice. "Year" is a mistake!'

# for i in cmd.split():
# 	for k in i:
# 		if k not in alf:
# 			print(k, end = '')
# 		if k in alf:
# 			if k == k.upper():
# 				print(alf[((alf.index(k) + len(i)) % m) + m], end = '')
# 			else:
# 				print(alf[(alf.index(k) + len(i)) % m], end = '')

for i in cmd.split():
	i = i.split()
	print(len(i)