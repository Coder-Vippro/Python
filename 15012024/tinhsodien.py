tiendien = int(input("Nhập số tiền điện phải trả (nghin đồng): "))
d1 = int(input("Nhập d1: "))
d2 = int(input("Nhập d2: "))
d3 = int(input("Nhập d3: "))
d4 = int(input("Nhập d4: "))
d5 = int(input("Nhập d5: "))
d6 = int(input("Nhập d6: "))
h = int(input("Nhập số phần trăm tiền điện tăng trong năm nay (%): "))
tiendien_no_tax = tiendien / (1 + 8/100)
KWh = 0
if tiendien_no_tax <= 50 * d1:
    tiendien_1 = tiendien_no_tax
    KWh = tiendien_no_tax / d1
elif tiendien_no_tax <= 50 * d1 + 50 * d2:
    tiendien_1 = 50 * d1
    tiendien_2 = tiendien_no_tax - tiendien_1
    KWh = 50 + tiendien_2 / d2
elif tiendien_no_tax <= 50 * d1 + 50 * d2 + 100 * d3:
    tiendien_1 = 50 * d1
    tiendien_2 = tiendien_no_tax - tiendien_1
    tiendien_3 = tiendien_2 - 50 * d2
    KWh = 50 + 50 + tiendien_3 / d3
elif tiendien_no_tax <= 50 * d1 + 50 * d2 + 100 * d3 + 100 * d4:
    tiendien_1 = 50 * d1
    tiendien_2 = tiendien_no_tax - tiendien_1
    tiendien_3 = tiendien_2 - 50 * d2
    tiendien_4 = tiendien_3 - 100 * d3
    KWh = 50 + 50 + 100 + tiendien_4 / d4
elif tiendien_no_tax <= 50 * d1 + 50 * d2 + 100 * d3 + 100 * d4 + 100 * d5:
    tiendien_1 = 50 * d1
    tiendien_2 = tiendien_no_tax - tiendien_1
    tiendien_3 = tiendien_2 - 50 * d2
    tiendien_4 = tiendien_3 - 100 * d3
    tiendien_5 = tiendien_4 - 100 * d4
    KWh = 50 + 50 + 100 + 100 + tiendien_5 / d5
else:
    tiendien_1 = 50 * d1
    tiendien_2 = 50 * d2
    tiendien_3 = 100 * d3
    tiendien_4 = 100 * d4
    tiendien_5 = 100 * d5
    tiendien_6 = tiendien_no_tax - tiendien_1 - tiendien_2 - tiendien_3 - tiendien_4 - tiendien_5
    KWh = 50 + 50 + 100 + 100 + 100 + tiendien_6 / d6
print(f"Số điện tiêu thụ (KWh): {KWh}")
