# import sqlite3
# conn = sqlite3.connect('roster.db')
# cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Roster (
#         Name TEXT,
#         Species TEXT,
#         Age INTEGER
#     )
# ''')
# conn.commit()
# conn.close()
# print("Ma'lumotlar bazasi va Roster jadvali muvaffaqiyatli yaratildi.")
################################# 2-misol ########################################
# import sqlite3
# from tabulate import tabulate
# conn = sqlite3.connect('roster.db')
# cur = conn.cursor()
# cur.execute("SELECT * FROM Roster")
# rows = cur.fetchall()
# headers = ["Ism", "Turlar", "Yosh"]
# print("2.Ma'lumotlarni kiritish:\n")
# print("- Ro'yxat jadvalini quyidagi yozuvlar bilan to'ldiring:\n")
# print(tabulate(rows, headers=headers, tablefmt="grid"))
# conn.close()
################################# 3-misol ########################################
# data = {
#     'data_name': 'Jadzia Dax'
# }
# data['data_name'] = 'Ezri Dax'
# print("Yangilangan ism:", data['data_name'])
################################# 4-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 50, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 40, 'species': 'Bajoran'}
# ]
# bajoran_data = [char for char in data if char['species'] == 'Bajoran']
# for char in bajoran_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 5-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 68, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 67, 'species': 'Bajoran'}
# ]
# data = [char for char in data if char['age'] <= 100]
# for char in data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 6-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 68, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 67, 'species': 'Bajoran'}
# ]
# for char in data:
#     if char['name'] == 'Jadzia Dax' or char['name'] == 'Ezri Dax':
#         char['rank'] = 'Commander'
#     elif char['name'] == 'Kira Nerys':
#         char['rank'] = 'Major'
#     elif char['name'] == 'Worf':
#         char['rank'] = 'Lieutenant'
#     elif char['name'] == 'Bashir Julian':
#         char['rank'] = 'Doctor'
#     elif char['name'] == 'Kassidy Yates':
#         char['rank'] = 'Captain'
#     else:
#         char['rank'] = 'Ensign'
# for char in data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}, Rank: {char.get('rank', 'No rank')}")
################################# 7-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 150, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 120, 'species': 'Bajoran'}
# ]
# sorted_data = sorted(data, key=lambda char: char['age'], reverse=True)
# for char in sorted_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 2-Task #########################################
################################# 1-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 150, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 120, 'species': 'Bajoran'}
# ]
# sorted_data = sorted(data, key=lambda char: char['age'], reverse=True)
# for char in sorted_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 2-misol ########################################
# books = []
# books.append({'title': 'Deep Space Nine: The Siege', 'author': 'Peter David', 'year': 1994})
# books.append({'title': 'Unity', 'author': 'S.D. Perry', 'year': 2003})
# books.append({'title': 'Avatar, Book One', 'author': 'S.D. Perry', 'year': 2001})
# books.append({'title': 'A Stitch in Time', 'author': 'Andrew J. Robinson', 'year': 2000})
# books.append({'title': 'Rising Son', 'author': 'S.D. Perry', 'year': 2003})
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year']}")
################################# 3-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1984},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'year_published': 1932}
# ]
# for book in books:
#     if book['year_published'] == 1984:
#         book['year_published'] = 1950
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year_published']}")
################################# 4-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian'},
#     {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'genre': 'Dystopian'},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance'}
# ]
# for book in books:
#     if book['genre'] == 'Dystopian':
#         print(f"Sarlavha: {book['title']}, Muallif: {book['author']}")
################################# 5-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'year_published': 1932},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# books = [book for book in books if book['year_published'] >= 1950]
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year_published']}")
################################# 6-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# ratings = {
#     'To Kill a Mockingbird': 4.8,
#     '1984': 4.7,
#     'The Great Gatsby': 4.5
# }
# for book in books:
#     book['rating'] = ratings.get(book['title'], None)  
# for book in books:
#     print(f"Sarlavha: {book['title']}, Reyting: {book['rating']}")
################################# 7-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# sorted_books = sorted(books, key=lambda book: book['year_published'])
# for book in sorted_books:
#     print(f"Sarlavha: {book['title']}, Yili: {book['year_published']}")
