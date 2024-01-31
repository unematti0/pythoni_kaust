import random
#Mattias Elmers
#16.01.24
#Kodutöö



















#13. Ülesanne
try:
    arv = input("Sisesta arv: ")
    if arv == "" or arv == "0":
        print("Vigane sisend")
    elif int(arv) % 2 == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
except ValueError:
    print("Vigane sisend") 






#11. Ülesanne

def loo_salakeel():
    valik = input("Kas soovid luua salakeelt (sisesta 1) või tõlkida salakeelt (sisesta 2): ")
    if valik.lower() == "1":
         tavaline_sona = input("Sisesta tavaline sõna: ")

         salakeel = ""
         for i in tavaline_sona:
             if i.isalpha():
                 salakeel += i + 'i' + i
             else:
                 salakeel += i

         print("Salakeel:", salakeel)
    elif valik.lower() == "2":
         salakeelne_sona = input("Sisesta salakeelne sõna: ")

         tavaline_sona = ""
         for i in range(0, len(salakeelne_sona), 3):
             tavaline_sona += salakeelne_sona[i]

         print("Tõlgitud sõna:", tavaline_sona)
    else:
         print("Vigane valik. Palun sisesta 1 või 2.")


loo_salakeel()












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



input()
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