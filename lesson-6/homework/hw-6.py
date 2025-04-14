# a = 10
# b = 2
# if b == 0:
#     print("Xatolik: Nolga bo'lish mumkin emas!")
# else:
#     print(a / b)  
# b = 0
# if b == 0:
#     print("Xatolik: Nolga bo'lish mumkin emas!")
# else:
#     print(a / b)  
#########################################
# c = lambda func: lambda a, b: func(a, b) if b != 0 else "Xato: Nomi bo'yicha 0 ga bo'linish mumkin emas!"
# d = c(lambda a, b: a / b)
# r = d(6, 2)
# print(r)  
# rz = d(6, 0)
# print(rz)  
#########################################
# c = lambda func: lambda a, b: func(a, b) if b != 0 else "Denominator can't be zero"
# d = c(lambda a, b: a / b)
# r = d(6, 2)
# print(r)  
# rz = d(6, 0)
# print(rz) 
#########################################
# a = "employees.txt"
# with open(a, 'a') as f:
#     print("Yangi xodim haqida ma'lumotlarni kiriting:")
#     b = input("Xodimning ID raqamini kiriting: ")
#     c = input("Xodimning ismini kiriting: ")
#     d = input("Xodimning lavozimini kiriting: ")
#     e = input("Xodimning maoshini kiriting: ")
#     f.write(f"{b}, {c}, {d}, {e}\n")
# print(f"Xodimning ma'lumotlari '{a}' fayliga qo'shildi.")
# print({b}, {c}, {d}, {e}, {f})
#########################################
# a = "employees.txt"
# b = lambda: open(a, 'a').write(f"{input('Xodimning ID raqamini kiriting: ')}, {input('Xodimning ismini kiriting: ')}, {input('Xodimning lavozimini kiriting: ')}, {input('Xodimning maoshini kiriting: ')}\n")
# c = lambda: print("\n".join(open(a, 'r').readlines()) if open(a, 'r').readlines() else "Faylda hech qanday xodim ma'lumotlari yo'q.")
# d = lambda: print(next((record.strip() for record in open(a, 'r').readlines() if record.startswith(input('Qidirilayotgan xodimning ID raqamini kiriting: '))), "Xodim topilmadi."))
# e = lambda: open(a, 'w').writelines([f"{input('Xodimning ID raqamini kiriting: ')}, {input('Xodimning yangi ismini kiriting: ')}, {input('Xodimning yangi lavozimini kiriting: ')}, {input('Xodimning yangi maoshini kiriting: ')}\n" if record.startswith(input('Yangilanishi kerak bo\'lgan xodimning ID raqamini kiriting: ')) else record for record in open(a, 'r').readlines()])
# f = lambda: open(a, 'w').writelines([record for record in open(a, 'r').readlines() if not record.startswith(input('O\'chirilishi kerak bo\'lgan xodimning ID raqamini kiriting: '))])
# while True:
#     print("\nTanlovlar:")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni ID bo'yicha qidirish")
#     print("4. Xodim ma'lumotlarini yangilash")
#     print("5. Xodimni o'chirish")
#     print("6. Chiqish")
#     g = input("\nTanlovni kiriting: ")
#     if g == '1':
#         b()
#     elif g == '2':
#         c()
#     elif g == '3':
#         d()
#     elif g == '4':
#         e()
#     elif g == '5':
#         f()
#     elif g == '6':
#         print("Dasturni yakunlash...")
#         break
#     else:
#         print("Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.")
#########################################
#Option 1:
# a = "employees.txt"
# print("\nYangi xodim haqida ma'lumotlarni kiriting:")
# b = input("Xodimning ID raqamini kiriting: ")
# c = input("Xodimning ismini kiriting: ")
# d = input("Xodimning lavozimini kiriting: ")
# e = input("Xodimning maoshini kiriting: ")
# with open(a, 'a') as f:
#     f.write(f"{b}, {c}, {d}, {e}\n")
# print(f"Xodimning ma'lumotlari '{a}' fayliga qo'shildi.")
# print({b}, {c}, {d}, {e},)
#########################################
#Option 2:
# a = "employees.txt"
# try:
#     with open(a, 'r') as b:
#         c = b.readlines()
#         if c:
#             print("\nBarcha xodimlar ma'lumotlari:")
#             for d in c:
#                 print(d.strip())
#         else:
#             print("Faylda hech qanday xodim ma'lumotlari yo'q.")
# except FileNotFoundError:
#     print(f"Xato: '{a}' fayli topilmadi.")
#########################################
#Option 3:
# a = "employees.txt"
# b = input("\nXodimni ID raqami bo'yicha qidirish uchun ID kiriting: ")
# try:
#     with open(a, 'r') as f:
#         c = f.readlines()
#         d = False
#         for e in c:
#             if e.startswith(b):
#                 print("\nXodim ma'lumotlari:")
#                 print(e.strip())
#                 d = True
#                 break        
#         if not d:
#             print(f"ID {b} bo'yicha xodim topilmadi.")
# except FileNotFoundError:
#     print(f"Xato: '{a}' fayli topilmadi.")
#########################################
#Option 4:
# a = "employees.txt"
# b = input("\nYangilanishi kerak bo'lgan xodimning ID raqamini kiriting: ")
# try:
#     with open(a, 'r') as c:
#         d = c.readlines()    
#     e = False
#     with open(a, 'w') as c:
#         for f in d:
#             if f.startswith(b):
#                 print("\nXodimning ma'lumotlarini yangilash:")
#                 g = input("Yangi ismni kiriting (hozirgi ism: " + f.split(",")[1].strip() + "): ")
#                 h = input("Yangi lavozimini kiriting (hozirgi lavozim: " + f.split(",")[2].strip() + "): ")
#                 j = input("Yangi maoshini kiriting (hozirgi maosh: " + f.split(",")[3].strip() + "): ")
#                 c.write(f"{b}, {g}, {h}, {j}\n")
#                 k = True
#             else:
#                 c.write(f)    
#     if e:
#         print(f"Xodimning ma'lumotlari muvaffaqiyatli yangilandi.")
#     else:
#         print(f"ID {b} bo'yicha xodim topilmadi.")
# except FileNotFoundError:
#     print(f"Xato: '{a}' fayli topilmadi.")
#########################################
#Option 5:
# a = "employees.txt"
# b = input("\nO'chirilishi kerak bo'lgan xodimning ID raqamini kiriting: ")
# try:
#     with open(a, 'r') as c:
#         d = c.readlines()    
#     e = False
#     with open(a, 'w') as c:
#         for f in d:
#             if not f.startswith(b):
#                 c.write(f)
#             else:
#                 e = True    
#     if e:
#         print(f"ID {b} bo'yicha xodimning ma'lumotlari o'chirildi.")
#     else:
#         print(f"ID {b} bo'yicha xodim topilmadi.")
# except FileNotFoundError:
#     print(f"Xato: '{a}' fayli topilmadi.")
#########################################
#Option 6:
# a = "employees.txt"
# while True:
#     print("\nTanlovlar:")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni ID bo'yicha qidirish")
#     print("4. Xodim ma'lumotlarini yangilash")
#     print("5. Xodimni o'chirish")
#     print("6. Chiqish")
#     b = input("\nTanlovni kiriting: ")
#     if b == '1':
#         c = input("\nXodimning ID raqamini kiriting: ")
#         d = input("Xodimning ismini kiriting: ")
#         e = input("Xodimning lavozimini kiriting: ")
#         f = input("Xodimning maoshini kiriting: ")
#         with open(a, 'a') as g:
#             g.write(f"{c}, {d}, {e}, {f}\n")
#         print(f"Xodimning ma'lumotlari '{a}' fayliga qo'shildi.")
#     elif b == '2':
#         try:
#             with open(a, 'r') as g:
#                 records = g.readlines()
#                 if records:
#                     print("\nBarcha xodimlar ma'lumotlari:")
#                     for record in records:
#                         print(record.strip())
#                 else:
#                     print("Faylda hech qanday xodim ma'lumotlari yo'q.")
#         except FileNotFoundError:
#             print(f"Xato: '{a}' fayli topilmadi.")
#     elif b == '3':
#         employee_id = input("\nXodimni ID raqami bo'yicha qidirish uchun ID kiriting: ")
#         try:
#             with open(a, 'r') as g:
#                 records = g.readlines()
#                 found = False
#                 for record in records:
#                     if record.startswith(employee_id):
#                         print("\nXodim ma'lumotlari:")
#                         print(record.strip())
#                         found = True
#                         break                
#                 if not found:
#                     print(f"ID {employee_id} bo'yicha xodim topilmadi.")
#         except FileNotFoundError:
#             print(f"Xato: '{a}' fayli topilmadi.")    
#     elif b == '4':
#         employee_id = input("\nYangilanishi kerak bo'lgan xodimning ID raqamini kiriting: ")
#         try:
#             with open(a, 'r') as g:
#                 records = g.readlines() 
#             updated = False
#             with open(a, 'w') as g:
#                 for record in records:
#                     if record.startswith(employee_id):
#                         print("\nXodimning ma'lumotlarini yangilash:")
#                         new_name = input("Yangi ismni kiriting (hozirgi ism: " + record.split(",")[1].strip() + "): ")
#                         new_position = input("Yangi lavozimini kiriting (hozirgi lavozim: " + record.split(",")[2].strip() + "): ")
#                         new_salary = input("Yangi maoshini kiriting (hozirgi maosh: " + record.split(",")[3].strip() + "): ")
#                         g.write(f"{employee_id}, {new_name}, {new_position}, {new_salary}\n")
#                         updated = True
#                     else:
#                         g.write(record)            
#             if updated:
#                 print(f"Xodimning ma'lumotlari muvaffaqiyatli yangilandi.")
#             else:
#                 print(f"ID {employee_id} bo'yicha xodim topilmadi.")
#         except FileNotFoundError:
#             print(f"Xato: '{a}' fayli topilmadi.")    
#     elif b == '5':
#         employee_id = input("\nO'chirilishi kerak bo'lgan xodimning ID raqamini kiriting: ")

