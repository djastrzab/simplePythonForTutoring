

def read_file():
    result=[]
    plik = open("pary.txt", "r")
    tekst = plik.read().splitlines()
    plik.close()

    for w in tekst:
        para = [int(w.split(" ")[0]),str(w.split(" ")[1])]
        result.append(para)
    return result


def write_results_to_file (filename,results):
    plik = open(filename, "w")
    plik.write(results)
    plik.close()

def wybierz_pary_do_rozpatrzenia(pary):
    result=[]
    for para in pary:
        if(para[0]==len(para[1])):
            result.append(para)
    return result

def czy_pierwszy_alafabetycznie_napis1(napis1,napis2):
    for i in range(0,len(napis1)):
        if napis1[i]<napis2[i]:
            return True
        elif napis1[i]>napis2[i]:
            return False
    return True

def czy_mniejsza_para1(para1,para2):
    if para1[0]<para2[0]:
        return True
    else:
        if para1[0]==para2[0]:
            if czy_pierwszy_alafabetycznie_napis1(para1[1],para2[1]):
                return True
            else:
                return False
    return False


def znajdz_najmniejsza_pare(pary_do_rozpatrzenia):
    for para1 in pary_do_rozpatrzenia:
        flag = True
        for para2 in pary_do_rozpatrzenia:
            if(para1==para2):
                continue
            else:
                if not(czy_mniejsza_para1(para1, para2)):
                    flag = False
                    break
        if flag:
            return para1


if __name__ == "__main__":
    pary=read_file()
    pary_do_rozpatrzenia=wybierz_pary_do_rozpatrzenia(pary)

    print(znajdz_najmniejsza_pare(pary_do_rozpatrzenia))





