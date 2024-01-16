import random
#Mattias Elmers
#16.01.24
#Kodutöö

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