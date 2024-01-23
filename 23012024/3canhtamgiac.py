import math
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
if a+b<c or a+c<b or b+c<a:
    print("Ba canh duoc nhap khong tap thanh tam giac")
else:
    p=float((a+b+c)/2)
    dt=float((p*(p-a)*(p-b)*(p-c))**0.5)
    print("Dien tich tam giac:",dt)
    print("Chu vi tam giac:",p*2)
