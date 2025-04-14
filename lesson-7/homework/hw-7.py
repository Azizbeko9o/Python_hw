# import math
# class Vektor:
#     def __init__(self, *komponentlar):
#         """Vektorni komponentlar bilan yaratish."""
#         self.komponentlar = komponentlar
#     def __repr__(self):
#         """Vektorning matn shaklini qaytaradi."""
#         return f"Vektor{self.komponentlar}"
#     def __add__(self, boshqa):
#         """Ikki vektorni qo'shish."""
#         if len(self.komponentlar) != len(boshqa.komponentlar):
#             raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak")
#         return Vektor(*(x + y for x, y in zip(self.komponentlar, boshqa.komponentlar)))
#     def __sub__(self, boshqa):
#         """Ikki vektorni ayirish."""
#         if len(self.komponentlar) != len(boshqa.komponentlar):
#             raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak")
#         return Vektor(*(x - y for x, y in zip(self.komponentlar, boshqa.komponentlar)))
#     def __mul__(self, skalyar):
#         """Vektorni skalyar bilan ko'paytirish."""
#         return Vektor(*(x * skalyar for x in self.komponentlar))
#     def skalyar_urish(self, boshqa):
#         """Vektorlarning skalyar (dot) mahsulotini hisoblash."""
#         if len(self.komponentlar) != len(boshqa.komponentlar):
#             raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak")
#         return sum(x * y for x, y in zip(self.komponentlar, boshqa.komponentlar))
#     def magnituda(self):
#         """Vektorning magnitudasini (uzunligini) hisoblash."""
#         return math.sqrt(sum(x ** 2 for x in self.komponentlar))
#     def normalizatsiya(self):
#         """Vektorni normalizatsiya qilish (birlik vektorini olish)."""
#         mag = self.magnituda()
#         if mag == 0:
#             raise ValueError("Zero vektorini normalizatsiya qilish mumkin emas")
#         return self * (1 / mag)
# v1 = Vektor(1, 2, 3)
# v2 = Vektor(4, 5, 6)
# print(f"v1: {v1}")
# print(f"v2: {v2}")
# print(f"v1 + v2: {v1 + v2}")
# print(f"v1 - v2: {v1 - v2}")
# print(f"v1 skalyar urish v2: {v1.skalyar_urish(v2)}")
# print(f"v1 magnituda: {v1.magnituda()}")
# print(f"v1 normalizatsiya qilingan: {v1.normalizatsiya()}")
#########################################
# import math
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#     def __mul__(self, scalar):
#         return Vector(self.x * scalar, self.y * scalar)
#     def dot(self, other):
#         return self.x * other.x + self.y * other.y
#     def magnitude(self):
#         return math.sqrt(self.x**2 + self.y**2)
#     def normalize(self):
#         mag = self.magnitude()
#         if mag == 0:
#             return Vector(0, 0)  
#         return Vector(self.x / mag, self.y / mag)
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)

