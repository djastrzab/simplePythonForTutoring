

def program():
    orders=[]
    numOfLetters=[]
    maxNumOfLetter=0
    tmp=0
    maxLetter=""
    for i in range(0,26):
        numOfLetters.append(0)

    #print(numOfLetters)
    plik = open("instrukcje.txt", "r")
    text = plik.read().splitlines()
    plik.close()



    for line in text:
        orders.append(line.split(" "))
    #print(orders)
    for order, letter in orders:
        if order =="DOPISZ":
            numOfLetters[ord(letter)-65]+=1

    for i in range(0, 26):
        tmp=numOfLetters[i]
        if(tmp>maxNumOfLetter):
            maxNumOfLetter=tmp
            maxLetter=chr(i+65)

    print([maxNumOfLetter,maxLetter])



if __name__ == "__main__":
    program()