#         try:
#             with open(a, 'r') as g:
#                 records = g.readlines()
            
#             found = False
#             with open(a, 'w') as g:
#                 for record in records:
#                     if not record.startswith(employee_id):
#                         g.write(record)
#                     else:
#                         found = True
            
#             if found:
#                 print(f"ID {employee_id} bo'yicha xodimning ma'lumotlari o'chirildi.")
#             else:
#                 print(f"ID {employee_id} bo'yicha xodim topilmadi.")
#         except FileNotFoundError:
#             print(f"Xato: '{a}' fayli topilmadi.")
    
#     elif b == '6':
#         print("Dasturdan chiqyapman...")
#         break    
#     else:
#         print("Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.")
#########################################
# try:
#     with open("sample.txt", "r") as a:
#         b = a.read()
#         print("sample.txt faylining mazmuni:")
#         print(b)
# except FileNotFoundError:
#     print("sample.txt fayli mavjud emas.")
#     print("Iltimos, faylni yaratish uchun bir paragraf yozing:")
#     user_input = input()  
#     with open("sample.txt", "w") as a:
#         a.write(user_input)
#     print("sample.txt fayli yaratildi va sizning matningiz yozildi.")
#########################################
# import string
# try:
#     with open("sample.txt", "r") as f:
#         a = f.read().lower() 
#         a = a.translate(str.maketrans("", "", string.punctuation))
#         b = a.split()
#         c = {}
#         for d in b:
#             if d in c:
#                 c[d] += 1
#             else:
#                 c[d] = 1
#         print("So'zlar chastotasi:")
#         for d, e in c.items():
#             print(f"{d}: {e}")
# except FileNotFoundError:
#     print("sample.txt fayli mavjud emas.")
#########################################
# import string
# from collections import Counter
# try:
#     with open("sample.txt", "r") as file:
#         a = file.read().lower()  
#         a = a.translate(str.maketrans("", "", string.punctuation))
#         b = a.split()
#         c = Counter(b)
#         d = sum(c.values())
#         e = c.most_common(5)
#         print(f"Umumiy so'zlar soni: {d}")
#         print("Eng ko'p uchragan 5 ta so'z:")
#         for f, g in e:
#             print(f"{f}: {g}")
#         with open("word_count_report.txt", "w") as h:
#             h.write(f"Umumiy so'zlar soni: {d}\n")
#             h.write("Eng ko'p uchragan 5 ta so'z:\n")
#             for f, g in e:
#                 h.write(f"{f}: {g}\n")
#     print("Natijalar 'word_count_report.txt' faylida saqlandi.")
# except FileNotFoundError:
#     print("sample.txt fayli mavjud emas.")
#########################################
# a = input("Iltimos, matn kiriting: ")
# with open("test_file.txt", "w") as b:
#     b.write(a)
# with open("test_file.txt", "r") as b:
#     c = b.read()
#     print("Fayldan o'qilgan matn:")
#     print(c)
#########################################
# import string
# try:
#     with open("sample.txt", "r") as f:
#         a = f.read().lower()  
#         for char in string.punctuation:
#             a = a.replace(char, "")
#         b = a.split()
#         c = {}
#         for word in b:
#             if word in c:
#                 c[word] += 1
#             else:
#                 c[word] = 1
#         d = len(b)
#         e = sorted(c.items(), key=lambda x: x[1], reverse=True)
#         e = e[:5]
#         print(f"Umumiy so'zlar soni: {d}")
#         print("Eng ko'p uchragan 5 ta so'z:")
#         for b, g in e:
#             if g == 1:
#                 print(f"{word} - {g} time")
#             else:
#                 print(f"{word} - {g} times")
# except FileNotFoundError:
#     print("sample.txt fayli mavjud emas.")
#########################################
# import string
# try:
#     with open("sample.txt", "r") as f:
#         c = f.read().lower() 
#         for a in string.punctuation:
#             c = c.replace(a, "")
#         b = c.split()
#         c = {}
#         for q in b:
#             if q in c:
#                 c[q] += 1
#             else:
#                 c[q] = 1
#         d = len(b)
#         e = sorted(c.items(), key=lambda x: x[1], reverse=True)
#         f = e[:5]
#         print("Word Count Report")
#         print(f"Total Words: {d}")
#         print("Top 5 Words:")
#         for q, g in f:
#             print(f"{q} - {g}")
#         with open("word_count_report.txt", "w") as h:
#             h.write("Word Count Report\n")
#             h.write(f"Total Words: {d}\n")
#             h.write("Top 5 Words:\n")
#             for q, g in f:
#                 h.write(f"{q} - {g}\n")
#     print("Natijalar 'word_count_report.txt' faylida saqlandi.")
# except FileNotFoundError:
#     print("sample.txt fayli mavjud emas.")
import string
from collections import Counter
a = int(input("Nechta eng ko'p uchragan so'zni ko'rsatishni xohlaysiz? Masalan, 3, 5, 10: "))
try:
    with open("sample.txt", "r") as f:
        b = f.read().lower()  
        b = b.translate(str.maketrans("", "", string.punctuation))
        c = b.split()
        d = Counter(c)
        e = d.most_common(a)
        print(f"Eng ko'p uchragan {a} ta so'z:")
        for f, g in e:
            print(f"{f} - {g} marta")        
except FileNotFoundError:
    print("sample.txt fayli mavjud emas.")
