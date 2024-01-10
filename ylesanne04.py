import random
# Mattias Elmers IT-23
# 14.11.2023
# ülesanne 01

"""
Ruutude ja kuupide tabel
Programm leiab ja väljastama ruudud ja kuubid arvudele 1..10.
Vorminda tabel tulpades.
Arv Ruut Kuup
1   1    1
2   4    8
3   9    27
4   16   64
jne
"""
print("arv ruut kuup")

for i in range (1,11):
    ruut = i**2
    kuup = i**3
    print(f"{i} {ruut:4} {kuup:5}")
    
    
    
    




input()

"""
Pank
Kasutaja soovib panka panna raha teatud aastateks.
Panga intress on 5% summast. Leia kui palju ta summa iga aasta kasvab.
Vorminda tabel tulpades.
Näiteks: paneme panka 10000€ ja 5 aastaks
Aasta   Algsumma    Intress     Aasta lõpuks
1       10000.00    500.00      10500.00
2       10500.00    525.00      11025.00
3       11025.00    551.25      11576.25
4       11576.25    578.81      12155.06
5       12155.06    607.75      12762.82
Summa kokku: 12762.82€
Kasum: 2762.82€
"""

raha = 10000
aasta = 5
konto = raha
intress = 0.05

print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range (aasta):
    print(f"{i+1} {konto:14.2f} {konto*intress:9.2f} {konto + konto * intress:13.2f}")
    konto = konto + konto * intress
    
print (f"Summa kokku: {konto:.2f}")
print (f"kasum: {konto-raha:.2f}€")
















"""
Arvamismäng
Kasutaja saab arvata arvuti poolt loodud arvu 3 korda.
Õnnitle kasutajat, kui arvas selle ära.
Kui mitte, siis küsi, kas ta soovib veel arvata.
"""
loop = 1
voidud = 0

while loop == 1:
    print("----------ARVAMISMÄNG----------")
    suv = random.randint(1,3)
    #print(suv)
    for i in range(3):
        arva = int(input("paku arv 1-3: "))
        if suv == arva:
            print("arvasid ära!")
            voidud += 1
            break
        else:
            print("proovi veel!")
    print("----------GAME OVER!----------")
    print(f"võidud: {voidud}")
    jatka = input("soovid jätkata? y/n: ")
    if jatka == "n":
        loop = 0








print()





"""
Viisikud
Programm väljastab ainult 5ga jaguvad arvud 1-100Viisikud
Programm väljastab ainult 5ga jaguvad arvud 1-100
"""


for i in range (1,101):
    if i%5 == 0:
        print(i)
        
input()





"""
Pisike korrutustabel
Koosta programm, mis tekitab automaatselt viiega korrutustabeli.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

for j in range(1,11):
    for i in range (1,11):
        print(f"{j} x {i} = {j*i}")











"""
Paaris ja paaritu
Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
"""

for x in range(1,11):
    if x % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
            
    print(x,v)




print()





"""
Loto
Koosta tsükli abil programm, mis kuvab 5 suvalist  ühekohalist numbrit. Näiteks 53542
"""

for x in range(5):
    print(random.randint(0, 9),end="")








print()
print()
"""
Tärnid
Loo tsükkel, mis väljastab 5×5 tärnid
Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""


j = 5
for  i in range(5):
    print("* "*j)
    j = j - 1





print()



j = 5
for  i in range(j):
    print("* "*(i+1))
print()








j = 5
for  i in range(j):
    print("* "*j)







"""
Jalgpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""

sugu = input("Sugu? : ")
if sugu == "mees":
    vanus = int(input("kui vana: "))
    if vanus >= 16 and vanus <=18:
        print("tere tulemast meeskonda")
    else:
        print("vanus ei sobi")
else:
    print("ei päese meeskonda")






"""
Müük
Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""




hind = int(input("sisesta hind: "))
if hind <= 10:
    vastus = 0.1
else:
    vastus = 0.2

print(f"toote hind on {hind-hind*vastus}€" )








"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
Plokkskeemi pole vaja!
"""

vanus = int(input("kui vana sa oled "))
if vanus % 5 == 0:
    v = "on"
else:
     v = "ei ole"       
print(f"vanus {vanus}: {v} juubel")








"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("arv 1: "))
nr2 = int(input("arv 2: "))
tehe = input("vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 - nr2
elif tehe == "/":
    vastus = nr1 - nr2
else:
    vastus = " ära huja"
    
    
print(f"{nr1} {tehe} {nr2} = {vastus}")



"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("ruudu 1. külg: "))
nr2 = int(input("ruudu 2. külg: "))

if nr1 == nr2:
    print("see on ruut")
else:
    print("see ei ole ruut")
    
    





