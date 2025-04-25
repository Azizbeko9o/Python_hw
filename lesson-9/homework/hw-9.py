#####1-misol
#  class Kutubxona:
#     def __init__(self):
#         self.kitoblar = []
#         self.ijaraga_olingan_kitoblar = {}
#     def kitob_qoshish(self, kitob_nomi):
#         self.kitoblar.append(kitob_nomi)
#         print(f"'{kitob_nomi}' kutubxonaga qo'shildi.")
#     def kitoblarni_korish(self):
#         if not self.kitoblar:
#             print("Kutubxonada hech qanday kitob mavjud emas.")
#         else:
#             print("Mavjud kitoblar:")
#             for index, kitob in enumerate(self.kitoblar, 1):
#                 print(f"{index}. {kitob}")
#     def kitob_ijaraga_olish(self, kitob_nomi, foydalanuvchi_nomi):
#         if kitob_nomi in self.kitoblar:
#             self.kitoblar.remove(kitob_nomi)
#             self.ijaraga_olingan_kitoblar[kitob_nomi] = foydalanuvchi_nomi
#             print(f"{foydalanuvchi_nomi} '{kitob_nomi}' kitobini ijaraga oldi.")
#         else:
#             print(f"Uzr, '{kitob_nomi}' kitobi kutubxonada mavjud emas.")
#     def kitob_qaytarish(self, kitob_nomi):
#         if kitob_nomi in self.ijaraga_olingan_kitoblar:
#             self.kitoblar.append(kitob_nomi)
#             foydalanuvchi_nomi = self.ijaraga_olingan_kitoblar.pop(kitob_nomi)
#             print(f"{foydalanuvchi_nomi} '{kitob_nomi}' kitobini qaytardi.")
#         else:
#             print(f"'{kitob_nomi}' kitobi bu kutubxonada ijaraga olinmagan.")
# def asosiy():
#     kutubxona = Kutubxona()
#     while True:
#         print("\nKutubxona Menyusi:")
#         print("1. Kitob qo'shish")
#         print("2. Mavjud kitoblarni ko'rish")
#         print("3. Kitobni ijaraga olish")
#         print("4. Kitobni qaytarish")
#         print("5. Chiqish")
#         tanlov = input("Iltimos, tanlovni kiriting (1-5): ")
#         if tanlov == '1':
#             kitob_nomi = input("Qo'shmoqchi bo'lgan kitob nomini kiriting: ")
#             kutubxona.kitob_qoshish(kitob_nomi)
#         elif tanlov == '2':
#             kutubxona.kitoblarni_korish()
#         elif tanlov == '3':
#             kitob_nomi = input("Ijara olish uchun kitob nomini kiriting: ")
#             foydalanuvchi_nomi = input("Foydalanuvchi nomini kiriting: ")
#             kutubxona.kitob_ijaraga_olish(kitob_nomi, foydalanuvchi_nomi)
#         elif tanlov == '4':
#             kitob_nomi = input("Qaytariladigan kitob nomini kiriting: ")
#             kutubxona.kitob_qaytarish(kitob_nomi)
#         elif tanlov == '5':
#             print("Kutubxonadan chiqish...")
#             break
#         else:
#             print("Noto'g'ri tanlov! Iltimos, 1-5 oralig'ida biror tanlov kiriting.")
# asosiy()
################################# 2-misol ########################################
# class BookNotFoundException(Exception):
#     def __init__(self, message="Kitob kutubxonada mavjud emas."):
#         self.message = message
#         super().__init__(self.message)
# class BookAlreadyBorrowedException(Exception):
#     def __init__(self, message="Kitob allaqachon ijaraga olingan."):
#         self.message = message
#         super().__init__(self.message)
# class MemberLimitExceededException(Exception):
#     def __init__(self, message="Foydalanuvchi ruxsat etilgan kitoblar limitini oshirib yubordi."):
#         self.message = message
#         super().__init__(self.message)
# class Kutubxona:
#     def __init__(self, max_ijara_limit=3):
#         self.kitoblar = []
#         self.ijaraga_olingan_kitoblar = {}
#         self.max_ijara_limit = max_ijara_limit  # Har bir foydalanuvchiga ruxsat etilgan kitoblar soni

