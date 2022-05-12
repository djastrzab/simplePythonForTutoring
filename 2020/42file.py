

def read_strings():
    teksty=[]
    plik = open("pary.txt", "r")
    tekst = plik.read().splitlines()
    plik.close()

    for w in tekst:
        l = str(w.split(" ")[1])
        teksty.append(l)
    return teksty
def check_most_cases_in_word(text):
    tmp_letter=text[0]
    counter=0
    max_counter=0
    result_letter=''
    for letter in text:
        if tmp_letter == letter:
            counter+=1
        else:
            counter=1
        if counter>max_counter:
            max_counter=counter
            result_letter=letter
        tmp_letter=letter
    return [result_letter*max_counter, max_counter]


def write_results_to_file (filename,results):
    plik = open(filename, "w")
    plik.write(results)
    plik.close()

def dlugosc1(wyra):
    litera1=wyra[0]
    licznik=0
    max_licznik=0
    litera2=""
    for litera in wyra:
        if litera==litera1:
            licznik+=1
        else:
            licznik=1
        if max_licznik<licznik:
            litera2=litera1
            max_licznik=licznik
        litera1=litera
    return(litera2*max_licznik,max_licznik)


if __name__ == "__main__":
    teksty=read_strings()
    print(teksty)
    pary=[]
    pary_pawel=[]
    result_text=''
    for tekst in teksty:
        pary_pawel.append(dlugosc1(tekst))
        pary.append(check_most_cases_in_word(tekst))
    print(pary)
    print(pary_pawel)
    for para in pary:
        result_text+=str(para[0])+" "+str(para[1])+'\n'
    write_results_to_file("4.2.txt",result_text)