# print("Qo'shish:", v1 + v2)
# print("Ayirish:", v1 - v2)
# print("Skalyar ko'paytirish:", v1 * 2)
# print("Dot product:", v1.dot(v2))
# print("Uzunlik:", v1.magnitude())
# print("Normallashtirilgan:", v1.normalize())
#########################################
# import math
# class Vector:
#     def __init__(self, components):
#         self.components = list(components)
#     def __check_dimensions(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vektorlar bir xil o'lchamda bo'lishi kerak.")
#     def __add__(self, other):
#         self.__check_dimensions(other)
#         result = [a + b for a, b in zip(self.components, other.components)]
#         return Vector(result)
#     def __sub__(self, other):
#         self.__check_dimensions(other)
#         result = [a - b for a, b in zip(self.components, other.components)]
#         return Vector(result)
#     def __mul__(self, scalar):
#         if isinstance(scalar, (int, float)):
#             result = [a * scalar for a in self.components]
#             return Vector(result)
#         else:
#             raise TypeError("Faqat skalyar (son) bilan ko'paytirish mumkin.")
#     def dot(self, other):
#         self.__check_dimensions(other)
#         return sum(a * b for a, b in zip(self.components, other.components))
#     def magnitude(self):
#         return math.sqrt(sum(a**2 for a in self.components))
#     def normalize(self):
#         mag = self.magnitude()
#         if mag == 0:
#             raise ValueError("Nol vektorni normallashtirib bo'lmaydi.")
#         return self * (1 / mag)
#     def __str__(self):
#         return f"Vector({self.components})"
#     def __repr__(self):
#         return self.__str__()
# v1 = Vector([3, 4, 5])
# v2 = Vector([1, 2, 3])
# print("v1:", v1)
# print("v2:", v2)
# print("Qo'shish:", v1 + v2)
# print("Ayirish:", v1 - v2)
# print("Skalyar * 2:", v1 * 2)
# print("Dot product:", v1.dot(v2))
# print("Uzunligi:", v1.magnitude())
# print("Unit vektor:", v1.normalize())
# v3 = Vector([1, 2])
#########################################
# file = open("employees.txt", "a")
# employee_id = input("Xodim ID sini kiriting: ")
# name = input("Ismni kiriting: ")
# position = input("Lavozimni kiriting: ")
# salary = input("Maoshni kiriting: ")
# file.write(employee_id + "," + name + "," + position + "," + salary + "\n")
# file.close()
# print("Xodim muvaffaqiyatli qo'shildi.\n")
# print("Barcha xodimlar ro'yxati:")
# try:
#     file = open("employees.txt", "r")
#     lines = file.readlines()
#     for line in lines:
#         parts = line.strip().split(",")
#         print("ID:", parts[0], "| Ism:", parts[1], "| Lavozim:", parts[2], "| Maosh:", parts[3])
#     file.close()
# except:
#     print("Xodimlar fayli topilmadi.")
# search_id = input("\nQaysi ID bo'yicha qidirilsin? ")
# found = False
# file = open("employees.txt", "r")
# lines = file.readlines()
# for line in lines:
#     parts = line.strip().split(",")
#     if parts[0] == search_id:
#         print("Topildi:", parts[1], parts[2], parts[3])
#         found = True
# file.close()
# if not found:
#     print("Xodim topilmadi.")
# update_id = input("\nQaysi ID yangilansin? ")
# file = open("employees.txt", "r")
# lines = file.readlines()
# file.close()
# new_lines = []
# for line in lines:
#     parts = line.strip().split(",")
#     if parts[0] == update_id:
#         new_name = input("Yangi ism: ")
#         new_position = input("Yangi lavozim: ")
#         new_salary = input("Yangi maosh: ")
#         new_line = update_id + "," + new_name + "," + new_position + "," + new_salary + "\n"
#         new_lines.append(new_line)
#     else:
#         new_lines.append(line)

