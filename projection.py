import numpy as np
import netCDF4
from mpl_toolkits.basemap import Basemap
from pyproj import Proj
import matplotlib.pyplot as plt

# Open the NetCDF file
nc_file = netCDF4.Dataset("test_2.nc", "r")

# Extract the longitude and latitude values from the file
lons = nc_file.variables['longitude'][:]
lats = nc_file.variables['latitude'][:]
value1=np.where(lons==-67.37856293)
x=0
for val in lons: 
    if val == -67.3785629272461:
        print("it is at", x)
        x=0
    else:
       
        x+=1

z=0
for val in lats:
    if val == 18.167919158935547:
        print("it is at", z)
        z=0
    else:
    
        z+=1

print(len(lons))
print(len(lats))

value2=np.where(lats==18.16791916)


