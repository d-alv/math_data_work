import os
import pandas as pd

# Specify the file path
file = "C:/Users/diego/Documents/GitHub/math_IA/modified_file.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file)
#df.drop(['Date_Time'], axis=1, inplace=True)

# Group the data by longitude and latitude
grouped = df.groupby(['Latitude', 'Longitude'])

# Compute the median of the "v" and "u" columns for each group
median_data = grouped[['U', 'V']].median()

# Reset the index to make the longitude and latitude columns into regular columns
median_data.reset_index(inplace=True)

# Rename the columns of the median dataframe
median_data.columns = ['Latitude', 'Longitude', 'median_U', 'median_V']


median_data.to_csv("median_merged_csv.csv", index=False)