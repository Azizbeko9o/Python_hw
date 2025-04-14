numbers = [123, 234, 123, 235, 123, 236, 123, 213]
numbers.count(123)
4
def sum_of_elements(c):
    a = 0
    for b in c:
        if b:  
            a += b
    return a
m = [1, 2, 3, 4, 5]
r = sum_of_elements(m)
print(f"Elementlar yig'indisi: {r}")
Elementlar yig'indisi: 15
a = [675, 543, 342, 231, 123]
b = a[0]  
for c in a:  
    if c > b:  
        b = c  
print(f"Eng katta element: {b}")
Eng katta element: 675
n = [123, 223, 334, 423, 123]

s = n[0]
for i in n:
    if i < s:
        s = i
print(f"Eng kichik element: {s}")
Eng kichik element: 123
a = [1, 2, 3, 4, 5]
b = 3

if b in a:
    print(f"Element {b} ro'yxatda mavjud.")
else:
    print(f"Element {b} ro'yxatda mavjud emas.")
Element 3 ro'yxatda mavjud.
m = [1, 2, 3, 4, 5]
if m:
    f = m[0]
    print(f"Ro'yxatning birinchi elementi: {f}")
else:
    print("Ro'yxat bo'sh, birinchi element yo'q.")
Ro'yxatning birinchi elementi: 1
names = ['John', 'Mark', 'Mete', 'Harry']
names.append('Jerry')
names
['John', 'Mark', 'Mete', 'Harry', 'Jerry']
names = ['John', 'Mark', 'Mete', 'Harry', 'Jerry']
names.reverse()
names
['Jerry', 'Harry', 'Mete', 'Mark', 'John']
names = ['John', 'Mark', 'Mete', 'Harry', 'Jerry']
names.sort()
sorted(names)
['Harry', 'Jerry', 'John', 'Mark', 'Mete']
names = ['John', 'Mark', 'Mete', 'Harry', 'Jerry','John']
names.remove('John')
names
['Mark', 'Mete', 'Harry', 'Jerry', 'John']
numbers = [1, 2, 3, 4, 5]
num = 6
index = 5  
numbers.insert(index, num)
print(f"Yangi ro'yxat: {numbers}")
Yangi ro'yxat: [1, 2, 3, 4, 5, 6]
numers = [1, 2, 3, 4, 5]
num =  2
e = numbers.index(num)
print(f"Element {num} ning birinchi uchrashgan indeksi: {e}")
Element 2 ning birinchi uchrashgan indeksi: 1
a = []
b = not a  
print(f"Ro'yxat bo'shmi? {b}")
Ro'yxat bo'shmi? False
a = [1]
b = not a
print(f"Ro'yhat bo'shmi? {b}")
Ro'yhat bo'shmi? False
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
juft = 0
for num in sonlar:
    if num % 2 == 0: 
        juft += 1  
print(f"Ro'yxatda {juft} ta juft son mavjud.")
Ro'yxatda 4 ta juft son mavjud.
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
toq = 0
for num in sonlar:
    if num % 2 != 0:  
        toq += 1  
print(f"Ro'yxatda {toq} ta toq son mavjud.")
Ro'yxatda 4 ta toq son mavjud.
list1 = ['AZIZBEK', 'BOBUR', 'SANJAR']
list2 = ['SHOHRUH', 'DIYORBEK', 'AKMAL']
list3 = list1 + list2
print(f"Yangi birlashgan ro'yxat: {list3}")
Yangi birlashgan ro'yxat: ['AZIZBEK', 'BOBUR', 'SANJAR', 'SHOHRUH', 'DIYORBEK', 'AKMAL']
number = [1, 2, 3, 4, 5, 6]
num = [3, 4, 5]
if num in (numers):
    print("Ro'yxatda mavjud.")
else:
    print("Ro'yxatda mavjud emas.")
Ro'yxatda mavjud emas.
number = [1, 2, 3, 4, 5, 6, 7]
element = 7
nelement = 8
if element in number:
    index_of_element = number.index(element)
    number[index_of_element] = nelement
