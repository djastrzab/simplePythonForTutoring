

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
            for char in resultWord:
                if char == letter:
                    char=chr((ord(char)+1-65)%26+65)
                    break

    print(len(resultWord))



if __name__ == "__main__":
    program()