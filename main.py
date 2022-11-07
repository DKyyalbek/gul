import operator
import random
import turtle


def guu():
    # Set initial position
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)

    # flower base
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # Petal 1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # Petal 2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # Leaves 1
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)

    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)
    turtle.done()

class Gul():
    def __init__(self, name, shtuk, price):
        self.name = name
        self.shtuk = shtuk
        self.price = price

    def show(self):
        print('Названия цветок: {}'
              ' Штук: {} штук'
              ' Цена: {} тг'.format(self.name, self.shtuk, self.price))


def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.show()

class Magaz(Gul):
    def __init__(self, name, shtuk, price):
        super().__init__(name, shtuk, price)


gul1 = Magaz('Roza', 50, 5000)
gul2 = Magaz('BakBak', 150, 2000)
gul3 = Magaz('Lala',100, 3500)
e = [gul1, gul2, gul3]

t = []

def su(t):
    for i in range(len(e)):
        t.append(e[i].price)
su(t)

def ajj(t):
    d = int(input("Kansha akshaga alasiz - "))
    if 0 < d < 2000:
        print("Norm Buket Zhok")
        print("Try again?")
        return ajj(t)
    elif d < 0:
        print("Minus san")
        print("Try again?")
        return ajj(t)
    else:
        r = [0]
        i = 0
        g = 0
        while g <= d:
            if e[0].shtuk == 0 or e[1].shtuk == 0 or e[2].shtuk == 0:
                print("Gul sany zhetpid")
            else:
                r.append(random.choice(t))

            i = i + 1
            if g <= d:
                g = g + r[i]
            if g > d:
                r.pop(-1)
        y = 0
        for i in range(len(r)):
            y = y + r[i]
        print(y)
        t = []
        mas = []
        su(t)
        print(r)
        for i in range(len(t)):
            a = 0
            for j in range(len(r)):
                if r[j] == t[i]:
                    a = a + 1
            mas.append(a)
        for i in range(len(e)):
            print(e[i].name, mas[i], "Dana")

        print("Alatin boldinizba?")
        print("1. Ya")
        print("2. Zhok")
        a = int(input())
        if a == 1:
            for i in range(len(e)):
                e[i].shtuk = e[i].shtuk - mas[i]
            # guu()
            print("Kalgan akshanyz - ", d - y)
        if a == 2:
            return ajj(t)


def ahh():
    print("Alatin boldinizba?")
    print("1. Ya")
    print("2. Zhok")
    a = int(input())
    if a == 1:
        for i in range(len(e)):
            e[i].shtuk = e[i].shtuk - mas[i]
        # guu()
    if a == 2:
        return ajj(t)

mas = []
def du(mas):
    for i in range(len(e)):
        a = int(input(e[i].name + " Kansh shtuk - "))
        if a <= e[i].shtuk:
            mas.append(a)
        else:
            print("ondai olshemde gul zhok zhazdynyz")
            return du(mas)

    for i in range(len(e)):
        print(e[i].name, mas[i], "Dana")

    ahh()
while True:

    print('1. Barlyk Gulder')
    print('2. Satyp Alamyn ! ')
    print('3. Admin')
    print('4. exit')

    # for i in range(len(e)-1):
    #     if e[i].shtuk == 0:
    #         e.pop(i)

    n = int(input())
    if n == 1:
        sort_choice(e, 'shtuk')

    if n == 2:
        while True:
            print('Guldi kalai aluga bolady?')
            print('1. Kolda bar aksha boinsha!')
            print('2. Bagasy boinsha!')
            print("3. Exit!")
            o = int(input())
            if o == 1:
                ajj(t)
            if o == 2:
                sort_choice(e, "shtuk")
                mas = []
                du(mas)
                # q1 = int(input(e[0].name + " Kansh shtuk - "))
                # q2 = int(input(e[1].name + " Kansh shtuk - "))
                # q3 = int(input(e[2].name + " Kansh shtuk - "))
                # mas = [q1,q2,q3]


            if o == 3:
                break
    if n == 3:
        print("Zhana gul keldy!")
        a = int(input("Kelgen gul turlerinin sany? "))
        for i in range(a):
            a1 = input("Gul aty?")
            a2 = int(input("Gul sany?"))
            a3 = int(input("Gul bagasy?"))
            r = 0
            for i in e:
                if a1.strip() == i.name:
                    i.shtuk = i.shtuk + a2
                    print("1 - Buringi baga kalsinba?")
                    print("2 - Osi baga bagaga 25 %?")
                    if i.price != a3:
                        f = int(input())
                        if f == 1:
                            continue
                        if f == 2:
                            i.price = a3 + a3 * 0.25
                    else:
                        continue
                else:
                    r = r + 1
            if r == len(e):
                w = Magaz(a1, a2, a3)
                e.append(w)

        for i in e:
            i.show()
    if n == 4:
        break


# import math
#
# class Triangle:
#
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def audan(self):
#         p = (self.a + self.b + self.c) / 2
#         s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#         return s
#
#
#     def perimeter(self):
#
#
#         return self.a + self.b + self.c
#
# first = Triangle(10,8,9)
# print(
#     "\na1 = ", first.a,
#     "\nb1 =",first.b,
#     "\nc1 = ", first.c,
#     "\ns1 = ", first.audan(),
#     "\np1 = ", first.perimeter()
# )
#
# first.perimeter()
# second = Triangle(a=36, b=40, c=50)
#
# print(
#     "\na1 = ", first.a,
#     "\nb1 =",first.b,
#     "\nc1 = ", first.c,
#     "\ns1 = ", first.audan(),
#     "\np1 = ", first.perimeter()
# )