print(f"Yangi ro'yxat: {number}")
Yangi ro'yxat: [1, 2, 3, 4, 5, 6, 8]
num = [1, 2, 3, 4, 5]
if len(num) >= 2:
    l = sl = float('-inf')      
    for num in num:
        if num > l:
            sl = l  
            l = num  
        elif num > sl and num != l:
            sl = num  
    print(f"Ikkinchi eng katta element: {sl}")
else:
    print("Ro'yxatda kamida 2 ta element bo'lishi kerak.")
Ikkinchi eng katta element: 4
m = [1, 2, 3, 4, 5]
if len(m) >= 2:
    s = s_s = float('inf')   
    for num in m:
        if num < s:
            s_s = s  
            s = num  
        elif num < s_s and num != s:
            s_s = num  
    print(f"Ikkinchi eng kichik element: {s_s}")
else:
    print("Ro'yxatda kamida 2 ta element bo'lishi kerak.")
Ikkinchi eng kichik element: 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
n = [num for num in numbers if num % 2 == 0]
print(f"Juft sonlar: {n}")
Juft sonlar: [2, 4, 6, 8]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
n = [num for num in numbers if num % 2 != 0]
print(f"Toq sonlar: {n}")
Toq sonlar: [1, 3, 5, 7]
number = [1, 2, 3, 4, 5]
uzun = len(number)
print(f"Ro'yxatdagi elementlar soni: {uzun}")
Ro'yxatdagi elementlar soni: 5
string = ['Azizbek', 'Shohruh', 'Akmal', 'Anvar']
copy_str = string.copy()
print(f"Birinchi ro'yxat: {string}")
print(f"Nusxa ro'yxat: {copy_str}")
Birinchi ro'yxat: ['Azizbek', 'Shohruh', 'Akmal', 'Anvar']
Nusxa ro'yxat: ['Azizbek', 'Shohruh', 'Akmal', 'Anvar']
num = [1, 2, 3, 4, 5, 6]
uzun = len(num)
if uzun % 2 == 0:
    nn = num[uzun//2 - 1:uzun//2 + 1]  
else:
    nn = num[uzun//2]  

print(f"O'rtadagi element(lar): {nn}")
O'rtadagi element(lar): [3, 4]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[2:6]  
c = max(b)
print(f"List ichidagi list : {b}")
print(f"List eng katta element: {c}")
List ichidagi list : [3, 4, 5, 6]
List maksimal element: 6
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[2:6]  
c = min(b)
print(f"List ichidagi list : {b}")
print(f"List eng kichig element: {c}")
List ichidagi list : [3, 4, 5, 6]
List eng kichig element: 3
num = [10, 20, 30, 40, 50]
index = 2
if index < len(num):
    del num[index]
print(f"Yangi ro'yxat: {num}")
Yangi ro'yxat: [10, 20, 40, 50]
num = [1, 2, 3, 4, 5]
tartib = all(num[i] <= num[i + 1] for i in range(len(num) - 1))
print(f"Ro'yxat tartiblanganmi? {tartib}")
Ro'yxat tartiblanganmi? True
num = [12, 23, 34, 45]
takror = 3
new_num = [elem for elem in num for _ in range(takror)]
print(f"Yangi ro'yxat: {new_num}")
Yangi ro'yxat: [12, 12, 12, 23, 23, 23, 34, 34, 34, 45, 45, 45]
list1 = [3, 1, 4, 5]
list2 = [2, 6, 8, 7]
list3 = list1 + list2
list = sorted(list3)
print(list)
[1, 2, 3, 4, 5, 6, 7, 8]
def a(lst, k):
    k = k % len(lst)
    for i in range(k):
        last_element = lst.pop()  
        lst.insert(0, last_element)  
    return lst
b = [1, 2, 3, 4, 5]
k = 2
a = a(b, k)
print(a)  
[4, 5, 1, 2, 3]
a = 1
b = 10
num = []
for i in range(a, b):
    num.append(i)
print(num) 
[1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [1, -2, 3, -4, 5, -6]
numbers = 0
for num in nums:
    if num > 0:
        numbers += num
print(numbers)  
-12
nums = [1, -2, 3, -4, 5, -6]
numbers = 0
for num in nums:
    if num < 0:
        numbers += num
print(numbers)  
-12
nums = [1, 2, 3, 2, 1]
palindrom = True
for i in range(len(nums) // 2):
    if nums[i] != nums[-(i + 1)]:
        palindrom = False
        break
print(palindrom)  
True
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = 3
t = []
for i in range(0, len(n), s):
    t.append(n[i:i + s])
print(t)  
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [1, 2, 2, 3, 4, 4, 5, 1]
u = []
for num in n:
    if num not in u:
        u.append(num)
print(u)  
[1, 2, 3, 4, 5]
num = (1, 2, 3, 4, 2, 5, 2)
e = 2
c = num.count(e)
print(c)  
3
n = (1, 2, 3, 4, 5)
max_e = max(n)
print(max_e)  
5
num = (1, 2, 3, 4, 5)
min_e = min(num)
print(min_e)  
1
num = (1, 2, 3, 4, 5)
max_e = max(num)
print(max_e)  
5
n = (1, 2, 3, 4, 5)
e = 3
t = e in n
print(t)  
True
m = (1, 2, 3, 4, 5)
first_e = m[0] if m else "Bo'sh tuple"
print(first_e) 
1
m = (1, 2, 3, 4, 5)
last_e = m[-1] if m else "Bo'sh tuple"
print(last_e)  
5
m = (1, 2, 3, 4, 5)
tuple_l = len(m)
print(f"Elementlar soni: {tuple_l}")  
Elementlar soni: 5
num = (1, 2, 3, 4, 5)
new = num[:3]
print(new)  
(1, 2, 3)
n = (1, 2, 3)
n2 = (4, 5, 6)
n3 = n + n2 
print(n3)
(1, 2, 3, 4, 5, 6)
list = ()
a = "Bo'sh" if not list else "Bo'sh emas"
print(a)
Bo'sh
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
element = 2
indec = [i for i, x in enumerate(num) if x == element]
print(indec)
[1]
num = (1, 2, 3, 4, 5)
s = sorted(num)
sc = s[-2] if len(s) > 1 else None
print(sc)
4
num = (1, 2, 3, 4, 5)
s = sorted(num)
sc = s[1] if len(s) > 1 else None
print(sc)
2
e = 5
n = (e,)
print(n)
(5,)
num = [1, 2, 3, 4, 5]
n = tuple(num)
print(n)
(1, 2, 3, 4, 5)
numb = (1, 2, 3, 4, 5, 6)
a = numb == tuple(sorted(numb))
print(a)
True
num = (1, 2, 3, 4, 5, 6, 7)
s = num[2:6]
a = max(s)
print(a)
6
num = (1, 2, 3, 4, 5, 6, 7)
s = num[2:6]
a = min(s)
print(a)
3
num = (1, 2, 3, 4, 5, 2)
el = 2
t = list(num)
if el in t:
    t.remove(el)
new_t = tuple(t)
print(new_t)
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
s = 3
n_t = tuple(tuple(num[i:i + s]) for i in range(0, len(num), s))
print(n_t)
((1, 2, 3), (4, 5, 6), (7, 8, 9))
num = (1, 2, 3)
r_c = 3
r_t_d = tuple(x for x in num for _ in range(r_c))
print(r_t_d)
(1, 1, 1, 2, 2, 2, 3, 3, 3)
start = 1
stop = 10
r_t = tuple(range(start, stop + 1))
print(r_t)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num = (1, 2, 3, 4, 5)
r = num[::-1]
print(r)
(5, 4, 3, 2, 1)
num = (1, 2, 3, 2, 1)
i = num == num[::-1]
print(i)
True
num = (1, 2, 3, 2, 4, 5, 3)
u = tuple(sorted(set(num), key=num.index))
print(u)
(1, 2, 3, 4, 5)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a | b
print(c)  
{1, 2, 3, 4, 5, 6}
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a & b
print(c)  
{3, 4}
a = {1, 2, 3, 4}
b= {3, 4, 5, 6}
c = a - b
print(c)  
{1, 2}
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = a.issubset(b)
print(c)  
True
a = {1, 2, 3, 4, 5}
b = 3
c = b in a
print(c)
True
num = {1, 2, 3, 4, 5}
set = len(num)
print(set)  
5
num1 = [1, 2, 3, 4, 5, 1, 2, 3]
u_s = set(num1)
print(u_s)
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
