#tekstifailid
#5.12.23
#Mattias Elmers



"""
Sellel aadressil asub nimekiri populaarsematest poliitikutest Facebookis: https://metshein.com/python/s6pru_l6ustaraamatus.txt
Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates.
"""





fail = open("s6pru_l6ustaraamatus.txt","r")
erakonnad = []

re = 0
ke = 0

for rida in fail:
    #enimi, perenimi, erak, sobrad = rida.split(" ")
    poliitik = rida.split(" ")


    print(f"{poliitik[0]:10} {poliitik[1]:10} {poliitik[2]:4} {poliitik[3]}", end ="")
    if poliitik[2]=="RE":
        re+=1
    elif poliitik[2]=="KE":
        ke+=1
#lisab unikaalsed erakonnad masiivi
    if poliitik[2] not in erakonnad:
        erakonnad.append(poliitik[2])



        #kirjutab tekstifaili
        with open("poliitikud.txt","a")  as kirjutamiseks:
            kirjutamiseks.write(poliitik[0]+" "+poliitik[1]+"/n")

print()
print(f"reformikad: {re} \nkesikud: {ke}")
print(f"erakondi kokku {len(erakonnad)}")


fail.close