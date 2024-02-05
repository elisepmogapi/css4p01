# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:58:06 2024

@author: Elisep Mogapi
"""

import pandas as pd
df = pd.read_csv('movie_dataset.csv')

#Question 1
df = pd.read_csv('movie_dataset.csv')
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]['Title'].values[0]
print('\nQ1')
print(highest_rated_movie)

#Question 2
average_revenue = df['Revenue (Millions)'].mean()
print('\nQ2')
print(average_revenue)

#Question3
# Filter the dataframe for movies released between 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
# Calculate the average revenue for the filtered movies
average_revenue_2015_2017 = filtered_df['Revenue (Millions)'].mean()
print('\nQ3')
print(average_revenue_2015_2017)

#Question4
# Filter the dataframe for movies released in 2016
movies_2016 = df[df['Year'] == 2016]
# Count the number of movies released in 2016
number_movies_2016 = len(movies_2016)
print('\nQ4')
print(number_movies_2016)

#Question5
# To find the number of movies directed by Christopher Nolan
number_movies_nolan_directed = df[df['Director'] == 'Christopher Nolan'].shape[0]
print('\nQ5')
print(number_movies_nolan_directed)

#Question6
# Count the number of movies with a rating of at least 8.0
number_high_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print('\nQ6')
print(number_high_rated_movies)

#Question7
# Filter the dataframe for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']
# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_directed = nolan_movies['Rating'].median()
print('\nQ7')
print(median_rating_nolan_directed)

#Question8
# Calculate the average rating for each year and find the year with the highest average rating
yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_rating = yearly_average_rating.idxmax()
print('\nQ8')
print(year_with_highest_rating)

#Question9
# Count the number of movies made in 2006
number_movies_2006 = df[df['Year'] == 2006].shape[0]
# Count the number of movies made in 2016
number_movies_2016 = df[df['Year'] == 2016].shape[0]
# Calculate the percentage increase
percentage_increase = ((number_movies_2016 - number_movies_2006) / number_movies_2006) * 100
print('\nQ9')
print(percentage_increase)

#Question10
from collections import Counter
# Combine all the actor names into a single list
all_actors = df['Actors'].str.split(', ').sum()
# Count the occurrences of each actor
actor_counts = Counter(all_actors)
# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0]
print('\nQ10')
print(most_common_actor)

#Question11
# Split the genres and create a list of all unique genres
unique_genres = set(df['Genre'].str.split(',').explode())
# Count the number of unique genres
number_unique_genres = len(unique_genres)
print('\nQ11')
print(number_unique_genres)

# Question12
# Exclude non-numeric columns
numeric_columns = df.select_dtypes(include='number')
# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

"""
Insights:

1. Positive correlation - exists between the movie rating and Metascore. A heightened rating tends to be linked with a higher metascore, suggesting that movies with better ratings generally receive more positive reviews.

2. There is no apparent connection between years and various movie attributes. The release year of a movie does not show a notable correlation with its rank, runtime, rating, votes, revenue, or Metascore. This suggests that the quality or success of a movie is not solely determined by its year of release.

3. There is an inverse relationship between the movie rank and the number of votes. Movies with lower ranks tend to have lower ratings and receive fewer votes.

4. There isn't a robust correlation between the duration of a movie and its revenue.

5. There is a moderate positive correlation between the movie's revenue and the number of votes it receives.

Advice for Directors:
- Focus on the storyline: A compelling and engaging plot is crucial for a successful movie.
- Understand your audience: Tailor the movie to the target demographic.
- Invest in good cinematography and visuals: Visual appeal enhances the overall viewing experience.
- Pay attention to pacing: A well-paced movie keeps the audience engaged.
- Seek feedback and adapt: Learn from audience reactions and adjust future projects accordingly.

"""

#Question13
"""
https://github.com/elisepmogapi/css4p01/upload/main
"""



















