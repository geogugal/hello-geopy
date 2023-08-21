# -*- coding: utf-8 -*-
"""Jugal_Lab04_Script2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B7hSjYLBR-Uj7qGS_1eDGrikKdT2DLke
"""

# Jugal Patel
# Lab 04.2: Global Land:Water Ratio
# Email: jugal.patel@mcgill.ca
# November 15th, 2019

# Problem: water policy experts want to know how much land there is relative to amount of surface water is in a given sqaure polygon across the globe
# Solution: generating grid of square polygons that covers Earth; then will add provided land shapefile to determine relative ratios of land and water for each sqaure

import shapely
import geopandas
from google.colab import drive
from geopandas import GeoDataFrame

# Mount Drive for reading/writing files
drive.mount("/content/gdrive")

# Import provided land shapefile
landshp = geopandas.read_file("/content/gdrive/My Drive/World_Land.shx")
union = landshp.unary_union

# Import our created grid
blank = geopandas.read_file("/content/gdrive/My Drive/test.shx")

# Intersect the grid and land files
intersect_poly = blank["geometry"].intersection(union)

# Iterate over the polygons and add to the land attribute if the polygon also exists in the World_Land.shx files
for i in range(len(intersect_poly.area)):
    ratio = intersect_poly.area[i] / 100
    blank["land"][i] = ratio

# Export new shapefile
blank.to_file("gdrive/My Drive/test2.shp")