##### numeric
import math # built in library 
# pow = ** - built-in function
 # min, max
 # int
 # float
 # complex
# a = 200_000_000
# b = 1.3e10
# print(b)
# print(type(b))

# print(math.sqrt(25))
# c = 7 + 5j
# print(c.real)
# print(c.imag)
# print(a.real)
###########################################
##### string_into
# a = '''a'''
# print(type(a)) 
# ' - single quote '
# " - double quote "
# \ - back slash
# / - forward slash
# \n - newLine character
# \' - single qoute
# \" - double qoute
# \t - tab 
# \\ - backlash
# + stringlar uchun "concatention"

###########################################
# a = """Hello 
#        World"""
# print(a)

# b = "Hello \nWorld"
# print(b)

# c = "Hello \nW\norld"
# print(c)
# i = "I'm a student"
# print(i)
# m = 'I'm a student' # bu xato
# print(m)
# p = 'I"m a student' 
# print(p)
# t = """I'm a " student""" 
# print(t)
# s = 'I\'m a \" student' 
# print(s)
# v = 'I\'m a student' 
# print(v)
# r = "I\"m a student" 
# print(r)
# q = "I\'m a student" 
# print(q)
# q = 'I\'m a student' 
# print(q)
# w = 'I\'m a stu\tdent' 
# print(w)
# e = "Hello \\nWo\\nrld"
# print(e)
# directorry = "D:\\dir\\lesson-1.py"
# print(directorry)
# directorry = r"D:\dir\lesson-1.py"
# print(directorry)
# directorry = r"D:\dir\lesson-1.py"
# print(type(directorry))
# print(directorry)
####### string_simple_app
# surname = input("what is your surname ")
# age = int(input("Age: "))
# print("Your surname is surname and you age years old. ")
# surname = input("what is your surname ")
# age = int(input("Age: "))
# print("Your surname is " + surname + " surname and you age years old. ")
# surname = input("what is your surname ")
# age = int(input("Age: "))
# print("Your surname is " + surname + " surname and you " + str(age) + " age years old. ")
# surname = "Ne'matov" #input("what is your surname ")
# age = 20 # int(input("Age: "))
# print("Your surname is " + surname + " surname and you " + str(age) + " are years old. ")
# surname = "Ne'matov"
# age = 20
# print(f"Your  surname is {surname} and you are {age} years old. ")
# surname = "Ne'matov"
# age = 20
# print("Your  surname is {surname} and you are {age} years old. ".format(surname=surname, age=age))
# surname = "Ne'matov"
# age = 20
# print("Your   surname is {} and you are {} years old. ".format(surname, age))
# surname = "Ne'matov"
# age = 20
# print("Your surname is {surname} and you are {age} years old. ".format(surname=surname, age=age))
# surname = "Ne'matov"
# age = 20
# print("Your surname is {fsurname} and you are {Age} years old. ".format(fsurname=surname, Age=age))
# name1 = "John"
# name2 = "Mete"
# print(f'{name1} - first name')
# print(f'{name2} - second name')
# name1 = "John"
# name2 = "Mete"
# print(f'{name1:<8} - first name')
# print(f'{name2:<8} - second name')
####################################################
#string_into
# my_str = "Hello World"
# print(len(my_str))
####################################################
# Slicing or Indexing
#BEGIN:END:STEP
# my_str = "Hello World"
# print(my_str[0])
# my_str = "Hello World"
# print(my_str[0:3])
# my_str = "Hello World"
# print(my_str[0:3])
# my_str = "Hello World"  # Sequence 
# print(my_str[11])
# IndexError: string index out of range
# SybtaxError
# TypeError
# ValueError
# my_str = "Hello World"  # Sequence 
# print(my_str[-1])
# my_str = "Hello World"   
# print(my_str[:3])
# my_str = "Hello World" 
# print(my_str[:3] + my_str[5:])
# my_str = "Hello World" 
# print(my_str[:])
# my_str = "Hello World" 
# print(my_str[::2])
# my_str = "Hello World" 
# print(my_str[::3])
# my_str = "Hello World" 
# print(my_str[-5:-1])
# word =input("Word:  ")
# last_character = word[-1]
# print(f"Last character is {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[len(word)-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print("Last character is :", last_character)
# word = input("Word:  ")
# last_character = word[-1]
# print("Last character is :", last_character, end="")
# word = input("Word:  ")
# last_character = word[-1]
# print("Last character is :", last_character, sep="")
##############
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = input("Word:  ")
# last_character = word[-1]
# print(f"Last character is : {last_character}")
# word = "Apple"
# last_character = word[len(word)-1]
# print(f"Last character is :{last_character}")
# print("Last character is :"< last_character)
########################################################
# Mutable vs Immutable (O'zgaruvchan vs O'zgarmas)
# m = "Azizbek"
# m = 'a' + m[1:]
# print(m)
# m = "Azizbek"
# print("Oldin:", id(m))
# m = 'a' + m[1:]
# print("Keyin:", id(m))
# print(m)
# m = "Azizbek"
# print("Oldin:", id(m))
# m2 = 'a' + m[1:]
# print("Keyin:", id(m))
# print(m, m2)
######################################################
# str_methods
# Case sensitive ve Case Insensitive
# fruits ="Apple Banana Cherry"
# print('Original:', fruits)
# print(fruits.lower())
# print(fruits.upper())
# print(fruits.capitalize())
# print(fruits.title())
# print(fruits.swapcase())
# print(fruits.strip())
# print(fruits.lstrip())
# print(fruits.rstrip())
# print(fruits.endswith('y'))
# print(fruits.startswith('A')) 
# print('-'*60)
# word = '      hello world       '
# print(word)
# print(word.strip())
# fruits = "Apple Banana Cherry"
# print(fruits.split())
# print(fruits.split("a"))
# file_name = "number.py"
# base_name = file_name.split(".")[0]
# extension = file_name.split(".")[1]
# print(f"{file_name=}")
# print(f"{base_name=}")
# print(f"{extension=}")
##################################################
# boolean_intro
# True va False
# a = 5 
# print(dir(a))
# print(a.real)
# print(a.imag)
# print(id(True))
# >, <, ==, <==, >= != Operatorlar
# a = 12
# b = 10
#print(a < b)
# Truthy va Falsy
# print(bool(a))
# print(bool(0))
# print(bool(1))
# print('Stringlar uchun')
# print(bool(""))
# print(bool("asfd"))
# print("Boolean uchun")
# print(bool(True))
# print(bool(False))
# print("Container data typelar uchun")
# print(bool([])) # Empty List
# print(bool(a)) # List
# print(bool(tuple())) # Empty Tuple
# print(bool((1, 2))) # Tuple
# print(bool({})) # Empty Dictionary
# print(bool({"key": "value"})) # Empty DIctionary
# print(bool(set())) #Empty Set
# print(bool({1, 2, 3, 4})) # Set
# print("-"*20)
# print(bool(" "))
# print(bool(""))
###############################################
# word = input()
# print(bool(word.strip()))
word = input()
if not bool(word.strip()):
    print("Please enter something")
else:
    print("You entered:", word)