# file = open("employees.txt", "w")
# for line in new_lines:
#     file.write(line)
# file.close()
# print("Xodim ma'lumoti yangilandi.")
# delete_id = input("\nQaysi ID ochirilsin? ")
# file = open("employees.txt", "r")
# lines = file.readlines()
# file.close()
# file = open("employees.txt", "w")
# for line in lines:
#     parts = line.strip().split(",")
#     if parts[0] != delete_id:
#         file.write(line)
# file.close()
# print("Xodim o'chirildi.")
#########################################
# print("1. Xodim qo'shish")
# print("2. Barcha xodimlarni ko'rish")
# print("3. Xodimni yangilash")
# print("4. Xodimni o'chirish")
# tanlov = input("Tanlang (1-4): ")
# if tanlov == "1":
#     f = open("employees.txt", "a")
#     employee_id = input("ID kiriting: ")
#     name = input("Ism kiriting: ")
#     position = input("Lavozim kiriting: ")
#     salary = input("Maosh kiriting: ")
#     f.write(employee_id + "," + name + "," + position + "," + salary + "\n")
#     f.close()
#     print("Xodim qo'shildi.")
# elif tanlov == "2":
#     try:
#         f = open("employees.txt", "r")
#         lines = f.readlines()
#         if len(lines) == 0:
#             print("Hech qanday xodim yo‘'q.")
#         else:
#             for line in lines:
#                 qism = line.strip().split(",")
#                 print("ID:", qism[0], "| Ism:", qism[1], "| Lavozim:", qism[2], "| Maosh:", qism[3])
#         f.close()
#     except:
#         print("Fayl topilmadi.")
# elif tanlov == "3":
#     update_id = input("Qaysi ID yangilansin? ")
#     try:
#         f = open("employees.txt", "r")
#         lines = f.readlines()
#         f.close()
#         yangi_ism = input("Yangi ism: ")
#         yangi_lavozim = input("Yangi lavozim: ")
#         yangi_maosh = input("Yangi maosh: ")
#         f = open("employees.txt", "w")
#         for line in lines:
#             qism = line.strip().split(",")
#             if qism[0] == update_id:
#                 yangi_qator = update_id + "," + yangi_ism + "," + yangi_lavozim + "," + yangi_maosh + "\n"
#                 f.write(yangi_qator)
#             else:
#                 f.write(line)
#         f.close()
#         print("Xodim yangilandi.")
#     except:
#         print("Xatolik yuz berdi.")
# elif tanlov == "4":
#     delete_id = input("Qaysi ID o'chirilsin? ")
#     try:
#         f = open("employees.txt", "r")
#         lines = f.readlines()
#         f.close()
#         f = open("employees.txt", "w")
#         for line in lines:
#             qism = line.strip().split(",")
#             if qism[0] != delete_id:
#                 f.write(line)
#         f.close()
#         print("Xodim o'chirildi.")
#     except:
#         print("Fayl topilmadi.")
# else:
#     print("Noto'g'ri tanlov.")
#########################################
# tanlov = ""
# while tanlov != "6":
#     print("\n--- Xodimlar Boshqaruvi ---")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni qidirish (ID bo'yicha)")
#     print("4. Xodimni yangilash")
#     print("5. Xodimni o'chirish")
#     print("6. Chiqish")
#     tanlov = input("Tanlang (1-6): ")
#     if tanlov == "1":
#         f = open("employees.txt", "a")
#         employee_id = input("ID: ")
#         name = input("Ism: ")
#         position = input("Lavozim: ")
#         salary = input("Maosh: ")
#         f.write(employee_id + "," + name + "," + position + "," + salary + "\n")
#         f.close()
#         print("Xodim qo'shildi.")
#     elif tanlov == "2":
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             if len(lines) == 0:
#                 print("Hech qanday xodim yo'q.")
#             else:
#                 print("\nBarcha xodimlar:")
#                 for line in lines:
#                     qism = line.strip().split(",")
#                     print("ID:", qism[0], "| Ism:", qism[1], "| Lavozim:", qism[2], "| Maosh:", qism[3])
#         except:
#             print("Fayl mavjud emas.")
#     elif tanlov == "3":
#         q_id = input("Qidirilayotgan ID: ")
#         topildi = False
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             for line in lines:
#                 qism = line.strip().split(",")
#                 if qism[0] == q_id:
#                     print("Topildi:", qism[1], qism[2], qism[3])
#                     topildi = True
#             if not topildi:
#                 print("Xodim topilmadi.")
#         except:
#             print("Fayl mavjud emas.")
#     elif tanlov == "4":
#         yangilash_id = input("Qaysi ID yangilansin? ")
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             yangi_ism = input("Yangi ism: ")
#             yangi_lavozim = input("Yangi lavozim: ")
#             yangi_maosh = input("Yangi maosh: ")
#             f = open("employees.txt", "w")
#             for line in lines:
#                 qism = line.strip().split(",")
#                 if qism[0] == yangilash_id:
#                     yangi_qator = yangilash_id + "," + yangi_ism + "," + yangi_lavozim + "," + yangi_maosh + "\n"
#                     f.write(yangi_qator)
#                 else:
#                     f.write(line)
#             f.close()
#             print("Xodim yangilandi.")
#         except:
#             print("Xatolik yuz berdi.")
#     elif tanlov == "5":
#         ochirish_id = input("Qaysi ID o'chirilsin? ")
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             f = open("employees.txt", "w")
#             for line in lines:
#                 qism = line.strip().split(",")
#                 if qism[0] != ochirish_id:
#                     f.write(line)
#             f.close()
#             print("Xodim o'chirildi.")
#         except:
#             print("Xatolik yuz berdi.")
#     elif tanlov == "6":
#         print("Dasturdan chiqildi. Xayr!")
#     else:
#         print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")
#########################################
# tanlov = ""
# while tanlov != "6":
#     print("\n--- XODIMLAR BILAN ISHLASH DASTURI ---")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni qidirish (ID orqali)")
#     print("4. Xodimni yangilash (ID orqali)")
#     print("5. Xodimni o'chirish (ID orqali)")
#     print("6. Chiqish")
#     tanlov = input("Tanlovni kiriting (1-6): ")
#     if tanlov == "1":
#         f = open("employees.txt", "a")
#         employee_id = input("ID: ")
#         name = input("Ism: ")
#         position = input("Lavozim: ")
#         salary = input("Maosh: ")
#         f.write(employee_id + "," + name + "," + position + "," + salary + "\n")
#         f.close()
#         print("Xodim qo'shildi.")
#     elif tanlov == "2":
#         try:
#             f = open("employees.txt", "r")
#             rows = f.readlines()
#             f.close()
#             if len(rows) == 0:
#                 print("Faylda hech qanday xodim mavjud emas.")
#             else:
#                 print("\nBarcha xodimlar:")
#                 for row in rows:
#                     parts = row.strip().split(",")
#                     print("ID:", parts[0], "| Ism:", parts[1], "| Lavozim:", parts[2], "| Maosh:", parts[3])
#         except:
#             print("Fayl topilmadi.")
#     elif tanlov == "3":
#         search_id = input("Qidirilayotgan xodim ID sini kiriting: ")
#         topildi = False
#         try:
#             f = open("employees.txt", "r")
#             rows = f.readlines()
#             f.close()
#             for row in rows:
#                 parts = row.strip().split(",")
#                 if parts[0] == search_id:
#                     print("Topildi: ID:", parts[0], "| Ism:", parts[1], "| Lavozim:", parts[2], "| Maosh:", parts[3])
#                     topildi = True
#                     break
#             if not topildi:
#                 print("Bunday IDga ega xodim topilmadi.")
#         except:
#             print("Fayl mavjud emas.")
#     elif tanlov == "4":
#         update_id = input("Qaysi xodim ID yangilansin? ")
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             yangilandi = False
#             f = open("employees.txt", "w")
#             for line in lines:
#                 parts = line.strip().split(",")
#                 if parts[0] == update_id:
#                     yangi_ism = input("Yangi ism: ")
#                     yangi_lavozim = input("Yangi lavozim: ")
#                     yangi_maosh = input("Yangi maosh: ")
#                     yangi_qator = update_id + "," + yangi_ism + "," + yangi_lavozim + "," + yangi_maosh + "\n"
#                     f.write(yangi_qator)
#                     yangilandi = True
#                 else:
#                     f.write(line)
#             f.close()
#             if yangilandi:
#                 print("Xodim ma'lumoti yangilandi.")
#             else:
#                 print("Xodim topilmadi.")
#         except:
#             print("Fayl bilan ishlashda xatolik.")
#     elif tanlov == "5":
#         delete_id = input("Qaysi xodim ID o'chirilsin? ")
#         try:
#             f = open("employees.txt", "r")
#             lines = f.readlines()
#             f.close()
#             f = open("employees.txt", "w")
#             topildi = False
#             for line in lines:
#                 parts = line.strip().split(",")
#                 if parts[0] != delete_id:
#                     f.write(line)
#                 else:
#                     topildi = True
#             f.close()
#             if topildi:
#                 print("Xodim o'chirildi.")
#             else:
#                 print("Xodim topilmadi.")
#         except:
#             print("Fayl bilan ishlashda xatolik.")
#     elif tanlov == "6":
#         print("Dasturdan chiqildi. Xayr!")
#     else:
#         print("Noto'g'ri tanlov! Faqat 1 dan 6 gacha tanlang.")
#########################################
# class Employee:
#     def __init__(self, employee_id, name, position, salary):
#         self.employee_id = employee_id
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def __str__(self):
#         return f"ID: {self.employee_id} | Ism: {self.name} | Lavozim: {self.position} | Maosh: {self.salary}"

