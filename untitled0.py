# Import digunakan untuk mengimport modul yang dibutuhkan
import requests
from bs4 import BeautifulSoup as bs
import csv

# URL yang akan di scrape
URL = 'https://proxyway.com/reviews'
titles_list = []

# Melakukan perulangan untuk mengabil data judul di setiap halaman
for page in range(1, 4):
    req = requests.get(f"{URL}/page/{page}")
    soup = bs(req.text, 'html.parser')
    titles = soup.find_all('h3')
    count = 1
    
    for title in titles:
        d = {}
        d['Page Number'] = f'Page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text.strip()
        count += 1
        titles_list.append(d)

# Menyimpan data ke dalam file CSV
filename = 'title_review.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Page Number', 'Title Number', 'Title Name'])
    writer.writeheader()
    writer.writerows(titles_list)

# Print keterangan jika proses scraping sukses dilakukan 
print("Scraping selesai. Data telah disimpan ke dalam file CSV.")