#Iseseisev töö 1
#Mattias Elmers IT-23
#18.12.2023

#1.4


inimeste_arv = input("mitu inimest on vaja transportida: ")
kohtade_arv = input("mitu kohta on bussil: ")

busse_vaja = int(inimeste_arv) // int(kohtade_arv)
viimane_buss = int(inimeste_arv) % int(kohtade_arv)


if int(inimeste_arv) == int(kohtade_arv):
    busse_vaja = int(inimeste_arv) // int(kohtade_arv)
    viimane_buss = int(inimeste_arv)


elif int(kohtade_arv) > 0 :
    busse_vaja = busse_vaja + 1 
else:
    busse_vaja = busse_vaja


viimane_buss = int(inimeste_arv) % int(kohtade_arv)
print("Busse vaja: " + str(busse_vaja) )
print("Viimases bussis inimesi: " + str(viimane_buss))






input()
#1.3

küsimus = input ("Kui kõrgel on pilvede alus kilomeetrites: ")

if int(küsimus) <= 6 :
    print("Need ei ole ülemised pilved")

else:
    print("need on ülemised pilved")






input()
#1.2

aasta = 2020
liblikas = "teelehemosaiikliblikas."
lause_keskosa = ". aasta liblikas on "
lause = (str(aasta) + lause_keskosa + liblikas)

print (lause)




input()
#1.1
print ("Tere, maailm!")


