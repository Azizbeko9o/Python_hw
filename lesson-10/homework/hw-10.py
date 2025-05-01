# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# import uvicorn
# import webbrowser
# from weather_service import weather

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def home(request: Request):
#     weather = weather("Tashkent")
#     return templates.TemplateResponse("index.html", {"request": request, "weather": weather})

# if __name__ == "__main__":
#     url = "http://127.0.0.1:8000"
#     webbrowser.open(url)
#     uvicorn.run(app, host="127.0.0.1", port=8000)
# import requests

# def weather(shahar):
#     api_key = "181472b3e6c642ccfbdcb1698c57905c" 
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={shahar}&units=metric&appid={api_key}"
#     response = requests.get(url)
#     malumotlar = response.json()

#     ob_havo = {
#         "Shahar": shahar,
#         "temp": malumotlar["asosiy"]["temp"],
#         "tavsifi": malumotlar["ob_havo"][0]["tavsifi"],
#         "namlik": malumotlar["asosiy"]["namlik"],
#         "shamol": malumotlar["shamol"]["tezlik"]
#     }
#     return ob_havo
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather App</title>
# </head>
# <body>
#     <h1>Ob-havo: {{ malumotlar.shahar }}</h1>
#     <p>Harorat: {{ malumotlar.temp }} °C</p>
#     <p>Holati: {{ malumotlar.tavsifi }}</p>
#     <p>Namlik: {{ malumotlar.namlik }}%</p>
#     <p>Shamol: {{ malumotlar.shamol }} m/s</p>
# </body>
# </html>
################################# 2-misol ########################################
# import requests
# key = '181472b3e6c642ccfbdcb1698c57905c'
# city = 'Tashkent'
# URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

# response = requests.get(URL)

# if response.status_code == 200:
#     malumotlar = response.json()
#     temperatura = malumotlar['main']['temp']
#     namlik = malumotlar['main']['humidity']
#     ob_havo = malumotlar['weather'][0]['description']
#     shamol_tezligi = malumotlar['wind']['speed']

#     print(f"Ob-havo {city}:")
#     print(f"Temperatura: {temperatura}°C")
#     print(f"Namlik: {namlik}%")
#     print(f"Vaziyat: {ob_havo}")
#     print(f"Shamol tezligi: {shamol_tezligi} m/s")
# else:
#     print("Ma'lumotni olib bo'lmadi:", response.status_code, response.text)
################################# 3-misol ########################################
# import requests
# API_KEY = 'd2da6212bcbc1e8f86884b3d4554e633'  
# BASE_URL = "https://api.themoviedb.org/3"
# def kino_qidirish(query):
#     url = f"{BASE_URL}/search/movie"
#     params = {
#         "api_key": API_KEY,
#         "query": query,  
#         "language": "uz"  
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Ma'lumotni olishda xatolik yuz berdi:", response.status_code)
#         return None
# kino_data = kino_qidirish("Inception")
# if kino_data:
#     for kino in kino_data['results']:
#         print(f"Film nomi: {kino['title']}")
#         print(f"Qisqacha tavsifi: {kino['overview']}")
#         print(f"Chiqarilgan sana: {kino['release_date']}")
#         print(f"O'rtacha reyting: {kino['vote_average']}")
#         print(f"Kinoning ID raqami: {kino['id']}")
#         print("="*50)
################################# 4-misol ########################################
# import requests
# import random
# API_KEY = 'd2da6212bcbc1e8f86884b3d4554e633' 
# BASE_URL = 'https://api.themoviedb.org/3'
# def get_genres():
#     url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
#     response = requests.get(url)
#     genres = response.json().get('genres', [])
#     return {genre['name'].lower(): genre['id'] for genre in genres}
# def recommend_movie_by_genre(genre_name):
#     genres = get_genres()
#     genre_id = genres.get(genre_name.lower())
#     if not genre_id:
#         return f"'{genre_name}' janri topilmadi. Iltimos, boshqa janr kiriting."
#     url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
#     response = requests.get(url)
#     movies = response.json().get('results', [])
#     if not movies:
#         return f"'{genre_name}' janrida film topilmadi."
#     movie = random.choice(movies)
#     return f"Tavsiya etilgan film: {movie['title']} \n Tavsifi: {movie.get('overview', 'Tavsif yoq')}"
# if __name__ == "__main__":
#     genre_input = input("Qaysi janrda film ko'rmoqchisiz? (masalan: action, comedy, drama): ")
#     recommendation = recommend_movie_by_genre(genre_input)
#     print("\n" + recommendation)



