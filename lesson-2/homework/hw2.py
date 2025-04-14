##########################################################
# num=[1,2,3,4]
# s=set(num)
# print(s)
##########################################################
# num = {1, 2, 3, 4, 5}
# a = 3
# if a in num:
#     num.remove(a)
# print(num)  
##########################################################
# num = {1, 2, 3, 4, 5}
# num.clear()  
# print(num) 
##########################################################
# my_set = {1, 2, 3}
# if my_set:
#     print("To'plam bo'sh emas")
# else:
#     print("To'plam bo'sh")
##########################################################
# num1 = {1, 2, 3, 4}
# num2 = {3, 4, 5, 6}
# sym_diff = num1 ^ num2
# sym_diff_method = num1.symmetric_difference(num2)
# print(sym_diff)  
# print(sym_diff_method)  
##########################################################
# num = {1, 2, 3, 4}
# num.add(5)
# print(num) 
# num.add(3)
# print(num) 
##########################################################
# num = {1, 2, 3, 4, 5}
# numb = num.pop()
# print("Olib tashlangan element:", numb)  
# print("Yangi elementlar:", num) 
##########################################################
# num = {10, 20, 30, 40, 50}
# m_e = max(num)
# print("Eng katta qiymat:", m_e) 
##########################################################
# num = {10, 20, 30, 40, 50}
# m_e = min(num)
# print("Eng kichik qiymat:", m_e) 
##########################################################
# numb = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set = {num for num in numb if num % 2 == 0}
# print("Juft raqamlar: ", set)
##########################################################
# numb = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set = {num for num in numb if num % 2 != 0}
# print("Toq raqamlar: ", set)
##########################################################
# num = set(range(1, 11))
# print(num)  
##########################################################
# num1 = [1, 2, 3, 4, 5]
# num2 = [4, 5, 6, 7, 8]
# set = set(num1 + num2)
# print(set)  
##########################################################
# num1 = {1, 2, 3, 4}
# num2 = {5, 6, 7, 8}
# num3 = num1.isdisjoint(num2)
# print(num3)  
##########################################################
# num = [1, 2, 3, 4, 5, 3, 4, 2, 6]
# list = list(set(num))
# print(list) 
########################################################## 
# string = ['apple', 'banana', 'orange', 'apple', 'banana']
# list = len(set(string))
# print("Noyob elementlar soni:", list) 
##########################################################
# str = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# k = 'name'
# if k in str:
#     a = str[k]
# else:
#     a = 'Key not found'
# print(a)
##########################################################
# str = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# k = 'name'
# if k in str:
#     print(f"'{k}' kaliti lug'atda mavjud.")
# else:
#     print(f"'{k}' kaliti lug'atda mavjud emas.")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = len(a)
# print(f"Lug'atdagi kalitlar soni: {b}")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = list(a.keys())
# print(f"Lug'atdagi barcha kalitlar: {b}")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = list(a.values())
# print(f"Lug'atdagi barcha qiymatlar: {b}")
##########################################################
# a1 = {'name': 'Alice', 'age': 25}
# a2 = {'city': 'Wonderland', 'country': 'Fiction'}
# a3 = {**a1, **a2}
# print(f"Birlashtirilgan lug'at: {a3}")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = 'age'
# c = a.pop(b, None)
# if c is not None:
#     print(f"Kalit '{b}' o'chirildi.")
# else:
#     print(f"Kalit '{b}' lug'atda mavjud emas.")
# print("Yangi lug'at:", a)
##########################################################
# empty_dict = dict()
# print(f"Yangi bo'sh lug'at: {empty_dict}")
##########################################################
# a = {}
# if len(a) == 0:
#     print("Lug'at bo'sh.")
# else:
#     print("Lug'atda elementlar mavjud.")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = 'age'
# if b in a:
#     print(f"Kalit: {b}, Qiymat: {a[b]}")
# else:
#     print(f"Kalit '{b}' lug'atda mavjud emas.")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = 'age'
# c = 26
# a[b] = c
# print(f"Yangilangan lug'at: {a}")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland', 'occupation': 'Alice'}
# b = 'Alice'
# c = list(a.values()).count(b)
# print(f"Qiymat '{b}' lug'atda {c} marta uchraydi.")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
# b = {v: k for k, v in a.items()}
# print(f"Teskari lug'at: {b}")
##########################################################
# a = {'name': 'Alice', 'age': 25, 'city': 'Wonderland', 'occupation': 'Engineer'}
# b = 'Alice'
# c = [key for key, value in a.items() if value == b]
# print(f"Qiymat '{b}' ga ega kalitlar: {c}")
##########################################################
# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# c = {}
# for i in range(len(a)):
#     c[a[i]] = b[i]
# print(c)
##########################################################
# a = {
#     'key1': {'subkey1': 1, 'subkey2': 2},
#     'key2': 10,
#     'key3': {'subkey3': 3}
# }
# for b, c in a.items():
#     if isinstance(c, dict):
#         print(f"Bu uchun '{b}' lug'at bor.")
#     else:
#         print(f"Bu ucuhun '{b}' lug'at yoq.")
##########################################################
# a = {
#     'key1': {'subkey1': 10, 'subkey2': 20},
#     'key2': {'subkey3': 30, 'subkey4': 40},
#     'key3': 50
# }
# b = a['key1']['subkey1']
# print(b)
##########################################################
# from collections import defaultdict
# a = defaultdict(lambda: 0)
# a['key1'] = 10
# a['key2'] = 20
# print(a['key1']) 
# print(a['key3'])  
##########################################################
# a = {
#     'key1': 10,
#     'key2': 20,
#     'key3': 10,
#     'key4': 30,
#     'key5': 20
# }
# b = set(a.values())
# c = len(b)
# print(c)
##########################################################
# a = {
#     'c': 3,
#     'a': 1,
#     'b': 2
# }
# b = {k: a[k] for k in sorted(a)}
# print(b)
##########################################################
# a = {
#     'a': 3,
#     'b': 1,
#     'c': 2
# }
# b = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}
# print(b)
##########################################################
# a = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40
# }
# b = {c: d for c, d in a.items() if d > 20}
# print(b)
##########################################################
# a1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# a2 = {
#     'b': 4,
#     'd': 5,
#     'e': 6
# }
# a3 = set(a1.keys()) & set(a2.keys())
# if a3:
#     print(f"Bu bir xil kalitlar: {a3}")
# else:
#     print("Bir xil kalit yoq.")
##########################################################
# a = (('a', 1), ('b', 2), ('c', 3))
# b = dict(a)
# print(b)
##########################################################
# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# b, c = next(iter(a.items()))
# print(f"Birinchi kalit: {b}, Birinchi qiymat: {c}")
##########################################################
