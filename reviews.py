# In this exercise we will create a summary of wine reviews by country and write the data to a CSV file.
# This exercise is based on the Kaggle Learn Pandas exercise 3.
# Create a Python program that reads in the `data/winemag-data-130k-v2.csv.zip` file. 
# Create a summary of the data that contains the name, number of reviews, and the average points for each unique country in the dataset. 
    # Write the summary data to a new file in the `data` folder named `reviews-per-country.csv`.

import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

summary_df = df.groupby('country').agg({'title': 'count', 'points': 'mean'}).round(1)

summary_df = summary_df.rename(columns = {'title': 'count'}).reset_index()

summary_df = summary_df.sort_values('count', ascending = False)

summary_df.to_csv('data/reviews-per-country.csv', index = False)
