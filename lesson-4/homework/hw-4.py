# num1 = [1, 1, 2]
# num2 = [2, 3, 4]
# num3 = num1 + num2
# print(num3)
#########################################
# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# num3 = num1 + num2
# print(num3)
#########################################
# num1 = [1, 1, 2, 3, 4, 2]
# num2 = [1, 3, 4, 5]
# a = [item for item in num1 if item not in num2] + [item for item in num2 if item not in num1]
# print(a)
#########################################
# n = 5
# for i in range(1, n + 1):
#     print(i * i)
#########################################
# str = "hello"
# str2 = str[:3] + "_" + str[3:]
# print(str2)
#########################################
# a = "assalom"
# b = a[:3] + "_" + a[3:]
# print(b)
#########################################
# a = "abcabcdabcdeabcdefabcdefg"
# b = a.replace("abc", "abc_")
# print(b)
#########################################
# import random
# num = random.randint(1, 100)
# print("Randomniy raqam:", num)
#########################################
# import random
# num = random.randint(1, 100)
# num1 = int(input("Raqamni taxmin qiling 1 dan 100 gacha bo'lgan:"))
# if num1 > num:
#     print("Juda baland!")
# elif num1 < num:
#     print("Juda past!")
# else:
#     print("To'g'ri! Siz raqamni taxmin qildingiz.")
#########################################
# import random
# num = random.randint(1, 100)
# while True:    
#     num1 = int(input("Raqamni taxmin qiling 1 dan 100 gacha bo'lgan: "))
#     if num1 > num:
#         print("Juda baland!")
#     elif num1 < num:
#         print("Juda past!")
#     else:
#         print("To'g'ri taxmin qildingiz!")
#         break  
#########################################
# print("O'yin boshlanmoqda...")
# restart = input("Yana o'ynaysizmi? (Y/YES/y/yes/ok): ").strip().lower()
# if restart in ['y', 'yes', 'ok']:
#     print("O'yin yana boshlanmoqda...")
# else:
#     print("O'yinni tugatdingiz. Rahmat!")
#########################################
# import re
# cod = input("Parolingizni kiriting: ")
# if len(cod) < 8:
#     print("Parol kamida 8 belgidan iborat bo'lishi kerak.")
# elif not re.search(r'[a-z]', cod):
#     print("Parolda kamida birta kichik harf bo'lishi kerak.")
# elif not re.search(r'[A-Z]', cod):
#     print("Parolda kamida birta katta harf bo'lishi kerak.")
# elif not re.search(r'[0-9]', cod):
#     print("Parolda kamida birta raqam bo'lishi kerak.")
# elif not re.search(r'[@$!%*?&]', cod):
#     print("Parolda kamida birta maxsus belgi bo'lishi kerak (@, $, !, %, *, ?, &).")
# else:
#     print("Parol to'g'ri.")
#########################################
# import re
# password = input("Parolingizni kiriting: ")
# if len(password) < 8:
#     print("Parol juda qisqa,  Kamida 8ta ishora bolishi kerak.")
# elif not re.search(r'[a-z]', password):
#     print("Parolda kamida birta kichik harf bo'lishi kerak.")
# elif not re.search(r'[A-Z]', password):
#     print("Parolda kamida birta katta harf bo'lishi kerak.")
# elif not re.search(r'[0-9]', password):
#     print("Parolda kamida birta raqam bo'lishi kerak.")
# elif not re.search(r'[@$!%*?&]', password):
#     print("Parolda kamida birta maxsus belgi bo'lishi kerak (@, $, !, %, *, ?, &).")
# else:
#     print("Parol to'g'ri.")
#########################################
# import re
# cod = input("Parolingizni kiriting: ")
# if len(cod) < 8:
#     print("Parol juda qisqa.Kamida 8 bolishi kk")
# elif not re.search(r'[a-z]', cod):
#     print("Parolda kamida birta kichik harf bo'lishi kerak.")
# elif not re.search(r'[A-Z]', cod):
#     print("Parolda katta harf bo'lishi kerak.")
# elif not re.search(r'[0-9]', cod):
#     print("Parolda kamida birta raqam bo'lishi kerak.")
#########################################
# import re
# cod = input("Parolingizni kiriting: ")
# if len(cod) < 8:
#     print("Parol juda qisqa.Kamida 8 bolishi kk.")
#     print("Parolda kamida birta kichik harf bo'lishi kerak.")
# elif not re.search(r'[A-Z]', cod):
#     print("Parolda kamida birta katta harf bo'lishi kerak.")
# elif not re.search(r'[0-9]', cod):
#     print("Parolda kamida birta raqam bo'lishi kerak.")
# else:
#     print("Parol kuchli.")
#########################################
# import random
# a = ["tosh", "qog'oz", "qaychi"]
# b = random.choice(a)
# c = input("Tanlovingizni kiriting (tosh, qog'oz, or qaychi): ").lower()
# if c not in a:
#     print("Yaroqsiz tanlov! Iltimos, tosh, qog'oz yoki qaychi tanlang.")
# else:
#     print(f"Sizning tanlovingiz: {c}")
#     print(f"Kompyuterning tanlovi: {b}")
#     if c == b:
#         print("Bular teng!")
#     elif (c == "tosh" and b == "qaychi") or \
#          (c == "qog'oz" and b == "tosh") or \
#          (c == "qaychi" and b == "qog'oz"):
#         print("Siz yutdingiz!")
#     else:
#         print("Siz yutqazdingiz!")
#########################################
# import random
# a = ["tosh", "qog'oz", "qaychi"]
# b = input("Tanlovingizni kiriting (tosh, qog'oz, or qaychi): ").lower()
# if b not in a:
#     print("Yaroqsiz tanlov! Iltimos'tosh', 'qog'oz', or 'qaychi'.")
# else:
#     c = random.choice(a)
#     print(f"Sizning tanloviz: {b}")
#     print(f"Kompyuterning tanlovi: {c}")
#     if b == c:
#         print("Bular teng!")
#     elif (b == "tosh" and c == "qaychi") or \
#          (b == "qog'oz" and c == "tosh") or \
#          (b == "qaychi" and c == "qog'oz"):
#         print("Siz yutdingiz!")
#     else:
#         print("Siz yutqazdingiz!")
#########################################
import random
a = ["tosh", "qog'oz", "qaychi"]
b = 0
c = 0
d = int(input("Qancha o'ynashni xohlaysiz? "))
for s in range(1, d + 1):
    print(f"\nRound {s}")
    b = input("Tanlovingizni kiriting(tosh, qog'oz, or qaychi): ").lower()
    if b not in a:
        print("Yaroqsiz tanlov! Iltimos tanlang 'tosh', 'qog'oz', or 'qaychi'.")
        continue
    c = random.choice(a)
    print(f"Sizning tanlovingiz: {b}")
    print(f"Kompyuter tanlovi: {c}")
    if b == c:
        print("Bular teng")
    elif (b == "tosh" and c == "qaychi") or \
         (b == "qog'oz" and c == "tosh") or \
         (b == "qaychi" and c == "qog'oz"):
        print("Siz bu turda g'alaba qozonasiz!")
        b += 1
    else:
        print("Siz bu turda yutqazasiz!")
        c += 1
print("\nO'yin tugadi!")
print(f"Yakuniy ball - Siz: {b} Kompyuter: {c}")
if b > c:
    print("Siz o'yinda g'alaba qozonasiz!")
elif b < c:
    print("Kompyuter o'yinda g'alaba qozonadi!")
else:
    print("O'yin teng!")
