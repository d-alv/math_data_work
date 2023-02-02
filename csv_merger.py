import os
import pandas as pd

# Specify the directory containing the CSV files
directory = "C:/Users/diego/Desktop/csv_prt_rico_summer"

# Use a list comprehension to create a list of all the file paths
files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

# Create an empty DataFrame to store the combined data
data = pd.DataFrame()
missing_data = pd.DataFrame()

# Iterate over the list of files
for file in files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    df.drop(['Date_Time'], axis=1, inplace=True)
    # Append the data to the combined DataFrame
    data = data.append(df, ignore_index=True)

# Group the data by longitude and latitude
grouped = data.groupby(['Latitude', 'Longitude'])

# Compute the mean of the "v" and "u" columns for each group
mean_data = grouped[['U', 'V']].mean()

# Reset the index to make the longitude and latitude columns into regular columns
mean_data.reset_index(inplace=True)

# Rename the columns of the mean dataframe
mean_data.columns = ['Latitude', 'Longitude', 'mean_U', 'mean_V']

# Merge the mean dataframe back to the original dataframe
merged_data = pd.merge(data, mean_data, on=['Latitude', 'Longitude'], how='left', suffixes=('_original', '_mean'))

# Drop the original "v" and "u" columns
merged_data.drop(['U_original', 'V_original'], axis=1, inplace=True)

# Rename the mean columns to the original "v" and "u"
merged_data.rename(columns={'mean_U': 'U', 'mean_V': 'V'}, inplace=True)

# Replace the NaN values in v and u columns with the original values
merged_data['U'].fillna(merged_data['mean_U'], inplace=True)
merged_data['V'].fillna(merged_data['mean_V'], inplace=True)

# Drop the original "v" and "u" columns
merged_data.drop(['mean_U', 'mean_V'], axis=1, inplace=True)

#save the final dataframe to a new csv file
merged_data.to_csv("merged_csv.csv", index=False)