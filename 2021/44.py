

def program():
    orders=[]
    resultWord=""
    plik = open("instrukcje.txt", "r")
    text = plik.read().splitlines()
    plik.close()
    for line in text:
        orders.append(line.split(" "))
    for order, letter in orders:
        if order =="DOPISZ":
            resultWord+=letter
        elif order =="USUN":
            resultWord=resultWord[0:len(resultWord)-1]
        elif order == "ZMIEN":
            resultWord = resultWord[0:len(resultWord) - 1]
            resultWord += letter

        elif order == "PRZESUN":
            for i in range(0,len(resultWord)):
                if(resultWord[i])==letter: #znajdz pierwsze wystapienie litery w słowie
                    resultWord=resultWord[0:i]+ chr((ord(resultWord[i])+1-65)%26+65) + resultWord[i+1:len(resultWord)]
                    break



    print(resultWord)


if __name__ == "__main__":
    program()