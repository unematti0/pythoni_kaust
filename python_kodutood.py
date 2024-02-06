import random
#Mattias Elmers
#16.01.24
#Kodutöö

#15. Ülesanne



jaanuar= [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3]
veebruar= [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18]
märts= [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2]
aprill= [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2]
mai= [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1]
juuni= [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22]
juuli= [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20]
august= [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11]
september= [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19]
oktoober= [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1]
november= [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1]
detsember= [-15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]
kuud = [jaanuar, veebruar, märts, aprill, mai, juuni, juuli, august, september, oktoober, november, detsember]

def koige_soojem_kuupaev(kuud):
    kuud.sort()
    


print(max(kuud))













input()
#13. Ülesanne
print("------PAARIS VÕI PAARITU ARV------")
try:
    arv = input("Sisesta arv: ")
    if int(arv)== 0:
        print("Arv on null")

    elif int(arv) % 2  == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
except ValueError:
    print("Vigane sisend") 




input()

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











input()
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