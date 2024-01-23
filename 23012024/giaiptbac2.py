a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
delta=b*b-4*a*c
if delta<0:
    print("Phuong trinh vo nghiem")
elif delta==0:
    x=-b/(2*a)
    print("Phuong trinh co nghiem kep x1=x2=",x)
else:
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print("Phuong trinh co hai nghiem x1=",x1,"x2=",x2)

