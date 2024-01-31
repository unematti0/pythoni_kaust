import random
#Mattias Elmers
#16.01.24
#Kodutöö


#11. Ülesanne


tähestik = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z", "ä", "ö", "ü", "õ"]

def salasta(tavakiri, sala_võti):
    salakiri = ""
    for i in tavakiri:
        if i.isalpha():
            i = i.lower()
            i_indeks = tähestik.index(i)
            uus_indeks = (i_indeks + sala_võti) % 26
            sala_täht = tähestik[uus_indeks].upper()
        else:
            sala_täht = i

        salakiri += sala_täht

    print("sinu salakiri on: " + salakiri)




#9. Ülesanne

def emaili_kontroll(email):
    email = input("Sisesta email: ")
    if "@" in email:
        nimi = email.split('.')[0]
        domeen = email.split('@')[1]
        print(f"Tere {nimi}, sinu email on {email} ja domeeniks on {domeen}.")
    else:
        print("Sisestatud email on vale")

print(emaili_kontroll("email"))
















#7. Ülesanne

def arvutus(küsimus):
    #küsib küsimuse
    küsimus = input("Kas soovid arvutada EUR --> EEK või EEK --> EUR? (EUR --> EEK = 1, EEK --> EUR = 2): ")
    #kui vastus on 1, siis arvutab eurod kroonideks
    if küsimus == "1":
        euro = int(input("Sisesta eurode arv: "))
        print(f"{euro} eurot on {euro * 15.6466} krooni.")
        #kui vastus on 2, siis arvutab kroonid eurodeks
    elif küsimus == "2":
        kroon = int(input("Sisesta kroonide arv: "))
        print(f"{kroon} krooni on {kroon / 15.6466} eurot.")
        #kui vastus on midagi muud, siis ütleb, et sellist valikut ei ole
    else:
        print("sellist valikut ei ole! (valige palun kas 1 või 2)")



print(arvutus("küsimus"))










input()

#5. Ülesanne

ostunimekiri = []

def ostunimekirja(ostunimekiri):
    while True:
        toode = input("Sisesta toode: ")
        if toode == "":
            print(ostunimekiri)
            break
        else:
            ostunimekiri.append(toode)
        

ostunimekirja(ostunimekiri)












input()


#3. Ülesanne


loend1 = ["1, 2, 3, 4, 5, 6, 7, 8, 9, 10"]
loend2 =  ["-1, -2, -3, -4, -5, -6, -7, -8, -9, -10"]


def hoidmine(loend1, loend2):
    for i in range (5) :
        number = int(input("Sisesta number: "))
        if number > 0:
            loend1.append(f"{number},")
        elif number < 0:
            loend2.append(f"{number},")
    for i in loend1:
        print(i)
    for i in loend2:
        print(i)

hoidmine(loend1, loend2)








input()


#1. Ülesanne

arv1 = random.randint(1, 10)
arv2 = random.randint(1, 10)


def korrutamine(arv1, arv2):
    print(f"{arv1} * {arv2} = ")
    for i in range(10):
        vastus = int(input("Sisesta vastus: "))
        if vastus == arv1 * arv2:
            print("Õige vastus!")
        else:
            print("Vale vastus!")

korrutamine(arv1, arv2)