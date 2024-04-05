import geopandas as gpd
from shapely.geometry import Point, LineString
import pandas as pd
import matplotlib.pyplot as plt
import requests

path = 'traceroute_results.csv'

def get_coordinates(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    coordinates = data.get('loc')
    if coordinates:
        latitude, longitude = map(float, coordinates.split(','))
        return [latitude, longitude]
    else:
        return []




# Load traceroute results from CSV
traceroute_results = pd.read_csv(path)

# Loop through traceroute results, and separate the rows by File and Address
for (file, address), group in traceroute_results.groupby(['File', 'Address']):
    # Loop through each row in the group
    previous_coordinates = []
    for i, row in group.iterrows():
        # Get the coordinates of the IP address
        data = get_coordinates(row['IP'])
        if data:
            print(data)
            print(row['IP'])
            print("----")
            latitude, longitude = data
            # Create a Point geometry for the IP address
            point = Point(longitude, latitude)
            # Add the Point geometry to the row
            traceroute_results.loc[i, 'geometry'] = point
            
            # if previous_coordinates != []:
            #     # Create a LineString geometry between the previous and current IP addresses
            #     line = LineString([Point(previous_coordinates), point])
            #     # Add the LineString geometry to the row
            #     traceroute_results.loc[i, 'geometry'] = line
            
            # # Update the previous coordinates
            # previous_coordinates = data

    # Convert the DataFrame to a GeoDataFrame
    gdf = gpd.GeoDataFrame(traceroute_results, geometry='geometry')

    # Plot the world map outline
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.boundary.plot(color='black', linewidth=0.5)

    # Plot the traceroute points
    gdf.plot(ax=plt.gca(), marker='o', color='red', markersize=5)

    # Set plot title
    plt.title(f"Traceroute Trajectory for {address}")
    plt.show()
    
    break
    