import math
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
if a+b<c or a+c<b or b+c<a:
    print(f"Ba canh {a}, {b}, {c} duoc nhap khong tap thanh tam giac")
else:
    p=float((a+b+c)/2)
    print(f"Chu vi tam giac: {p}")
    dt=float(((p-a)**0.5)*((p-b)**0.5)*((p-c)**0.5))
