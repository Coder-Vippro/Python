import math
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
if a+b<c or a+c<b or b+c<a:
    print("Ba canh duoc nhap khong tap thanh tam giac")
else:
    p=float((a+b+c)/2)
    dt=float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print(f"Dien tich tam giac: {dt}")
    print(f"Chu vi tam giac: {p}")
    dt=float(((p-a)**0.5)*((p-b)**0.5)*((p-c)**0.5))
