#Raqamli ma'lumotlar turiga oid savollar:
# number = float(input("Enter a float number: "))
# n = round(number, 2) 
# print(n)
#############################################################
# n1 = input("Birinchi raqamni kiriting: ")
# n2 = input("Ikkinchi raqamni kiriting: ")
# n3 = input("Uchinchi raqamni kiriting: ")
# katta = max(n1, n2, n3)
# kichik = min(n1, n2, n3)
# print(f"Eng katta raqam>  {katta}")
# print(f"Eng kichik raqam> {kichik}")
##############################################################
# km = input("Masofani kilometrda kiriting: ")
# if km.replace('.', '', 1).isdigit() and km.count('.') <= 1:
#     km = int(km)  
#     metr = km * 1000
#     santimetr = km * 100000
#     print(f"{km} kilometrga teng {metr} metr yoki {santimetr} santimetr.")
###############################################################
# n1 = int(input("Birinchi sonni kirit: "))
# n2 = int(input("Ikkinchi sonni kirit: "))
# butun = n1 // n2
# qolgan = n1 % n2
# print(f"Sonni bolish natijasi butun qismi: {butun}")
# print(f"Qoldiq: {qolgan}")
###############################################################
# c = float(input("Gradusni Kiriting: "))
# if c >= -273.15:
#     f = (c * 9/5) + 32
#     print(f"{c}°C ga teng {f}°F.")
##############################################################
# n = int(input("Son kiriting: "))
# if n >= 0:
#     o = n % 10
# else:
#     o = (-n) % 10 
# print(f"{n} sonining oxirgi raqami: {o}")
#############################################################
# son = int(input("Biror raqam kiriting: "))
# if son % 2 == 0:
#     print(f"{son} juft son.")
# else:
#     print(f"{son} toq son.")
#############################################################
# ism = input("Ismingizni kiriting: ")
# ty = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2025 - ty
# print(f"{ism}, sizning yoshingiz {yosh}da:)")
############################################################
# a = input("So'z kiriting: ")
# print("So'zning uzunligi: ", len(a))
# print("katta harf: ", a.upper())
# print("kichik harf: ", a.lower())
###########################################################
# soz = input("So'z kiriting: ")
# if soz == soz[::-1]:
#     print("So'z palinandrom. ")
# else:
#     print("So'z palinandrom emas. ")
##########################################################
# def sozni_taxrirlash(matn):
#     unli = "aeiouAEIOU"  
#     unli_soni = 0
#     undosh_soni = 0
#     for harf in matn:
#         if harf.isalpha():  
#             if harf in unli:  
#                 unli_soni += 1
#             else:  
#                 undosh_soni += 1
#     return unli_soni, undosh_soni
# matn = input("Matnni kiriting: ")
# unli, undosh = sozni_taxrirlash(matn)
# print(f"Unli harflar: {unli}")
# print(f"Undosh harflar: {undosh}")
########################################################
# soz = input("Gap kiriting: ")
# alsoz = input("O'zgaruvchi so'zni kiriting: ")
# orsoz = input("Uni almashtirish uchun so'zni kiriting: ")
# ysoz = soz.replace(alsoz, orsoz)
# print("Yangi tuzilgan gap:", ysoz)
#######################################################
# soz = input("Matnni kiriting: ")
# if soz:
#     print(f"Birinchi harf: {soz[0]}")
#     print(f"Oxirgi harf: {soz[-1]}")
# else:
#     print("Matn bo'sh!")
######################################################
# m = input("Matnni kiriting: ")
# teskari = ""
# for a in m:
#     teskari = a + teskari
# print("Teskari matn:", teskari)
#####################################################
# s = input("Jumlani kiriting: ")
# words = s.split()  
# sr = len(words)  
# print("So'zlar soni:", sr)
###################################################
# soz = input("Matnni kiriting: ")
# sr = any(char.isdigit() for char in soz)
# if sr:
#     print("Matn raqamlarni o'z ichiga oladi.")
# else:
#     print("Matn raqamlarni o'z ichiga olmaydi.")
######################################################
# soz = input("So'zlar ro'yxatini kiriting (bo'sh joy bilan ajratilgan): ").split()
# belgi = input("Ajratish belgisini kiriting (masalan, -, ,): ")
# sozniajrat = belgi.join(soz)
# print("Birlashtirilgan matn:", sozniajrat)
####################################################
# string = input("Matnni kiriting: ")
# space_string = string.replace(" ", "")
# print("Bo'sh joylarsiz matn:", space_string)
# Foydalanuvchidan ikkita matnni olish
##################################################
# string1 = input("Birinchi matnni kiriting: ")
# string2 = input("Ikkinchi matnni kiriting: ")
# if string1 == string2:
#     print("Matnlar teng.")
# else:
#     print("Matnlar teng emas.")
##################################################
# soz = input("Jumlani kiriting: ")
# gap = soz.split()
# acronym = "".join(word[0].upper() for word in gap)
# print("qisqartma:", acronym)
#################################################
# m = input("Matnni kiriting: ")
# b = input("O'chiriladigan belgini kiriting: ")
# s = m.replace(b, "")
# print("O'zgartirilgan matn:", s)
#################################################
# a = input("Matnni kiriting: ")
# b = "aeiouAEIOU"
# c = "".join("*" if char in b else char for char in a)
# print("O'zgartirilgan matn:", c)
#################################################
# a = input("Matnni kiriting: ")
# b = input("Boshlanish so'zini kiriting: ")
# c = input("Tugash so'zini kiriting: ")
# if a.startswith(b) and a.endswith(c):
#     print("Matn berilgan so'zlar bilan boshlanadi va tugaydi.")
# else:
#     print("Matn berilgan so'zlar bilan boshlanmaydi yoki tugamaydi.")
#################################################
# ism = input("Ism kiriting: ")
# parol = input("Parol kiriting: ")
# if ism and parol:
#     print("Ism va parol to'g'ri kiritildi.")
# else:
#     print("Ism yoki parol bo'sh bo'lmasligi kerak!")
#################################################
# n1 = float(input("Birinchi sonni kiriting: "))
# n2 = float(input("Ikkinchi sonni kiriting: "))
# if n1 == n2:
#     print("Parol to'gri! ;)")
# else:
#     print("Parol notog'ri.")
#################################################
# n = int(input("Sonni kiriting: "))
# if n > 0 and n % 2 == 0:
#     print("Son musbat va juft.")
# else:
#     print("Son musbat emas yoki juft emas.")
#################################################
# n1 = float(input("Birinchi sonni kiriting: "))
# n2 = float(input("Ikkinchi sonni kiriting: "))
# n3 = float(input("Uchinchi sonni kiriting: "))
# if n1 != n2 and n1 != n3 and n2 != n3:
#     print("Barcha sonlar turlicha.")
# else:
#     print("Ba'zi sonlar bir xil.")
##################################################
# s1 = input("Birinchi matnni kiriting: ")
# s2 = input("Ikkinchi matnni kiriting: ")
# if len(s1) == len(s2):
#     print("Matnlarning uzunligi bir xil.")
# else:
#     print("Matnlarning uzunligi bir xil emas.")
##################################################
# n = int(input("Sonni kiriting: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("Son 3 va 5 ga bo'linadi.")
# else:
#     print("Son 3 va 5 ga bo'linmaydi.")
##################################################
# n1 = float(input("Birinchi sonni kiriting: "))
# n2 = float(input("Ikkinchi sonni kiriting: "))
# if n1 + n2 > 50.8:
#     print("Sonlarning yig'indisi 50.8 dan katta.")
# else:
#     print("Sonlarning yig'indisi 50.8 dan kichik yoki teng.")
