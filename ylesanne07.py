import math
#tekstifailid
#5.12.23
#Mattias Elmers


"""
Koosta ruumalade leidmise programm. Kasutajalt küsitakse, millise kujundi ruumala on vaja leida ja siis vajalikke argumente. Kasutada tuleb funktsioone. Tore, kui programm ei lõpetaks kohe töö vaid lubab valida teisi ruumalasid.
"""



kuju = input("\n1 kuup \n2 kera \n3 koonus \n4 silinder \n Vali kujund :")


if kuju == "1":
    def kuup(a,b,c):
        v = a*b*c
        print(f"kuubi ruumala on: {v}")

    kuup(3,3,3)

elif kuju == "2":
    def kera():
        pass

elif kuju == "3":
    def koonus(sk, sp):
        St = sk + sp
        print(f"koonuse pindala on : {St}")


elif kuju == "4":
    def silinder():
        pass





input()


def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"hi {nimi}!")
    elif keel == "et":
        print(f"Tere {nimi}!")
    else:
        print(f"hallo {nimi}!")



tervita("jüri")