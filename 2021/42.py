

def program():
    orders=[]
    numOfConcurOrders = 1
    curOrder=-1
    lastOrder=-1
    maxOrder=0
    maxOrderId=0
    ordersDict={1 : "DOPISZ", 2 : "USUN", 3 : "PRZESUN", 4: "ZMIEN" }
    plik = open("instrukcje.txt", "r")
    text = plik.read().splitlines()
    plik.close()
    for line in text:
        orders.append(line.split(" "))
    for order, letter in orders:
        if order =="DOPISZ":
            curOrder=1
        elif order =="USUN":
            curOrder=2
        elif order == "PRZESUN":
            curOrder=3
        elif order == "ZMIEN":
            curOrder=4
        if lastOrder==curOrder:
            numOfConcurOrders+=1
        else:
            numOfConcurOrders=1
        if numOfConcurOrders>maxOrder:
            maxOrder=numOfConcurOrders
            maxOrderId=curOrder
        lastOrder=curOrder
    print([maxOrder,ordersDict[maxOrderId]])



if __name__ == "__main__":
    program()