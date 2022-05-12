polecenia = []
litery = []

plik = open("instrukcje.txt", "r")
tekst = plik.read().splitlines()

plik.close()

for w in tekst:
    p = (w.split(" ")[0])
    polecenia.append(p)

for z in tekst:
    l = (z.split(" ")[1])
    litery.append(l)

# zad 4.1
dlugosc = 0
for pol in polecenia:
    if pol == "DOPISZ":
        dlugosc += 1
    elif pol == "USUN":
        dlugosc -= 1

print("zad 4.1", dlugosc)

# zad 4.2
rodzaj1 = None
rodzaj2 = None
dlugosc_rodzaju = 0
dlugosc_rodzaju1 = 0

for rodzaj in polecenia:
    if rodzaj1 == rodzaj:
        dlugosc_rodzaju += 1
        if dlugosc_rodzaju > dlugosc_rodzaju1:
            dlugosc_rodzaju1 = dlugosc_rodzaju
            rodzaj2 = rodzaj
    if not rodzaj1 == rodzaj:
        rodzaj1 = rodzaj
        dlugosc_rodzaju = 1
        continue

print("zad 4.2", rodzaj2, ":", dlugosc_rodzaju1)

# zad 4.3
litera1 = None
powtorzenia = 0
n = 0
for polecenie in polecenia:
    if polecenie == "DOPISZ":
        for litera in litery:
            if litera == litera[n]:
                powtorzenia += 1
                litera1 = litera
                n += 1
            if not litera == litera[n]:
                powtorzenia = 1

print("zad 4.3", litera1, powtorzenia)