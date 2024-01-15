d1=int(input("Nhap d1: "))
d2=int(input("Nhap d2: "))
d3=int(input("Nhap d3: "))
d4=int(input("Nhap d4: "))
d5=int(input("Nhap d5: "))
d6=int(input("Nhap d6: "))
x=int(input("Nhap so dien tieu thu (KWh): "))
h=int(input("Nhap so phan tram tien dien tang trong nam nay (%): "))
if h!=0:
    d1=d1+d1*(h/100)
    d2=d2+d2*(h/100)
    d3=d3+d3*(h/100)
    d4=d4+d4*(h/100)
    d5=d5+d5*(h/100)
    d6=d6+d6*(h/100)
if x<=50:
    print(f"So tien dien phai tra: {(x*d1)+(x*d1)*(8/100)} nghin dong")
elif x>=51 and x<=100:
    tiendien=0
    tiendien=50*d1+(x-50)*d2
    print(f"So tien dien phai tra: {tiendien+tiendien*(8/100)} nghin dong")
elif x>=101 and x<=200:
    tiendien=0
    tiendien=50*d1+50*d2+(x-100)*d3
    print(f"So tien dien phai tra: {tiendien+tiendien*(8/100)} nghin dong")
elif x>=201 and x<=300:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+(x-200)*d4
    print(f"So tien dien phai tra: {tiendien+tiendien*(8/100)} nghin dong")
elif x>=301 and x<=400:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+100*d4+(x-300)*d5
    print(f"So tien dien phai tra: {tiendien+tiendien*(8/100)} nghin dong")
else:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+100*d4+100*d5+(x-400)*d6
    print(f"So tien dien phai tra: {tiendien+tiendien*(8/100)} nghin dong")

