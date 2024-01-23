d1=int(input("Nhap d1: "))
d2=int(input("Nhap d2: "))
d3=int(input("Nhap d3: "))
d4=int(input("Nhap d4: "))
d5=int(input("Nhap d5: "))
d6=int(input("Nhap d6: "))
x=int(input("Nhap so dien tieu thu (KWh): "))
if x<=50:
    tiendien=(x*d1)
elif x>=51 and x<=100:
    tiendien=0
    tiendien=50*d1+(x-50)*d2 
elif x>=101 and x<=200:
    tiendien=0
    tiendien=50*d1+50*d2+(x-100)*d3
elif x>=201 and x<=300:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+(x-200)*d4 
elif x>=301 and x<=400:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+100*d4+(x-300)*d5
else:
    tiendien=0
    tiendien=50*d1+50*d2+100*d3+100*d4+100*d5+(x-400)*d6
print("So tien dien phai tra:",tiendien,"nghin dong")
