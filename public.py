import math

p = int(input('Enter value of p: '))
print(p)

q = int(input('Enter value of q: '))
print(q)

n = p*q
print('Value of n = ' + str(n))

z = (p-1)*(q-1)
print('Value of z = ' + str(z))

elist = []
dlist = []

for i in range(1, n): 
    if math.gcd(i, z) == 1:
        elist.append(i)

print('Possible Values of E')
print(elist)
print()
print('Possible values of D based on E chosen')

for y in range(0, len(elist)):
    for x in range(1, 21):
        if ((elist[y]*x)-1)%z == 0:          
            dlist.append(x)
    print('E: ' + str(elist[y]))
    
    print(dlist)
    dlist.clear()
