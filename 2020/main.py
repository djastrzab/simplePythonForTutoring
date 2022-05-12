
def sprawdz_czy_pierwsza(pierwsze,liczba):
    flag=0
    for pierwsza in pierwsze:
        if(liczba%pierwsza==0):
            flag=1
    if flag==0:
        pierwsze.append(liczba)

def szukaj_sumy(pierwsze,parzysta):
    res=[]
    for pierwsza1 in pierwsze:
        for pierwsza2 in pierwsze:
            if pierwsza1+pierwsza2==parzysta:
                return {pierwsza1,pierwsza2}




liczby=[]
parzyste=[]
pierwsze=[]
sumy=[]
result=[]

plik = open("pary.txt", "r")
tekst=plik.read().splitlines()

plik.close()

for w in tekst:
    l=int(w.split(" ")[0])
    liczby.append(l)

for p in liczby:
    if p%2==0:
        parzyste.append(p)
print(parzyste)
for i in range(2,100):
    sprawdz_czy_pierwsza(pierwsze,i)
print(pierwsze)
for parzysta in parzyste:
    tmp=szukaj_sumy(pierwsze,parzysta)
    sumy.append({parzysta,tmp})
print(sumy)







