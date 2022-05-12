polecenia=[]
litery=[]

plik=open("instrukcje.txt", "r")
tekst=plik.read().splitlines()

plik.close()

for w in tekst:
    p=(w.split(" ")[0])
    polecenia.append(p)

for z in tekst:
    l=(z.split(" ")[1])
    litery.append(l)


rodzaj1=None
rodzaj2=None
dlugosc_rodzaju=0
dlugosc_rodzaju1=0

for rodzaj in polecenia:
    if rodzaj1==rodzaj:
        dlugosc_rodzaju+=1
        if dlugosc_rodzaju>dlugosc_rodzaju1:
            dlugosc_rodzaju1=dlugosc_rodzaju
            rodzaj2=rodzaj
    if not rodzaj1==rodzaj:
        rodzaj1=rodzaj
        dlugosc_rodzaju=1
