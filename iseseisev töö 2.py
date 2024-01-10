import random
#Iseseisev töö 1
#Mattias Elmers IT-23
#18.12.2023


#2.5

def lumivalgeke (p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad -= pounad
        print(pounad)
    print(f"lumivalgekesele jäi {ounad} õuna")

    
 

lumivalgeke(6)




input()
#2.4
def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(nisuterad)

male(5)
        







input()
#2.3

def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))


taringud(6)









input()
#2.2

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid += 1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid
    print(f"jänkulaps saab: {porgandid} porgandit!")



ringid = int(input("ringide arv:"))
porgandid(ringid)








input()
#2.1

def aratus(nr):
    for i in range(nr):
        print("Tõuse ja sära!")


kordused = int(input("sisestage mitu korda äratada: "))
aratus(kordused)