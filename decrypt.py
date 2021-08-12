import math

n = int(input('Enter value of N: '))
print(n)
d = int(input('Enter value of D: '))
print(d)

m = input('Enter encrypted letters separated by a space: ')
mlist = m.split()

for i in range(len(mlist)):
	num = ord(mlist[i])-96
	if num == 1:
		num = 27
	de = (num**d)
	cr = de%n
	yp = cr+96
	print('Encrypted letter: ' + chr(yp))