#     def to_line(self):
#         return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

#     @staticmethod
#     def from_line(line):
#         parts = line.strip().split(",")
#         return Employee(parts[0], parts[1], parts[2], parts[3])
# while True:
#     print("\n--- XODIMLAR DASTURI ---")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni qidirish")
#     print("4. Xodimni yangilash")
#     print("5. Xodimni o'chirish")
#     print("6. Chiqish")
#     choice = input("Tanlang (1-6): ")
#     if choice == "1":
#         eid = input("ID: ")
#         ism = input("Ism: ")
#         lavozim = input("Lavozim: ")
#         maosh = input("Maosh: ")
#         xodim = Employee(eid, ism, lavozim, maosh)
#         with open("employees.txt", "a") as f:
#             f.write(xodim.to_line())
#         print("Xodim qo'shildi.")
#     elif choice == "2":
#         try:
#             with open("employees.txt", "r") as f:
#                 lines = f.readlines()
#                 if not lines:
#                     print("Hech qanday xodim mavjud emas.")
#                 else:
#                     print("\nBarcha xodimlar:")
#                     for line in lines:
#                         xodim = Employee.from_line(line)
#                         print(xodim)
#         except FileNotFoundError:
#             print("Fayl mavjud emas.")
#     elif choice == "3":
#         qidir_id = input("Qidirilayotgan ID: ")
#         topildi = False
#         try:
#             with open("employees.txt", "r") as f:
#                 for line in f:
#                     xodim = Employee.from_line(line)
#                     if xodim.employee_id == qidir_id:
#                         print("Topildi:", xodim)
#                         topildi = True
#                         break
#             if not topildi:
#                 print("Xodim topilmadi.")
#         except:
#             print("Fayl xatoligi.")
#     elif choice == "4":
#         yangilash_id = input("Qaysi ID yangilansin? ")
#         try:
#             with open("employees.txt", "r") as f:
#                 lines = f.readlines()
#             with open("employees.txt", "w") as f:
#                 topildi = False
#                 for line in lines:
#                     xodim = Employee.from_line(line)
#                     if xodim.employee_id == yangilash_id:
#                         yangi_ism = input("Yangi ism: ")
#                         yangi_lavozim = input("Yangi lavozim: ")
#                         yangi_maosh = input("Yangi maosh: ")
#                         yangilangan = Employee(xodim.employee_id, yangi_ism, yangi_lavozim, yangi_maosh)
#                         f.write(yangilangan.to_line())
#                         topildi = True
#                     else:
#                         f.write(xodim.to_line())
#             if topildi:
#                 print("Yangilandi.")
#             else:
#                 print("ID topilmadi.")
#         except:
#             print("Xatolik yuz berdi.")