#     def kitob_qoshish(self, kitob_nomi):
#         self.kitoblar.append(kitob_nomi)
#         print(f"'{kitob_nomi}' kutubxonaga qo'shildi.")
#     def kitoblarni_korish(self):
#         if not self.kitoblar:
#             print("Kutubxonada hech qanday kitob mavjud emas.")
#         else:
#             print("Mavjud kitoblar:")
#             for index, kitob in enumerate(self.kitoblar, 1):
#                 print(f"{index}. {kitob}")
#     def kitob_ijaraga_olish(self, kitob_nomi, foydalanuvchi_nomi):
#         if kitob_nomi not in self.kitoblar:
#             raise BookNotFoundException(f"'{kitob_nomi}' kitobi kutubxonada mavjud emas.")
#         if kitob_nomi in self.ijaraga_olingan_kitoblar:
#             raise BookAlreadyBorrowedException(f"'{kitob_nomi}' kitobi allaqachon ijaraga olingan.")
#         borrowed_books = [kitob for kitob, user in self.ijaraga_olingan_kitoblar.items() if user == foydalanuvchi_nomi]
#         if len(borrowed_books) >= self.max_ijara_limit:
#             raise MemberLimitExceededException(f"{foydalanuvchi_nomi} ruxsat etilgan {self.max_ijara_limit} kitobni oshirib ijaraga olishga urindi.")
#         self.kitoblar.remove(kitob_nomi)
#         self.ijaraga_olingan_kitoblar[kitob_nomi] = foydalanuvchi_nomi
#         print(f"{foydalanuvchi_nomi} '{kitob_nomi}' kitobini ijaraga oldi.")
#     def kitob_qaytarish(self, kitob_nomi):
#         if kitob_nomi not in self.ijaraga_olingan_kitoblar:
#             print(f"'{kitob_nomi}' kitobi bu kutubxonada ijaraga olinmagan.")
#             return
#         foydalanuvchi_nomi = self.ijaraga_olingan_kitoblar.pop(kitob_nomi)
#         self.kitoblar.append(kitob_nomi)
#         print(f"{foydalanuvchi_nomi} '{kitob_nomi}' kitobini qaytardi.")
# def asosiy():
#     kutubxona = Kutubxona()
#     while True:
#         print("\nKutubxona Menyusi:")
#         print("1. Kitob qo'shish")
#         print("2. Mavjud kitoblarni ko'rish")
#         print("3. Kitobni ijaraga olish")
#         print("4. Kitobni qaytarish")
#         print("5. Chiqish")
#         tanlov = input("Iltimos, tanlovni kiriting (1-5): ")
#         if tanlov == '1':
#             kitob_nomi = input("Qo'shmoqchi bo'lgan kitob nomini kiriting: ")
#             kutubxona.kitob_qoshish(kitob_nomi)
#         elif tanlov == '2':
#             kutubxona.kitoblarni_korish()
#         elif tanlov == '3':
#             kitob_nomi = input("Ijara olish uchun kitob nomini kiriting: ")
#             foydalanuvchi_nomi = input("Foydalanuvchi nomini kiriting: ")
#             try:
#                 kutubxona.kitob_ijaraga_olish(kitob_nomi, foydalanuvchi_nomi)
#             except BookNotFoundException as e:
#                 print(e)
#             except BookAlreadyBorrowedException as e:
#                 print(e)
#             except MemberLimitExceededException as e:
#                 print(e)
#         elif tanlov == '4':
#             kitob_nomi = input("Qaytariladigan kitob nomini kiriting: ")
#             kutubxona.kitob_qaytarish(kitob_nomi)
#         elif tanlov == '5':
#             print("Kutubxonadan chiqish...")
#             break
#         else:
#             print("Noto'g'ri tanlov! Iltimos, 1-5 oralig'ida biror tanlov kiriting.")
# asosiy()
################################# 3-misol ########################################
# class Book:
#     def __init__(self, title, author):
#         self.title = title  
#         self.author = author   
#         self.is_borrowed = False  
#     def __str__(self):
#         return f"'{self.title}' - {self.author}"
# class Member:
#     def __init__(self, name):
#         self.name = name  
#         self.borrowed_books = []  
#     def borrow_book(self, book):
#         if len(self.borrowed_books) >= 3:
#             print(f"{self.name} limitni oshirib bo'ldi, maksimal 3 kitobni ijaraga olish mumkin.")
#             return False
#         if book.is_borrowed:
#             print(f"'{book.title}' kitobi allaqachon ijaraga olingan.")
#             return False
#         self.borrowed_books.append(book)
#         book.is_borrowed = True
#         print(f"{self.name} '{book.title}' kitobini ijaraga oldi.")
#         return True
#     def return_book(self, book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.is_borrowed = False
#             print(f"{self.name} '{book.title}' kitobini qaytardi.")
#         else:
#             print(f"{self.name} '{book.title}' kitobini ijaraga olmadi.")
# class Library:
#     def __init__(self):
#         self.books = []  
#         self.members = []  
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"'{book.title}' kutubxonaga qo'shildi.")
#     def add_member(self, member):
#         self.members.append(member)
#         print(f"{member.name} kutubxona a'zosi sifatida qo'shildi.")
#     def list_books(self):
#         if not self.books:
#             print("Kutubxonada hech qanday kitob mavjud emas.")
#         else:
#             print("Kutubxonadagi kitoblar:")
#             for book in self.books:
#                 status = "ijaraga olingan" if book.is_borrowed else "mavjud"
#                 print(f"'{book.title}' - {book.author} ({status})")
# def asosiy():
#     kutubxona = Library()
#     kutubxona.add_book(Book("Alisher Navoiy", "Xamsa"))
#     kutubxona.add_book(Book("A.S. Pushkin", "Eugene Onegin"))
#     kutubxona.add_book(Book("J.K. Rowling", "Harry Potter"))
#     kutubxona.add_book(Book("J.R.R. Tolkien", "The Hobbit"))
#     member1 = Member("Ali")
#     member2 = Member("Sahro")
#     kutubxona.add_member(member1)
#     kutubxona.add_member(member2)
#     kutubxona.list_books()
#     member1.borrow_book(kutubxona.books[0])  
#     member1.borrow_book(kutubxona.books[1])  
#     member2.borrow_book(kutubxona.books[2])
#     member1.borrow_book(kutubxona.books[3]) 
#     kutubxona.list_books()
#     member1.return_book(kutubxona.books[0]) 
#     member2.return_book(kutubxona.books[2])  
#     kutubxona.list_books()
# asosiy()
################################# 4-misol ########################################
# class Book:
#     def __init__(self, title, author):
#         self.title = title  
#         self.author = author  
#         self.is_borrowed = False  
#     def __str__(self):
#         return f"'{self.title}' - {self.author}"
# class Member:
#     def __init__(self, name):
#         self.name = name  
#         self.borrowed_books = []  
#     def borrow_book(self, book):
#         if len(self.borrowed_books) >= 3:
#             raise MemberLimitExceededException(f"{self.name} limitni oshirib bo'ldi, maksimal 3 kitobni ijaraga olish mumkin.")
#         if book.is_borrowed:
#             raise BookAlreadyBorrowedException(f"'{book.title}' kitobi allaqachon ijaraga olingan.")
#         self.borrowed_books.append(book)
#         book.is_borrowed = True
#         print(f"{self.name} '{book.title}' kitobini ijaraga oldi.")
#     def return_book(self, book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.is_borrowed = False
#             print(f"{self.name} '{book.title}' kitobini qaytardi.")
#         else:
#             raise BookNotFoundException(f"{self.name} '{book.title}' kitobini ijaraga olmadi.")
# class Library:
#     def __init__(self):
#         self.books = []  
#         self.members = []  
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"'{book.title}' kutubxonaga qo'shildi.")
#     def add_member(self, member):
#         self.members.append(member)
#         print(f"{member.name} kutubxona a'zosi sifatida qo'shildi.")
#     def list_books(self):
#         if not self.books:
#             print("Kutubxonada hech qanday kitob mavjud emas.")
#         else:
#             print("Kutubxonadagi kitoblar:")
#             for book in self.books:
#                 status = "ijaraga olingan" if book.is_borrowed else "mavjud"
#                 print(f"'{book.title}' - {book.author} ({status})")
# class BookNotFoundException(Exception):
#     def __init__(self, message="Kitob kutubxonada mavjud emas."):
#         self.message = message
#         super().__init__(self.message)
# class BookAlreadyBorrowedException(Exception):
#     def __init__(self, message="Kitob allaqachon ijaraga olingan."):
#         self.message = message
#         super().__init__(self.message)
# class MemberLimitExceededException(Exception):
#     def __init__(self, message="Foydalanuvchi ruxsat etilgan kitoblar limitini oshirib yubordi."):
#         self.message = message
#         super().__init__(self.message)
# def asosiy_testlar():
#     kutubxona = Library()
#     kutubxona.add_book(Book("Alisher Navoiy", "Xamsa"))
#     kutubxona.add_book(Book("A.S. Pushkin", "Eugene Onegin"))
#     kutubxona.add_book(Book("J.K. Rowling", "Harry Potter"))
#     kutubxona.add_book(Book("J.R.R. Tolkien", "The Hobbit"))
#     member1 = Member("Ali")
#     member2 = Member("Sahro")
#     kutubxona.add_member(member1)
#     kutubxona.add_member(member2)
#     print("\nKutubxona kitoblari:")
#     kutubxona.list_books()
#     try:
#         member1.borrow_book(kutubxona.books[0])  
#         member1.borrow_book(kutubxona.books[1])  
#         member1.borrow_book(kutubxona.books[2])  
#         member1.borrow_book(kutubxona.books[3])  
#     except MemberLimitExceededException as e:
#         print(e)
#     try:
#         member2.borrow_book(kutubxona.books[2])  
#     except BookAlreadyBorrowedException as e:
#         print(e)
#     print("\nKutubxona kitoblari:")
#     kutubxona.list_books()
#     try:
#         member1.return_book(kutubxona.books[0])  
#     except BookNotFoundException as e:
#         print(e)
#     print("\nKutubxona kitoblari:")
#     kutubxona.list_books()
#     try:
#         member2.return_book(kutubxona.books[2])  
#     except BookNotFoundException as e:
#         print(e)
#     print("\nKutubxona kitoblari:")
#     kutubxona.list_books()
# asosiy_testlar()
################################# 5-misol ########################################
# import csv
# data = [
#     ["Name", "Subject", "Grade"],
#     ["Alice", "Math", 85],
#     ["Bob", "Science", 78],
#     ["Carol", "Math", 92],
#     ["Dave", "History", 74]
# ]
# with open('grades.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# print('grades.csv file has been created successfully.')
################################# 6-misol ########################################
# import csv
# from collections import defaultdict
# grades_data = []
# with open('grades.csv', mode='r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         grades_data.append(row)
# subject_grades = defaultdict(list)
# for row in grades_data:
#     subject = row['Subject']
#     grade = int(row['Grade'])
#     subject_grades[subject].append(grade)
# average_grades = {}
# for subject, grades in subject_grades.items():
#     average = sum(grades) / len(grades)
#     average_grades[subject] = round(average, 2)
# with open('average_grades.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Subject', 'Average Grade'])
#     for subject, average in average_grades.items():
#         writer.writerow([subject, average])
# print("average_grades.csv has been created successfully.")
################################# 7-misol ########################################
# import csv
# grades_data = []
# try:
#     with open('grades.csv', mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             grades_data.append(row)
# except FileNotFoundError:
#     print("Error: 'grades.csv' fayli topilmadi. Iltimos, faylni tekshirib ko'ring.")
#     exit()  
# subject_grades = {}
# for row in grades_data:
#     subject = row['Subject']
#     try:
#         grade = int(row['Grade'])  
#     except ValueError:
#         print(f"Xato: {row['Grade']} - bu yaroqsiz qiymat!")
#         continue  
#     if subject not in subject_grades:
#         subject_grades[subject] = []
#     subject_grades[subject].append(grade)
# average_grades = {}
# for subject, grades in subject_grades.items():
#     average = sum(grades) / len(grades)
#     average_grades[subject] = round(average, 2)
# try:
#     with open('average_grades.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Subject', 'Average Grade'])
#         for subject, average in average_grades.items():
#             writer.writerow([subject, average])
#     print("average_grades.csv fayli muvaffaqiyatli yaratildi.")
# except Exception as e:
#     print(f"Faylga yozishda xato yuz berdi: {e}")
################################# 8-misol ########################################
# import json
# tasks_data = [
#     {"id": 1, "task": "Kir yuvish", "completed": False, "priority": 3},
#     {"id": 2, "task": "Ovqat xarid qilish", "completed": True, "priority": 2},
#     {"id": 3, "task": "Darsni tugatish", "completed": False, "priority": 1}
# ]
# with open('tasks.json', 'w') as file:
#     json.dump(tasks_data, file, indent=4)
# print("Tasks.json fayli muvaffaqiyatli yaratildi va unga ma'lumotlar yozildi.")
################################# 9-misol ########################################
# import json
# def load_tasks():
#     try:
#         with open('tasks.json', 'r') as file:
#             tasks = json.load(file)
#             return tasks
#     except FileNotFoundError:
#         print("Error: 'tasks.json' fayli topilmadi.")
#         return []
#     except json.JSONDecodeError:
#         print("Error: 'tasks.json' fayli noto'g'ri formatda.")
#         return []
# def save_tasks(tasks):
#     with open('tasks.json', 'w') as file:
#         json.dump(tasks, file, indent=4)
#     print("O'zgartirishlar tasks.json fayliga saqlandi.")
# def display_tasks(tasks):
#     print("\n-- Mavjud Vazifalar --")
#     for task in tasks:
#         print(f"ID: {task['id']}, Vazifa: {task['task']}, "
#               f"Tamomlandi: {'Ha' if task['completed'] else 'Yo\'q'}, "
#               f"Ustuvorlik: {task['priority']}")
# def modify_task(tasks, task_id):
#     for task in tasks:
#         if task['id'] == task_id:
#             print(f"\nVazifa '{task['task']}' topildi.")
#             print("1. Vazifa nomini o'zgartirish")
#             print("2. Tamomlanish holatini o'zgartirish")
#             print("3. Ustuvorlikni o'zgartirish")
#             choice = input("Tanlang (1/2/3): ")
#             if choice == '1':
#                 new_task = input("Yangi vazifa nomini kiriting: ")
#                 task['task'] = new_task
#             elif choice == '2':
#                 new_completed = input("Tamomlandi (ha/yo'q): ").lower()
#                 task['completed'] = True if new_completed == 'ha' else False
#             elif choice == '3':
#                 new_priority = int(input("Yangi ustuvorlikni kiriting (1, 2, 3): "))
#                 task['priority'] = new_priority
#             else:
#                 print("Noto'g'ri tanlov!")
#             break
#     else:
#         print("Vazifa ID topilmadi.")
# def main():
#     tasks = load_tasks()
#     if not tasks:
#         print("Hech qanday vazifa mavjud emas.")
#         return
#     display_tasks(tasks)
#     task_id = int(input("\nO'zgartirmoqchi bo'lgan vazifa ID sini kiriting: "))
#     modify_task(tasks, task_id)
#     save_tasks(tasks)
# if __name__ == "__main__":
#     main()
################################# 10-misol ########################################
# import json
# def load_tasks():
#     try:
#         with open('tasks.json', 'r') as file:
#             tasks = json.load(file)
#             return tasks
#     except FileNotFoundError:
#         print("Error: 'tasks.json' fayli topilmadi.")
#         return []
#     except json.JSONDecodeError:
#         print("Error: 'tasks.json' fayli noto'g'ri formatda.")
#         return []
# def save_tasks(tasks):
#     with open('tasks.json', 'w') as file:
#         json.dump(tasks, file, indent=4)
#     print("O'zgartirishlar tasks.json fayliga saqlandi.")
# def display_tasks(tasks):
#     print("\n-- Mavjud Vazifalar --")
#     for task in tasks:
#         print(f"ID: {task['id']}, Vazifa: {task['task']}, "
#               f"Tamomlandi: {'Ha' if task['completed'] else 'Yo\'q'}, "
#               f"Ustuvorlik: {task['priority']}")
# def calculate_stats(tasks):
#     total_tasks = len(tasks)
#     completed_tasks = sum(1 for task in tasks if task['completed'])
#     pending_tasks = total_tasks - completed_tasks
#     average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
#     print("\n-- Vazifa Statistikasi --")
#     print(f"Jami vazifalar: {total_tasks}")
#     print(f"Tamomlangan vazifalar: {completed_tasks}")
#     print(f"Yakunlanmagan vazifalar: {pending_tasks}")
#     print(f"O'rtacha ustuvorlik: {round(average_priority, 2)}")
# def modify_task(tasks, task_id):
#     for task in tasks:
#         if task['id'] == task_id:
#             print(f"\nVazifa '{task['task']}' topildi.")
#             print("1. Vazifa nomini o'zgartirish")
#             print("2. Tamomlanish holatini o'zgartirish")
#             print("3. Ustuvorlikni o'zgartirish")
#             choice = input("Tanlang (1/2/3): ")
#             if choice == '1':
#                 new_task = input("Yangi vazifa nomini kiriting: ")
#                 task['task'] = new_task
#             elif choice == '2':
#                 new_completed = input("Tamomlandi (ha/yo'q): ").lower()
#                 task['completed'] = True if new_completed == 'ha' else False
#             elif choice == '3':
#                 new_priority = int(input("Yangi ustuvorlikni kiriting (1, 2, 3): "))
#                 task['priority'] = new_priority
#             else:
#                 print("Noto'g'ri tanlov!")
#             break
#     else:
#         print("Vazifa ID topilmadi.")
# def main():
#     tasks = load_tasks()
#     if not tasks:
#         print("Hech qanday vazifa mavjud emas.")
#         return
#     calculate_stats(tasks)
#     display_tasks(tasks)
#     task_id = int(input("\nO'zgartirmoqchi bo'lgan vazifa ID sini kiriting: "))
#     modify_task(tasks, task_id)
#     save_tasks(tasks)
# if __name__ == "__main__":
#     main()
################################# 11-misol ########################################
import json
import csv
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        print("Error: 'tasks.json' fayli topilmadi.")
        return []
    except json.JSONDecodeError:
        print("Error: 'tasks.json' fayli noto'g'ri formatda.")
        return []
def convert_json_to_csv():
    tasks = load_tasks()
    if not tasks:
        print("Hech qanday vazifa mavjud emas.")
        return
    with open('tasks.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Task', 'Completed', 'Priority'])
        writer.writeheader()  
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })
    print("tasks.csv fayli muvaffaqiyatli yaratildi.")
def main():
    convert_json_to_csv()
if __name__ == "__main__":
    main()
