import os
import pandas as pd

import os
import pandas as pd

# Specify the directory containing the CSV files
directory = "C:/Users/diego/Desktop/csv_prt_rico_summer"

# Use a list comprehension to create a list of all the file paths
files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

# Create an empty DataFrame to store the combined data
data = pd.DataFrame()

# Iterate over the list of files
for file in files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)
    # Append the data to the combined DataFrame
    if data.empty:
        data = df
    else:
        data = data.append(df)

#save the final dataframe to a new csv file
data.to_csv("merged_csv.csv", index=False)