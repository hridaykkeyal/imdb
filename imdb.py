from bs4 import BeautifulSoup
import requests

def invalid():
    print('\nINVALID OPTION')
    return

print('1. Movies')
print('2. TV Series')
print('3. Exit')

n=int(input('Choose option: '))

if n==1:
    url = 'http://www.imdb.com/chart/top'
elif n==2:
    url = 'http://www.imdb.com/chart/toptv'
elif n==3:
        print('\nThank You')
        exit()
else:
    invalid()
    exit()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]

imdb = []

for index in range(0, len(movies)):

    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()))
    movie_title = movie[len(str(index))+2:-7]
    year = int(movie[-5:-1])
    rank = index+1
    data = {'movie_title': movie_title,
            'year': year,
            'rank': rank,
            'cast': crew[index]}
    imdb.append(data)

for item in imdb:
    print(item['rank'], '-', item['movie_title'], '-', item['year'], '-','Starring:', item['cast'])

def rank():
    rank_search = int(input('\nEnter rank: '))

    for item in imdb:
        if rank_search == item['rank']:
            print(item['movie_title'])

    choose()

def year():
    year_search = int(input('\nEnter year: '))

    for item in imdb:
        if year_search == item['year']:
            print(item['movie_title'])

    choose()

def cast():
    cast_search = input('\nEnter name of cast: ')

    for item in imdb:
        if cast_search in item['cast']:
            print(item['movie_title'])

    choose()

def choose():
    print('\nSearch:')
    print('1. Rank')
    print('2. Year')
    print('3. Cast')
    print('4. Exit')

    option=int(input('Choose option: '))

    if option==1:
        rank()
    elif option==2:
        year()
    elif option==3:
        cast()
    elif option==4:
        print('\nThank You')
        exit()
    else:
        invalid()
        choose()

choose()
