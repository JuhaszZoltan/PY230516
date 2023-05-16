from random import randint

szamok:list[int] = []

for _ in range(50):
    rn:int = randint(5, 49) * 2 + 1
    szamok.append(rn)

for i in range(len(szamok)):
    print(szamok[i], end=' ')
    if (i+1) % 10 == 0: print(end='\n')

for szam in szamok:
    if szam == 13:
        print('van benne 13')
        break
else: print('nincs benne 13')

index:int = 0
while index < len(szamok) and szamok[index] != 13:
    index += 1
if i < len(szamok): print('van benne 13')
else: print('nincs benne 13')

if 13 in szamok: print('van benne 13')
else: print('nincs benne 13')

halmaz:set[int] = { 3, 4, 10, 6 }
lista:list[int] = []

for e in halmaz:
    lista.append(e)

lista.sort()
print(halmaz)
print(lista)