print("keterangan gaji pemulung")
class pemulung:
    def __init__(self):
        pass 

    def cetak_nama(self,nama):
        return print(nama)
    def cetak_gaji(self):
        gaji_pokok=1000000
        tunjangan=250000
        total_gaji=gaji_pokok + tunjangan
        return print (total_gaji)
                      
class gaji_tunjangan:
    def cetak_gaji(self,tunjangan):
        return print (gaji.tunjangan)
a=pemulung()
a.cetak_nama("wahyu")
a.cetak_gaji()

print("gaji selama 9 tahun jadi pemulung")


import turtle

t = turtle.Turtle()
s = turtle.Screen()


s.bgcolor('black')
t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-75,130)
t.pendown()
t.color('white')
t.write("100%",font=("verdana",25,"bold"))



t.penup()
t.goto(-150,-100)
t.pendown()
t.color('white')
t.write("I LOVE YOU",font=("verdana",40,"bold"))

turtle.done()