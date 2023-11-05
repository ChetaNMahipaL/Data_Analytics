import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

with open('q1text.csv', 'w', newline='', encoding='utf-8') as csvfile:

    # create a writer object
    writer = csv.writer(csvfile)

    writer.writerow(['Title', 'Year', 'Duration', 'Rating', 'Gross', 'Genre'])

    for page_num in range(1, 11):
        url = f'https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page={page_num}&sort=list_order,asc'

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        movie_items = soup.find_all('div', class_='lister-item mode-detail')

        for movie in movie_items:
            title = movie.h3.a.text
            if (title == "The Lion King"):
                year = movie.h3.find('span', class_='lister-item-year').text
                title ="The Lion King" + year
            year = movie.h3.find('span', class_='lister-item-year').text[-5:-1] # extract only year value
            duration = movie.find('span', class_='runtime').text
            rating = movie.find('span', class_='ipl-rating-star__rating').text

            gross_element = movie.find('span', class_='text-muted', text='Gross:')
            if gross_element:
                gross = gross_element.find_next_sibling('span').text.strip()
            else:
                gross = None

            genre_element = movie.find('span', class_='genre')
            if genre_element:
                genre = genre_element.text.strip()
            else:
                genre = None

            writer.writerow([title, year, duration, rating, gross, genre])

df = pd.read_csv('q1text.csv')
df1 = pd.read_csv('q1text.csv')

df['Genre'] = df['Genre'].str.split(', ')

df = df.explode('Genre')

genre_counts = df['Genre'].value_counts()

df1['Gross'] = df1['Gross'].str.replace('$', '').str.replace('M', '').astype(float)

top_100 = df1.nlargest(100, 'Gross')

# Create a bar graph
plt.bar(genre_counts.index, genre_counts.values)

plt.title('Movie Frequency by Genre')
plt.xlabel('Genre')
plt.ylabel('Frequency')

plt.xticks(rotation=45)

plt.savefig('graph1.png')

# Create a new figure for the line graph
plt.figure()

# Create a line graph
plt.plot(top_100['Title'], top_100['Gross'])

plt.title('Top 100 Movies by Gross Value')
plt.xlabel('Movie Title')
plt.ylabel('Gross Value (in millions)')

plt.xticks(rotation=90)

plt.savefig('graph2.png')
plt.show()