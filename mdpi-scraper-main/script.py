from datetime import datetime
import csv
from bs4 import BeautifulSoup
import requests

# sample page url to use for page url prompt
# https://www.mdpi.com/search?q=education

# https://www.mdpi.com/2073-4360/16/4/456/pdf?version=1707238581
def format_date_string(date_string):
    try:
        date_object = datetime.strptime(date_string, '%d %b %Y')
        formatted_date = date_object.strftime('%Y-%m-%d')
    except ValueError:
        formatted_date = None  # Return None if date parsing fails
    return formatted_date


base_url = "https://www.mdpi.com"
pageURL = input('Enter page address url📚: ')
date_from = input(
    "Enter start year for publication date (e.g 2023 or Hit enter to skip ⏭ ):  ")
date_to = input(
    'Enter end year for publication (e.g 2024 or Hit enter to skip ⏭ ): ')
filtered_url = f"{pageURL}&year_from={date_from}&year_to={date_to}"


print("Initializing...")

# Get the current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
dt_object = datetime.strptime(current_datetime, "%Y%m%d_%H%M%S")
# Extract year, month, and day
year = dt_object.year
month = dt_object.month
day = dt_object.day

csv_file = open(f'{year}-{month}-{day}.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'url', 'pdf_address', "pub_date"])

source = requests.get(filtered_url).text

soup = BeautifulSoup(source, 'lxml')
print("Scraping initiated...")
pdf_links = []
for article in soup.find_all('div', class_='article-item'):
    try:
        headline = article.find("a", class_='title-link').text
        article_link = f"{base_url}{article.find('a', class_='title-link')['href']}"
        pdf_link = f"{base_url}{article.find('a', class_='title-link')['href']}/pdf"
        reg_date = article.find('div', class_='color-grey-dark').text.split("-")
        pub_date = format_date_string(reg_date[-1].strip())
        pdf_links.append({"title": headline, "pdf_link": pdf_link})
    except:
        pass
    finally:
        csv_writer.writerow([headline, article_link, pdf_link, pub_date])


print('Request processed successfully ✅')
csv_file.close()
