#TÜ iseseisevtöö
#M.Metshein
#10.01.24

kassa = 0
def pronksikarva_summa(f):
    kassa = 0
    fail = open("myndid.txt")
    for mynt in fail:
        if int(mynt) > 10:
            print(mynt, end="")
            kassa += int(mynt)
    print("\nKassas: ", kassa)









input()

kylalised = 8
def tervitus(n):
    print('võõrustaja: "Tere!"')
    print(f"täna {n}. kord tervitada!")
    print('külaline: \"Tere, suur tänu kutse eest!\"')


for  i in range(kylalised):
    tervitus(i+1)















input()

def eelarve(kylalised):
    summa = kylalised * 10 + 55
    return summa

palju = int(input("külaliste arv: "))
palju2 = int(input("mitu tuleb: "))

print(f"maksimaalne eelarve:{eelarve(palju)}")
print(f"minimaalne eelarve:{eelarve(palju2)}")





input()


def mahlapakkideaerv(kg):
    pakid = round(kg * 0.4 / 3)
    return pakid

kogus = float(input("õunte kogus: "))
print(mahlapakkideaerv(kogus))









input()

def banner(t):
    print(t.upper())


ask = int(input("mitu korda? : "))
ask2 = input("reklaamlause : ")


for i in range(ask):
    banner(ask2)