import math

n = int(input('Enter value of N: '))
print(n)
e = int(input('Enter value of E: '))
print(e)


m = input('Enter letters separated by a space: ')
mlist = m.split()
print(mlist)
for i in range(len(mlist)):
	num = ord(mlist[i])-96
	en = (num**e)
	cr = en%n
	if cr > 26:
		cr = cr%26
	yp = cr+96
	print('Encrypted letter: ' + chr(yp))
