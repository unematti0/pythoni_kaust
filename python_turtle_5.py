import turtle
import random

# Mattias Elmers IT-23
# 28.11.2023
# töö

"""
	Turtle (if, for), Python 5- (6. - 9. Tund) /
Hinne: Kilpkonn (IF, FOR)
- funktsioon, mis loob erineva suuruse ja asukohaga viisnurga kogu platsi ulatuses (üle ääre ei tohi minna)
- funktsioon, mis loob erineva suuruse ja asukohaga kolmnurki kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt viisnurki ja kolmnurki
- menüü -> küsib kasutajalt, millist kujundit soovib, küsib kogust ja kui ära joonistab, siis küsib jälle. EXIT võimalus.
"""




#akna loomisne
w = turtle.Screen()
w.setup(600,600)



def looviisnurk():
    a = random.randint(10,200)
    x = random.randint(-300,200-a)
    y = random.randint(-300+(a//1.5),200-(a//1.5))
    john = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,360))
    for i in range(5):
        print(i)
        john.fd(a)
        john.rt(144)


def lookolmnurk():
    a = random.randint(10,200)
    x = random.randint(-300,200-a)
    y = random.randint(-300+(a//1.5),200-(a//1.5))
    john = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,360))
    for j in range(3):
        print(j)
        john.fd(a)
        john.rt(120)
    




def loosuvaline():
    suv = random.randint(1,2)
    print(suv)
    if suv == 1:
        looviisnurk()
    else:
        lookolmnurk()
        
    



def kuvamenyy():
    loop = 1
    while loop==1:
        valikujund = w.numinput("kujundi valik","1. vali viisnurk \n2. vali kolmnurk \n3. vali suvaline \n4.EXIT")
        if valikujund >= 4:
            exit()
        valikogus = int(w.numinput("kujundite arv","vali kujundite arv:"))
        for i in range (valikogus):
            if valikujund == 1:
                looviisnurk()
            elif valikujund == 2:
                lookolmnurk()
            elif valikujund == 3:
                loosuvaline()
            else:
                print("EXIT")
                
            

    


kuvamenyy()


turtle.exitonclick()




