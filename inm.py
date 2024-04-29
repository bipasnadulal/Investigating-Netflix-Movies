import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv")
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
netflix_movies=netflix_movies.dropna(subset=['duration'])
# netflix_movies['duration'] = pd.to_numeric(netflix_movies['duration'], errors='coerce')
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# print(short_movies)
# print(netflix_movies.head())
# print(netflix_movies.describe())
# print(netflix_movies['duration'].unique())

colors = []
for lab, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('yellow')
    elif row['genre'] == 'Documentaries':
        colors.append('red')
    elif row['genre'] == 'Stand-up':
        colors.append('green')
    else:
        colors.append('black')

colors[:10]


plt.figure(figsize=(12, 8))

plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")

plt.show()

