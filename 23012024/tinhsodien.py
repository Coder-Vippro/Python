tiendien = int(input("Nhập số tiền điện phải trả (nghìn đồng): "))
d1 = int(input("Nhập d1: "))
d2 = int(input("Nhập d2: "))
d3 = int(input("Nhập d3: "))
d4 = int(input("Nhập d4: "))
d5 = int(input("Nhập d5: "))
d6 = int(input("Nhập d6: "))
KWh = 0

if tiendien <= 50 * d1:
    KWh = tiendien / d1
elif tiendien <= 50 * d1 + 50 * d2:
    KWh = 50 + (tiendien - 50 * d1) / d2
elif tiendien <= 50 * d1 + 50 * d2 + 100 * d3:
    KWh = 50 + 50 + (tiendien - 50 * d1 - 50 * d2) / d3
elif tiendien <= 50 * d1 + 50 * d2 + 100 * d3 + 100 * d4:
    KWh = 50 + 50 + 100 + (tiendien - 50 * d1 - 50 * d2 - 100 * d3) / d4
elif tiendien <= 50 * d1 + 50 * d2 + 100 * d3 + 100 * d4 + 100 * d5:
    KWh = 50 + 50 + 100 + 100 + (tiendien - 50 * d1 - 50 * d2 - 100 * d3 - 100 * d4) / d5
else:
    KWh = 50 + 50 + 100 + 100 + 100 + (tiendien - 50 * d1 - 50 * d2 - 100 * d3 - 100 * d4 - 100 * d5) / d6
print("Số điện tiêu thụ (KWh):", KWh)
