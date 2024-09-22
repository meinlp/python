from bs4 import BeautifulSoup
import requests

# this one scrapes a site with a list with the best movies of all times and puts it in the txt

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

film_list = []
for title in soup.find_all('h3'):
    film_list.append(title.text)

with open('film_list.txt', 'w') as file:
    for film in film_list[::-1]:
        file.write(film + '\n')
