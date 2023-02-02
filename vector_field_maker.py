import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import rasterio

latitude = []
longitude = []
u = []
v = []
speed=[]

with open('data_speed_unit.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header
    for row in reader:
        print(row)
        latitude.append(float(row[0]))
        longitude.append(float(row[1]))
        u.append(float(row[5]))
        v.append(float(row[6]))
        speed.append(float(row[4]))

latitude = np.array(latitude)
longitude = np.array(longitude)

fig, ax = plt.subplots(figsize=(10, 10))

plt.figure(figsize=(10, 10))
map = Basemap(projection='merc', llcrnrlat=10, urcrnrlat=30, llcrnrlon=-80, urcrnrlon=-60, resolution='h',
              )
map.drawcoastlines()
ax.quiver(longitude, latitude, u, v, scale=120)
plt.show()