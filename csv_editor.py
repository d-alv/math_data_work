import os
import pandas as pd

# Specify the file path
file = "C:/Users/diego/Documents/GitHub/math_ia/merged_csv.csv"


#file = "C:/Users/diego/Desktop/csv_prt_rico_summer/file.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(file)

# Drop the Date_Time column
#data.drop(['Date_Time'], axis=1, inplace=True)

# Group the data by longitude and latitude
grouped = data.groupby(['Latitude', 'Longitude'])

# Compute the mean of the "U" and "V" columns for each group
mean_data = grouped[['U', 'V']].mean()

# Reset the index to make the longitude and latitude columns into regular columns
mean_data.reset_index(inplace=True)

# Rename the columns of the mean dataframe
mean_data.columns = ['Latitude', 'Longitude', 'mean_U', 'mean_V']

#save the final dataframe to a new csv file
mean_data.to_csv("merged_csv.csv", index=False)