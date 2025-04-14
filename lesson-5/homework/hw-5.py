### HOMEWORK-5
# a = int(input("Bitta rqam kiriting: "))
# b = a * 9 / 5 + 32
# print(b) 
#########################################
# a = int(input("Bitta rqam kiriting: "))
# b = (a - 32) * 5 / 9
# print(b)  
#########################################
# a = int(input("Dastlabki investitsiya miqdorini kiriting: $"))
# b = int(input("Yillik foiz stavkasini kiriting (%): "))
# c = int(input("Yillar sonini kiriting: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     e = a * (1 + d) ** a1
#     print(f"{a1}-Yil: ${e:.2f}")
#########################################
# a = int(input("Dastlabki depozit miqdorini kiriting: $"))
# b = int(input("Yillik daromad stavkasini kiriting : "))
# c = int(input("Yillar sonini kiriting: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for year in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{year}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting: $"))
# b = int(input("Yillik qaytish foizini kiriting: %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
#########################################
# a = int(input("Boshlang'ich depozit miqdorini kiriting (dolar): $"))
# b = int(input("Yillik qaytish foizini kiriting (foizda): %"))
# c = int(input("Nechta yil davomida investitsiya qilishni istaysiz?: "))
# d = b / 100
# for a1 in range(1, c + 1):
#     a = a * (1 + d)
#     print(f"{a1}-Yil: ${a:.2f}")
#########################################
# n = int(input("Musbat butun sonni kiriting: "))
# print(f"{n} sonining bo'luvchilari:")
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)
#########################################
# n = int(input("Musbat butun sonni kiriting: "))
# print(f"{n} sonining bo'luvchilari:")
# for i in range(1, n + 1):
#     if n % i == 0:  
#         print(i)
#########################################
# n = int(input("Musbat butun sonni kiriting: "))
# if n <= 0:
#     print("Iltimos, musbat butun son kiriting.")
# else:
#     print(f"{n} sonining bo'luvchilari:")
#     for i in range(1, n + 1):
#         if n % i == 0:  
#             print(i)
#########################################
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]
# usd_to_uzs = 12950
# print("Universitetlar ro'yxati:")
# print(f"{'Universitet':<40} {'Talabalar soni':<20} {"To'lov (UZS)":<15}")
# print("="*75)
# for university in universities:
#     name, students, tuition_usd = university
#     tuition_uzs = tuition_usd * usd_to_uzs  
#     print(f"{name:<40} {students:<20} {tuition_uzs:<15}")
#########################################
# a = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Urganch Davlat Universiteti", 10000, 4000000]
# ]
# for b in a:
#     ism = a[0]  
#     talabalar = a[1]  
#     oqish_tolovi = a[2]     
#     print(f"Universitet: {ism}")
#     print(f"Talabalar soni: {talabalar}")
#     print(f"Yillik o'quv xarajatlari: {oqish_tolovi} so'm")
#     print("-" * 30)
#########################################
# a = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Universiteti", 10000, 4000000]
# ]
# b = []  
# c = []  
# for a1 in a:
#     b.append(a1[1])  
#     c.append(a1[2]) 
# print("Talabalar soni:", b)
# print("O'quv xarajatlari:", c)
#########################################
# num = [10, 20, 30, 40, 50, 60, 70]
# a = sum(num)  
# b = a / len(num)
# print(f"O'rtacha qiymat: {b}")
# num.sort() 
# n = len(num)
# if n % 2 == 1: 
#     a1 = num[n // 2] 
# else:  
#     a1 = (num[n // 2 - 1] + num[n // 2])
# print(f"Median qiymat: {a1}")
#########################################
# universities = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Universiteti", 10000, 4000000]
# ]
# a = []  
# b = []  
# for university in universities:
#     a.append(university[1])  
#     b.append(university[2])  
# c = sum(a)
# d = sum(b)
# e = c / len(a)
# f = d / len(b)
# a.sort()
# g = len(a)
# if g % 2 == 1:
#     h = a[g // 2]
# else:
#     h = (a[g // 2 - 1] + a[g // 2]) / 2
# b.sort()
# q = len(b)
# if q % 2 == 1:
#     s = b[q // 2]
# else:
#     s = (b[q // 2 - 1] + b[q // 2]) / 2
# print(f"Umumiy talabalar soni: {c}")
# print(f"Umumiy o'quv xarajatlari: {d} so'm")
# print(f"Talabalar sonining o'rtachasi (mean): {e}")
# print(f"O'quv xarajatlarining o'rtachasi (mean): {f} so'm")
# print(f"Talabalar sonining mediani: {h}")
# print(f"O'quv xarajatlarining mediani: {s} so'm")
#########################################
# universities = [
#     ["Toshkent Davlat Universiteti", 15000, 5000000],
#     ["Samarkand Davlat Universiteti", 12000, 4500000],
#     ["Buxoro Davlat Universiteti", 10000, 4000000]
# ]
# a = []  
# b = [] 
# for c in universities:
#     a.append(c[1])  
#     b.append(c[2]) 
# d = sum(a)
# e = sum(b)
# f = d / len(a)
# g = e / len(b)
# a.sort()
# h = len(a)
# if h % 2 == 1:
#     j = a[h // 2]
# else:
#     j = (a[h // 2 - 1] + a[h // 2]) / 2
# b.sort()
# k = len(b)
# if k % 2 == 1:
#     l = b[k // 2]
# else:
#     l = (b[k // 2 - 1] + b[k // 2]) / 2
# print("*" * 30)
# print(f"Jami talabalar: {d:,}")
# print(f"Umumiy o'qish to'lovi $ {e:,.2f}")
# print()
# print(f"Talabalar soni bo'yicha o'rtacha qiymat: : $ {f:,.2f}")
# print(f"Talabalar o'rtacha: {j:,}")
# print()
# print(f"O'qish to'lovi: $ {g:,.2f}")
# print(f"Ta'lim o'rtacha: $ {l:,.2f}")
# print("*" * 30)
#########################################
n = int(input("Istalgan sonni kiriting: "))  
if n <= 1:
    print(False)
else:
    a = True
    for i in range(2, n):
        if n % i == 0:
            a = False
            break  
    print(a) 
