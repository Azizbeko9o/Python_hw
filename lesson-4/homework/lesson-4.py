# from collections import defaultdict, OrderedDict
# person = defauldict(list)\
# person = {}
# person['name'] = 'John'
# skills = person.get('skills)
# if not skills:
#     person['skills] = []
# person.setdefault('skills', []).append('c#')
# person['skills'].append('python')
# person['skills'].append('django')
# person['skills'].append('writing')
# print(person['skills'])
# authenticated = True
# if authenticated == True:
#     print("You are logged in")
# age = 20
# if age > 18:
#     print("You can vote")
# authenticated = True
# if authenticated:
#     print("You logged in")
# authenticated = False
# if authenticated:
#     print("You logged in")
#     print("Welcome")
# print("Outside if statement")
# if authenticated:
#     pass
# print("Other stuff")
# a = 1
# if a:
#     print("Truthy")
# else:
#     print("Falthy")
# a = 0
# if a:
#     print("Truthy")
# else:
#     print("Falthy")
# a = 1
# print(bool(a))
# if a:
#     print("Truthy")
# else:
#     print("Falthy")
# age = int(input("Enter you age "))
# print(bool(age))
# if age:
#     print("Truthy")
# else:
#     print("Falthy")
# age = None
# if age is None:
#     print("Your age is", age)
# else:
#     print("Age not defined")
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(a is b)
# x = 5
# y = 5
# print(x is y)
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a # reference assigment
# print(a == b)
# print(a is c)
# age = 18
# car = "BWM"
# if age >= 18 and car in ["Honda", "BMW", "Toyota"]:
#     print("True")
# else:
#     print("false")
# age = 17
# car = "BWM"
# if age >= 18 or car in ["Honda", "BMW", "Toyota"]:
#     print("true")
# else:
#     print("false")
# age = 10
# if age < 0:
#     print("Incorrect number for age")
# elif age < 18:
#     print("You can vote")
# elif age < 150:
#     print("You can not vote")
# else:
#     print("Incorrect number for age. Humans can not live that long")
#########################################  
               # LOOPS #
#########################################
# n = 10
# while n < 20:
#     print("Executed")
#     n += 1
# print("Outside loop")
# n = 10
# while n <= 20:
#     print("Executed n =", n)
#     n += 1
# print("Outside loop")
# while True:
#     print("Still running")
#     break
# cnt = 1
# while True:
#     print("cnt += 1")
#     if cnt == 10:
#        break
# while True:
#     a = int(input('a = '))
#     b = int(input('b = '))
#     operation = input("Choose: (+, -, *, /,)")
#     if operation == '+':
#         print('a = b', a+b)
#     elif operation == '-':
#         print('a - b=', a-b)
#     q = input('Dou you want to run again?')
#     if q.lower() in ['q', 'quit', 'n', 'no']:
#         break
# cnt = 1
# while cnt < 30:
#     cnt += 1
#     if cnt == 10:
#        continue
#     print("cnt=", cnt)
# cnt = 1
# while cnt < 30:
#     cnt += 1
#     if cnt == 10:
#        break
#     print("cnt=", cnt)
# cnt = 1
# while cnt < 30:
#     cnt += 1
#     if cnt in (10, 16, 28):
#        continue
#     print("cnt=", cnt)
# l = [1, 2, 3]
# i = 0
# check_number = 5
# while i < len(l):
#     if l[i] == check_number:
#         print("Found")
#         break
#     i += 1
# else:
#     print("Number not found")
##########################################
               #FOR LOOP
#########################################
# m = [1, 2, 3]
# i = 0
# while i < len(m):
#     print(m[i])
#     i += 1
# m = [1, 2, 3]
# o = []
# i = 0
# while i < len(m):
#     a = m[i]
#     o.append(a**2)
#     i += 1
#     print(o)
# m = [1, 2, 3]
# o = []
# i = 0
# for a in m:
#     print(a)
# m = [1, 2, 3]
# o = []
# i = 0
# for a in m:
#     o.append(a**2)
# print(0)
# m = 'asjhdjshd'
# for char in m:
#     print(char)
# users = {'user1': 'John', 'user2': 'Adam', 'user3': 'Josh'}
# for user in users:
#    print(user, users[user])
users = {'user1': 'John', 'user2': 'Adam', 'user3': 'Josh'}
for user in users:
    users.keys()