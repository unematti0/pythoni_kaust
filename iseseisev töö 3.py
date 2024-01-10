import random
#Iseseisev töö 3
#Mattias Elmers IT-23
#18.12.2023

import datetime
paev = (datetime.datetime.now().day)




#tahvli juurde
fail= open("nimekiri.txt", encoding="UTF-8")
nr = 1
for nimi in fail:  
    if nr == paev:
        print(nimi, end="") 
    nr += 1












input()
#jukebox
siiamidagi = input("Sisesta faili nimi: ")
fail = open(siiamidagi, encoding="UTF-8")
print("muusikapalade valik:")
nr = 1
for i in fail:
    print(f"{nr}. {i}" ,end="")
    nr += 1
valik = int(input("Vali laulu arv: "))

fail.seek(0) #keri faili algusesse
nr = 1
for i in fail:
    if nr == valik:
        print(i)
    nr += 1

input()














input()

#3.2


fail = open("konto.txt")
for i in fail:
    if float(i) > 0:
        print(i,end="")







#input()

#3.1


#fail = open("rebased.txt", encoding="UTF-8")
#vastuvoetud = []
#for rida in fail:
    #vastuvoetud.append(int(rida))



#print(vastuvoetud)
#fail.close()