import os
import netCDF4

folder_path = "C:/Users/diego/Documents/GitHub/math_IA/math_data_PR_nc"

# Initialize empty lists to store the results

min_lons = []
max_lons = []
min_lats = []
max_lats = []

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a NetCDF file
    if filename.endswith(".nc"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        # Open the NetCDF file
        nc_file = netCDF4.Dataset(file_path, "r")
        print(nc_file.variables.keys())

        # Get the longitude and latitude variables
        crs= nc_file.variables['crs']
        longitude = nc_file.variables["longitude"]
        latitude = nc_file.variables["latitude"]

        # Get the minimum and maximum values
        min_lon = longitude[:].min()
        max_lon = longitude[:].max()
        min_lat = latitude[:].min()
        max_lat = latitude[:].max()

        # Append the results to the lists
        min_lons.append(min_lon)
        max_lons.append(max_lon)
        min_lats.append(min_lat)
        max_lats.append(max_lat)
        print(len(longitude))
        print(len(latitude))

        # Close the file
        nc_file.close()

# Print the results
print("Minimum longitudes: ", min_lons)
print("Maximum longitudes: ", max_lons)
print("Minimum latitudes: ", min_lats)
print("Maximum latitudes: ", max_lats)