a=int(input("Nhap tien dien: "))
d1=int(input("Nhap d1: "))
d2=int(input("Nhap d2: "))
d3=int(input("Nhap d3: "))
d4=int(input("Nhap d4: "))
d5=int(input("Nhap d5: "))
d6=int(input("Nhap d6: "))
x=1 
tiendien=0
dem=0
a=a-(a*(8/100))
while tiendien!=a:
    if dem<50 and tiendien+d1<=a:
        tiendien=tiendien+d1
        dem=dem+1
    if dem>=50 and dem<100 and tiendien+d2<=a:
        tiendien=tiendien+d2
        dem=dem+1
    if dem>=100 and dem<200 and tiendien+d3<=a:
        tiendien=tiendien+d3
        dem=dem+1
    if dem>=200 and dem<300 and tiendien+d4<=a:
        tiendien=tiendien+d4
        dem=dem+1
    if dem>=300 and dem<400 and tiendien+d5<=a:
        tiendien=tiendien+d5
        dem=dem+1
    if dem>=400 and tiendien+d6<=a:
        tiendien=tiendien+d6
        dem=dem+1
    #else: break
print(f"Gia dinh da su dung {dem} so dien")
