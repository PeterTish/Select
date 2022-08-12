import requests
from pprint import pprint
import sqlalchemy
from sqlalchemy import create_engine

# Spotify
url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"<REQUIRED>","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "9cbef57cacmsh98bbc2e0574f4e8p1ef946jsne3c0f9fd9d31",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()
Musician = response['albums']['items']


'''Name musician, ID musician, Album, Release year'''
Name_Musician = []
Id_Musician = []
Album = []
Release_year = []
for i in Musician:
	musician = i['data']['artists']['items']

	Album.append(i['data']['name'])
	Release_year.append(int(i['data']['date']['year']))

	for name in musician:
		if name['profile']['name'] not in Name_Musician:
			Name_Musician.append(name['profile']['name'])

		if name['uri'][15:-1] not in Id_Musician:
			Id_Musician.append(name['uri'][15:-1])

album_release = dict(zip(Album, Release_year))
collections = {'Top-5': 1985, 'Top-10':1986, 'Top-15':1987, 'Top-15':2000, 'Top-20':2020, 'Top-25':2016, 'Top-30':2017, 'Top-35':2012}
genre = ['Pop', 'Jazz', 'Blues', 'Rock', 'Folk', 'Classical']




engine = create_engine("postgresql+psycopg2://postgres:Kybuk241194@localhost/homework")

db = 'postgresql://postgres:Kybuk241194@localhost:5432/homework'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# Musician
# for name in Name_Musician:
# 	connection.execute(f"""INSERT into musician(nickname) VALUES('{name}');""")

# Album & release year
# for k,v in album_release.items():
# 	connection.execute(f"""INSERT into album(name, release) VALUES('{k}', {v});""")

# Collection
# for k,v in collections.items():
# 	connection.execute(f"""INSERT into collection(name, release) VALUES('{k}', {v});""")

# Genre
# for g in genre:
# 	connection.execute(f"""INSERT into genre(name) VALUES('{g}');""")















