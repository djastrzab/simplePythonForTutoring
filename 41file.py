import math

liczby=[]
parzyste=[]
pierwsze=[2,3]
pary=[]


plik = open("pary.txt", "r")
tekst=plik.read().splitlines()


for w in tekst:
    l=int(w.split(" ")[0])
    liczby.append(l)

#print(liczby)

for p in liczby:
    if p%2==0:
        parzyste.append(p)

print(parzyste)

def czy_pierwsza(pierwsze,liczba):
    flaga=0
    for pierwsza in pierwsze:
        if(liczba%pierwsza==0):
            flaga=1
    if flaga==0:
        pierwsze.append(liczba)

for i in range(2,100):
    czy_pierwsza(pierwsze,i)

print(pierwsze)

def goldbach(parzysta):
    p1=2
    for p1 in pierwsze:
        for p2 in pierwsze:
            if p1+p2==parzysta:
                return (parzysta,p1,p2)

for p in parzyste:
    pary.append(goldbach(p))
print(pary)
plik.close()