import math
import turtle
# Mattias Elmers IT-23
# 14.11.2023
# ülesanne 02

"""
kilpkonn - küsib kasutajalt ringi raadiust
           kasutab funktsiooni ringi joonistamiseks
           """
w = turtle.Screen()

def ring(r):
    john = turtle.Turtle()
    john.circle(r)

r = w.numinput("ringi loomine","sisesta ringi raadius:")

print(r)
ring(r)
turtle.exitonclick()

"""
Kütusekulu arvutamine
Kasutaja sisestab tangitud kütuse liitrid
Kasutaja sisestab läbitud kilomeetrid
Programm leiab kütusekulu 100km kohta keskmiselt
"""

kytus = int(input("sisesta liitrid: "))
km = int(input("sisesta läbitud km: "))
kulu = kytus / (km / 100)
print("kütuse kulu on:", kulu,"L")










"""
Arvusüsteemid
Kasutaja sisestab täisarvu kümnendsüsteemis
Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""

arv = int(input("sisesta arv: "))
bii = bin(arv)
heks = hex(arv)
print(bii, heks)







"""
Ajateisendus
Kasutaja sisestab aja minutites
Sinu valem leiab ja väljastab tunnid ja minutid
Näiteks: sisestus 72, vastus 1:12
"""


minutid = int(input("sisesta aeg minutites: "))
h = minutid // 60
m = minutid % 60
print(h,":",m)









"""
Leia kolmnurga hüpotenuus
Kolmnurga külgede pikkused on a=16 ja b=9
Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""

a = 16
b = 9
c = round(math.sqrt(a**2 + b**2))
print("kolmnurga hüpotenuus on",c)








"""
Rulluisutaja keskmine kiirus on 29,9km/h
Kui kaugele jõuab 24minutiga
"""


kiirus = 29.9
aeg = 24
tund = 60
kaugus = (kiirus/tund)*aeg

print("kiirusega", kiirus, "km/h jõuab", kaugus, "km kaugusele")









"""
Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
Jätate teenindajale 10% jootraha
Koosta programm, mis leiab kui palju peab igaüks maksma
"""


pitsahind = 12.90
jootraha = 0.1
sõbrad = 3
hind = (pitsahind+pitsahind*jootraha)/sõbrad

print("iga tüüp maksab ",hind,"€")


"""
Toote hind
Toote hind 36,75€
Soodushind hetkel 40%
Soovin kolme toote summat
"""



hind = 36.75
ale = 0.4
kogus = 3
summa = (hind-hind*ale)*kogus

print(str(kogus)+" toote hind kokku on "+str(summa))






"""
Loo kolm täisarvulist muutujat a, b, c
Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
"""

a,b,c = 5,10,15

p = a + b + c

print("kolnurga ümbermõõt:",p)