#     elif choice == "5":
#         del_id = input("Qaysi ID o'chirish kerak? ")
#         try:
#             with open("employees.txt", "r") as f:
#                 lines = f.readlines()
#             with open("employees.txt", "w") as f:
#                 topildi = False
#                 for line in lines:
#                     xodim = Employee.from_line(line)
#                     if xodim.employee_id != del_id:
#                         f.write(xodim.to_line())
#                     else:
#                         topildi = True
#             if topildi:
#                 print("O'chirildi.")
#             else:
#                 print("Xodim topilmadi.")
#         except:
#             print("Xatolik yuz berdi.")

#     elif choice == "6":
#         print("Dasturdan chiqildi.")
#         break
#     else:
#         print("Noto'g'ri tanlov. Qaytadan kiriting.")
#########################################
# class Employee:
#     def __init__(self, employee_id, name, position, salary):
#         self.employee_id = employee_id
#         self.name = name
#         self.position = position
#         self.salary = salary
#     def __str__(self):
#         return f"ID: {self.employee_id} | Ism: {self.name} | Lavozim: {self.position} | Maosh: {self.salary}"
#     def to_line(self):
#         return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"
#     def from_line(line):
#         parts = line.strip().split(",")
#         return Employee(parts[0], parts[1], parts[2], parts[3])
# filename = "employees.txt"
# tanlov = ""
# while tanlov != "6":
#     print("\n--- XODIMLAR BILAN ISHLASH DASTURI ---")
#     print("1. Yangi xodim qo'shish")
#     print("2. Barcha xodimlarni ko'rish")
#     print("3. Xodimni qidirish (ID)")
#     print("4. Xodimni yangilash")
#     print("5. Xodimni o'chirish")
#     print("6. Chiqish")
#     tanlov = input("Tanlang (1-6): ")
#     if tanlov == "1":
#         employee_id = input("ID: ")
#         ism = input("Ism: ")
#         lavozim = input("Lavozim: ")
#         maosh = input("Maosh: ")
#         with open(filename, "r") as f:
#             existing_ids = [line.split(",")[0] for line in f]
#         if employee_id in existing_ids:
#             print("Bunday ID bilan xodim mavjud!")
#         else:
#             xodim = Employee(employee_id, ism, lavozim, maosh)
#             with open(filename, "a") as f:
#                 f.write(xodim.to_line())
#             print("Xodim qo'shildi.")
#     elif tanlov == "2":
#         try:
#             with open(filename, "r") as f:
#                 rows = f.readlines()
#             if not rows:
#                 print("Faylda hech qanday xodim mavjud emas.")
#             else:
#                 print("\nBarcha xodimlar:")
#                 for row in rows:
#                     parts = row.strip().split(",")
#                     print("ID:", parts[0], "| Ism:", parts[1], "| Lavozim:", parts[2], "| Maosh:", parts[3])
#         except:
#             print("Fayl mavjud emas.")
#     elif tanlov == "3":
#         search_id = input("Qidirilayotgan xodim ID sini kiriting: ")
#         topildi = False
#         try:
#             with open(filename, "r") as f:
#                 rows = f.readlines()
#             for row in rows:
#                 parts = row.strip().split(",")
#                 if parts[0] == search_id:
#                     print("Topildi: ID:", parts[0], "| Ism:", parts[1], "| Lavozim:", parts[2], "| Maosh:", parts[3])
#                     topildi = True
#                     break
#             if not topildi:
#                 print("Bunday IDga ega xodim topilmadi.")
#         except:
#             print("Fayl mavjud emas.")
#     elif tanlov == "4":
#         update_id = input("Qaysi xodim ID yangilansin? ")
#         try:
#             with open(filename, "r") as f:
#                 lines = f.readlines()
#             with open(filename, "w") as f:
#                 topildi = False
#                 for line in lines:
#                     parts = line.strip().split(",")
#                     if parts[0] == update_id:
#                         yangi_ism = input("Yangi ism: ")
#                         yangi_lavozim = input("Yangi lavozim: ")
#                         yangi_maosh = input("Yangi maosh: ")
#                         yangi_qator = update_id + "," + yangi_ism + "," + yangi_lavozim + "," + yangi_maosh + "\n"
#                         f.write(yangi_qator)
#                         topildi = True
#                     else:
#                         f.write(line)
#                 if topildi:
#                     print("Yangilandi.")
#                 else:
#                     print("Xodim topilmadi.")
#         except:
#             print("Xatolik yuz berdi.")
#     elif tanlov == "5":
#         delete_id = input("Qaysi xodim ID o'chirilsin? ")
#         try:
#             with open(filename, "r") as f:
#                 lines = f.readlines()
#             with open(filename, "w") as f:
#                 topildi = False
#                 for line in lines:
#                     parts = line.strip().split(",")
#                     if parts[0] != delete_id:
#                         f.write(line)
#                     else:
#                         topildi = True
#                 if topildi:
#                     print("Xodim o'chirildi.")
#                 else:
#                     print("Xodim topilmadi.")
#         except:
#             print("Xatolik yuz berdi.")
#     elif tanlov == "6":
#         print("Dasturdan chiqildi. Xayr!")
#         break
#     else:
#         print("Noto'g'ri tanlov! Faqat 1 dan 6 gacha tanlang.")
#########################################
# import json
# import os
# class Task:
#     def __init__(self, task_id, title, description, due_date=None, status="Pending"):
#         self.task_id = task_id
#         self.title = title
#         self.description = description
#         self.due_date = due_date
#         self.status = status
#     def __str__(self):
#         return f"ID: {self.task_id} | Title: {self.title} | Description: {self.description} | Due: {self.due_date if self.due_date else 'N/A'} | Status: {self.status}"
#     def to_dict(self):
#         return {
#             "task_id": self.task_id,
#             "title": self.title,
#             "description": self.description,
#             "due_date": self.due_date,
#             "status": self.status
#         }
#     def from_dict(data):
#         return Task(data["task_id"], data["title"], data["description"], data["due_date"], data["status"])
# filename = "tasks.json"
# def load_tasks():
#     if os.path.exists(filename):
#         with open(filename, "r") as f:
#             tasks_data = json.load(f)
#         return [Task.from_dict(task) for task in tasks_data]
#     return []
# def save_tasks(tasks):
#     with open(filename, "w") as f:
#         tasks_data = [task.to_dict() for task in tasks]
#         json.dump(tasks_data, f)
# def add_task(tasks, task):
#     tasks.append(task)
#     save_tasks(tasks)
#     print("Task qo'shildi.")
# def view_tasks(tasks):
#     if not tasks:
#         print("Hech qanday task mavjud emas.")
#     else:
#         for task in tasks:
#             print(task)
# def find_task_by_id(tasks, task_id):
#     for task in tasks:
#         if task.task_id == task_id:
#             return task
#     return None
# def update_task(tasks, task_id, new_task):
#     for i, task in enumerate(tasks):
#         if task.task_id == task_id:
#             tasks[i] = new_task
#             save_tasks(tasks)
#             print("Task yangilandi.")
#             return
#     print("Task topilmadi.")
# def delete_task(tasks, task_id):
#     task = find_task_by_id(tasks, task_id)
#     if task:
#         tasks.remove(task)
#         save_tasks(tasks)
#         print("Task o'chirildi.")
#     else:
#         print("Task topilmadi.")
# def filter_tasks_by_status(tasks, status):
#     filtered_tasks = [task for task in tasks if task.status.lower() == status.lower()]
#     if filtered_tasks:
#         for task in filtered_tasks:
#             print(task)
#     else:
#         print(f"{status} holatida tasklar topilmadi.")
# tasks = load_tasks()
# while True:
#     print("\n--- To-Do Dasturi ---")
#     print("1. Yangi task qo'shish")
#     print("2. Barcha tasklarni ko'rish")
#     print("3. Taskni yangilash")
#     print("4. Taskni o'chirish")
#     print("5. Tasklarni status bo‘yicha filtrlash")
#     print("6. Chiqish")
#     tanlov = input("Tanlang (1-6): ")
#     if tanlov == "1":
#         task_id = input("Task ID: ")
#         title = input("Title: ")
#         description = input("Description: ")
#         due_date = input("Due Date (optional): ")
#         status = input("Status (Pending, In Progress, Completed): ")
#         new_task = Task(task_id, title, description, due_date if due_date else None, status)
#         add_task(tasks, new_task)
#     elif tanlov == "2":
#         print("\nBarcha Tasklar:")
#         view_tasks(tasks)
#     elif tanlov == "3":
#         task_id = input("Yangilash uchun task ID: ")
#         task = find_task_by_id(tasks, task_id)
#         if task:
#             title = input(f"Yangi Title ({task.title}): ") or task.title
#             description = input(f"Yangi Description ({task.description}): ") or task.description
#             due_date = input(f"Yangi Due Date ({task.due_date}): ") or task.due_date
#             status = input(f"Yangi Status ({task.status}): ") or task.status
#             updated_task = Task(task_id, title, description, due_date, status)
#             update_task(tasks, task_id, updated_task)
#########################################
class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    def __str__(self):
        return f"ID: {self.task_id} | Title: {self.title} | Description: {self.description} | Due: {self.due_date if self.due_date else 'N/A'} | Status: {self.status}"
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data["due_date"], data["status"])
import json
import csv
import os
class FileHandler:
    def __init__(self, filename, format="json"):
        self.filename = filename
        self.format = format.lower()
    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        if self.format == "json":
            return self.load_json()
        elif self.format == "csv":
            return self.load_csv()
    def save_tasks(self, tasks):
        if self.format == "json":
            self.save_json(tasks)
        elif self.format == "csv":
            self.save_csv(tasks)
    def load_json(self):
        with open(self.filename, "r") as f:
            tasks_data = json.load(f)
        return [Task.from_dict(task) for task in tasks_data]
    def save_json(self, tasks):
        with open(self.filename, "w") as f:
            tasks_data = [task.to_dict() for task in tasks]
            json.dump(tasks_data, f)
    def load_csv(self):
        tasks = []
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  
                    task = Task(row[0], row[1], row[2], row[3], row[4])
                    tasks.append(task)
        return tasks
    def save_csv(self, tasks):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
class TaskManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = self.file_handler.load_tasks()
    def add_task(self, task):
        self.tasks.append(task)
        self.file_handler.save_tasks(self.tasks)
        print("Task qo‘shildi.")

    def view_tasks(self):
        if not self.tasks:
            print("Hech qanday task mavjud emas.")
        else:
            for task in self.tasks:
                print(task)

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task(self, task_id, new_task):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks[i] = new_task
                self.file_handler.save_tasks(self.tasks)
                print("Task yangilandi.")
                return
        print("Task topilmadi.")

    def delete_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.file_handler.save_tasks(self.tasks)
            print("Task o‘chirildi.")
        else:
            print("Task topilmadi.")

    def filter_tasks_by_status(self, status):
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
        else:
            print(f"{status} holatida tasklar topilmadi.")
def main():
    filename = input("Fayl nomini kiriting (tasks.json yoki tasks.csv): ")
    format = filename.split(".")[-1]
    file_handler = FileHandler(filename, format)
    task_manager = TaskManager(file_handler)

    while True:
        print("\n--- To-Do Dasturi ---")
        print("1. Yangi task qo‘shish")
        print("2. Barcha tasklarni ko‘rish")
        print("3. Taskni yangilash")
        print("4. Taskni o‘chirish")
        print("5. Tasklarni status bo‘yicha filtrlash")
        print("6. Chiqish")
        tanlov = input("Tanlang (1-6): ")
if __name__ == "__main__":
    main()
