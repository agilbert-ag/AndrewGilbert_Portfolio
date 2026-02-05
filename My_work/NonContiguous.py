# This code needs to be run in fresh environment.
# You can clone the default environment in ArcGIS by going to the project tab -> package manager -> select settings gear icon -> select 3 dots -> clone environment



!conda install -y geopandas shapely matplotlib

import geopandas as gpd
import numpy as np
import random
import matplotlib.pyplot as plt
from shapely import affinity
from shapely.strtree import STRtree

# This is the only file you need to input.
# However, the .shp must contain a columb by which you wish to scale each state by. Which in this case is 'StnPer100t'
# Read states shapefile
gdf = gpd.read_file(r"C:\GEOGVIZ\Week_11\noncontiguous\Data\Albersstates.shp")
print(gdf.columns)

# Calculate scale factors
gdf['scale_factor'] = gdf['StnPer100t']

min_scale = 0.1
max_scale = 3.0

dev = gdf['scale_factor']
gdf['scale_factor'] = min_scale + (dev - dev.min()) * (max_scale - min_scale) / (dev.max() - dev.min())

# Scale geometries around centroid
def scale_geometry(geom, scale):
    centroid = geom.centroid
    scaled = affinity.scale(
        geom,
        xfact=scale,
        yfact=scale,
        origin=(centroid.x, centroid.y)
    )
    return scaled

gdf['geometry'] = gdf.apply(lambda row: scale_geometry(row.geometry, row.scale_factor), axis=1)

# Separate overlapping polygons
def separate_polygons(gdf, max_iter=20, step=0.05):
    gdf = gdf.copy()  # Work on a copy
    for iteration in range(max_iter):
        tree = STRtree(gdf.geometry.values)
        moved = False
        
        for i in range(len(gdf)):
            geom = gdf.geometry.iloc[i]
            # Query returns indices of potentially intersecting geometries
            possible_matches = tree.query(geom)
            
            for j in possible_matches:
                if i == j:
                    continue
                    
                other_geom = gdf.geometry.iloc[j]
                
                if geom.intersects(other_geom):
                    c1 = geom.centroid
                    c2 = other_geom.centroid
                    dx = c1.x - c2.x
                    dy = c1.y - c2.y
                    
                    if dx == 0 and dy == 0:
                        dx = random.random() - 0.5
                        dy = random.random() - 0.5
                    
                    # Move current geometry away
                    geom = affinity.translate(geom, xoff=dx*step, yoff=dy*step)
                    moved = True
            
            gdf.at[gdf.index[i], 'geometry'] = geom
        
        if not moved:
            break
            
    return gdf

gdf = separate_polygons(gdf, max_iter=50, step=0.33)

# Plot the result
fig, ax = plt.subplots(figsize=(20, 14))
gdf.boundary.plot(ax=ax, color='lightgray', linewidth=2)
ax.set_axis_off()
#output path, the file type is svg 
plt.savefig(r"C:\GEOGVIZ\Week_11\noncontiguous\pop100tcartogram.svg", 
            format='svg',
            dpi=300,
            bbox_inches='tight',  # Removes extra whitespace
            transparent=True)      # Transparent background
plt.show()


# This code was written with assistance from AI.
