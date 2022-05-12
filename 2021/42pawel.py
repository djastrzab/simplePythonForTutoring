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


aktualny_rodzaj=None
rodzaj2=None
dlugosc_rodzaju=0
dlugosc_maksymalnego_rodzaju=0

for rodzaj in polecenia:
    if aktualny_rodzaj==rodzaj:
        dlugosc_rodzaju+=1
        if dlugosc_rodzaju>dlugosc_maksymalnego_rodzaju:
            dlugosc_maksymalnego_rodzaju=dlugosc_rodzaju
            rodzaj2=rodzaj
    if not aktualny_rodzaj == rodzaj:
        aktualny_rodzaj=rodzaj
        dlugosc_rodzaju=1
