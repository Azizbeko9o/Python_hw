################################# Task -1 ########################################


# # Task_1: Scrape weather information from an HTML file and process it using Python and BeautifulSoup.

# from bs4 import BeautifulSoup
# with open('homework/weather.html', 'r', encoding='utf-8') as fayl:
#     html = fayl.read()                                             #  Parse the HTML File:

# soup = BeautifulSoup(html, 'html.parser')                            #Display Weather Data:
# weather_data = []
# rows = soup.find('tbody').find_all('tr')
# for row in rows:
#     cells = row.find_all('td')
#     day = cells[0].text.strip()
#     temperature = int(cells[1].text.strip().replace('°C', ''))  
#     condition = cells[2].text.strip()
#     weather_data.append({'day': day, 'temp': temperature, 'condition': condition})
# print("5 kunlik ob-havo ma'lumotlari:")


# for data in weather_data:
#     print(f"{data['day']}: {data['temp']}°C, {data['condition']}")
# max_temp = max(data['temp'] for data in weather_data)
# hottest_days = [data['day'] for data in weather_data if data['temp'] == max_temp]
# print(f"\n Eng issiq kun(lar): {', '.join(hottest_days)} ({max_temp}°C)")
# sunny_days = [data['day'] for data in weather_data if data['condition'].lower() == 'sunny']
# print(f" Quyoshli kunlar: {', '.join(sunny_days)}")
# average_temp = sum(data['temp'] for data in weather_data) / len(weather_data)
# print(f"\n🌡 O'rtacha harorat: {average_temp:.1f}°C")




################################# Task-2 ########################################


                  # Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.




# import requests
# from bs4 import BeautifulSoup
# import sqlite3
# import pandas as pd
# from typing import List, Tuple
# DB_NAME = 'jobs.db'

# def create_db():
#     with sqlite3.connect(DB_NAME) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS jobs (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 title TEXT,
#                 company TEXT,
#                 location TEXT,
#                 description TEXT,
#                 application_link TEXT,
#                 UNIQUE(title, company, location)
#             )
#         ''')
#         conn.commit()

# def fetch_job_listings(url: str) -> List[Tuple[str, str, str, str, str]]:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     jobs_data = []
#     listings = soup.select('div.job') 
#     for job in listings:
#         title = job.select_one('.job-title').text.strip()
#         company = job.select_one('.company-name').text.strip()
#         location = job.select_one('.job-location').text.strip()
#         description = job.select_one('.job-description').text.strip()
#         application_link = job.select_one('a.apply-button')['href'].strip()

#         jobs_data.append((title, company, location, description, application_link))
    
#     return jobs_data

# def insert_or_update_jobs(jobs: List[Tuple[str, str, str, str, str]]):
#     with sqlite3.connect(DB_NAME) as conn:
#         cursor = conn.cursor()
#         for job in jobs:
#             title, company, location, description, link = job
#             cursor.execute('''
#                 SELECT description, application_link FROM jobs
#                 WHERE title=? AND company=? AND location=?
#             ''', (title, company, location))
#             result = cursor.fetchone()

#             if result is None:
               
#                 cursor.execute('''
#                     INSERT INTO jobs (title, company, location, description, application_link)
#                     VALUES (?, ?, ?, ?, ?)
#                 ''', (title, company, location, description, link))
#             else:
#                 old_desc, old_link = result
#                 if old_desc != description or old_link != link:
                   
#                     cursor.execute('''
#                         UPDATE jobs
#                         SET description=?, application_link=?
#                         WHERE title=? AND company=? AND location=?
#                     ''', (description, link, title, company, location))

#         conn.commit()

# def filter_jobs(location: str = None, company: str = None) -> pd.DataFrame:
#     query = "SELECT title, company, location, description, application_link FROM jobs WHERE 1=1"
#     params = []

#     if location:
#         query += " AND location LIKE ?"
#         params.append(f"%{location}%")
#     if company:
#         query += " AND company LIKE ?"
#         params.append(f"%{company}%")

#     with sqlite3.connect(DB_NAME) as conn:
#         df = pd.read_sql_query(query, conn, params=params)

#     return df

# def export_to_csv(df: pd.DataFrame, filename: str = 'filtered_jobs.csv'):
#     df.to_csv(filename, index=False)
#     print(f"Exported {len(df)} records to {filename}")


# if __name__ == "__main__":
#     create_db()
#     url = "https://example.com/jobs"  
#     job_listings = fetch_job_listings(url)
#     insert_or_update_jobs(job_listings)

    
#     filtered = filter_jobs(location="Tashkent")
#     export_to_csv(filtered)



################################# Task-3 ########################################

             # You are tasked with scraping laptop data from the "Laptops" section of the Demoblaze website and storing the extracted information in JSON format.


# import requests
# from bs4 import BeautifulSoup
# import json

# BASE_URL = "https://www.demoblaze.com/"
# LAPTOPS_URL = BASE_URL + "prodcat.html?id=Laptops"

# def get_page_soup(url):
#     """Sahifaning HTML tarkibini olish va BeautifulSoup bilan tahlil qilish."""
#     response = requests.get(url)
#     return BeautifulSoup(response.text, 'html.parser')

# def get_laptop_details(laptop_card):
#     """Har bir noutbukning nomi, narxi va tavsifini olish."""
#     name = laptop_card.find('h4', class_='card-title').text.strip()
#     price = laptop_card.find('h5').text.strip()
#     description = laptop_card.find('p', class_='card-text').text.strip()
#     return {
#         'name': name,
#         'price': price,
#         'description': description
#     }

# def scrape_laptops():
#     """Bir nechta sahifalardan noutbuklarni to‘plash va JSON formatida saqlash."""
#     laptops = []
#     current_page_url = LAPTOPS_URL

#     while current_page_url:
#         print(f"Scraping page: {current_page_url}")
#         soup = get_page_soup(current_page_url)

        
#         laptop_cards = soup.find_all('div', class_='card')

        
#         for card in laptop_cards:
#             laptop_data = get_laptop_details(card)
#             laptops.append(laptop_data)

        
#         next_button = soup.find('a', {'aria-label': 'Next'})
#         if next_button and 'href' in next_button.attrs:
#             next_page_url = BASE_URL + next_button.attrs['href']
#             current_page_url = next_page_url
#         else:
#             current_page_url = None

#     return laptops

# def save_to_json(data, filename="laptops.json"):
#     """To‘plangan ma'lumotlarni JSON faylga saqlash."""
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
#     print(f"Ma'lumotlar {filename} fayliga saqlandi.")


# if __name__ == "__main__":
#     laptops = scrape_laptops()  
#     save_to_json(laptops)  
