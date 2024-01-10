# Mattias Elmers IT-23
# 14.11.2023
# ülesanne 01


"""
palindroom
"""

tekst = input("sisesta tekst: ")
print(tekst == tekst[::-1])






"""
Tundide ajad
Kasutaja sisestab tundide alguse ja lõpu. Näiteks 8:30 ja 14:15
Sinu programm leiab, kui pikk oli õpilase päev
Väljasta täislause ja kasuta vormindamisel format() meetodit.
"""

algus = input("sisesta tundide algus: ")
lopp = input("sisesta tundide lõpp: ")

hh1,mm1 = algus.split(":")
hh2,mm2 = lopp.split(":")


algus_minutid = int(hh1) * 60 + int(mm1)
lopp_minutid = int(hh2) * 60 + int(mm2)


ajavahe =  lopp_minutid - algus_minutid
tunnid = ajavahe // 60 
minutid =ajavahe % 60


print(f"{tunnid}:{minutid}")




"""
Email
Küsi kasutajalt emaili ja kontrolli, kas see sisaldas @-märki.
Näiteks: sisend–>minu@mail.ee; väljund–> True või False
"""

ask = input("mis on teie email?: ")
print("@" in ask)







"""
Vandumine
Kui kasutaja sisestab “kogemata” teksti, kus leidub sõna ‘kurat’, siis sinu programm asendab need tärnidega.
Näiteks: sisend–>Kurat küll!; väljund–>*** küll!
"""

ask = input("sisesta tekst: ")
print(f"Tere {ask.replace('kurat','***')}!")







"""
Korralik nimi
Küsi kasutajalt nime
Tervita teda ja sinu programm väljastab nime kirjapildi õigesti – suure algustähega ja eemaldab ülearused tühikud
Näiteks: sisend–>mARiO; väljund–>Tere, Mario!
"""

nimi = input("Mis on sinu nimi?: ")



print(f"Tere {nimi.strip().capitalize()}!")



