# Jugal Patel
# Lab 03: Soil Sampling 
# Email: jugal.patel@mcgill.ca
# November 1st, 2019

# Problem: geomorphologist needs help automating tasks 
# Solution: generating a plot of soil sample sites,  randomly assigning site to sample, and validating user input

# Import necessary modules
import matplotlib.pyplot as plt
import random

# Saskatchewan provincial boundaries 
# Individual variables associated with the bounding box of Saskatchewan. 
North = 60
South = 48.99
East = -101.36
West = -109.99

# Quadrant Split Values - simple maths to figure out midpoint:
xadd = (East - West)/2
#long_split = West + xadd # For task two, the variable is redefined below; hashed out to allow validation function

yadd = (North - South)/2
#lat_split = South + yadd # For task two, the variable is redefined below; hashed out to allow validation function

# Task two requires building a validation function. Here it is. Our input parameters are x and coord; the split specification and whether or not its lat or lon
def withinSask(x, coord): 
    if coord == "longitude":
        if x > West or x < East:
            return True
        else:
            return False
            print("FALSE")
    elif coord == "latitude":
        if x < North or x > South:
            return True
        else:
            return False
            print("FALSE")
    else:
        print("Please specify if this split test is for longitude or latitude; parameter missing")

#print("Longitudinal midpoint of Saskatchewan is at: {0}".format(long_split)) # We will use this split to define X quadrant boundaries
#print("Latitudinal midpoint of Saskatchewan is at: {0}".format(lat_split)) # We will use this split to define Y quadrant boundaries

# Ask user to input three variables: number of sites; latitude split; and longitude split
n_sites = int(raw_input("Please specify the number sites we want to sample"))

long_split = float(raw_input("Please specify the longitudinal split. This determines quadrant extent with respect to the X axis"))
while long_split < West or long_split > East:
    long_split = float(raw_input("Please try again; stay between {0} and {1}".format(West, East)))
    
lat_split = float(raw_input("Please specify the latitudinal split. This determines quadrant extent with respect to the Y axis"))
while lat_split > North or lat_split < South:
    lat_split = float(raw_input("Please try again; stay between {0} and {1}".format(North, South)))

#withinSask(long_split, 'longitude')
#withinSask(lat_split, 'latitude')

# Plot Saskatchewan as a rectangle
sask_lon = [-101.36, -101.36, -109.99, -109.99, -101.36]
sask_lat = [48.99, 60, 60, 48.99, 48.99]

plt.plot([sask_lon], [sask_lat])
plt.xlabel("Longitude")
plt.ylabel("Latitude")

for i in range(1, n_sites):
    rand_lat = random.uniform(South, North) # We want to generate random points that fall beteen Northern most and Southern most extent of Saskatchewan
    rand_long = random.uniform(East, West) # We want to generate random points that fall between the Eastern most and Western most extent of Saskatchewan
    
# Nested conditional statement to specifiy symbology for each of the four qudrants; split by longitudinal and latitudinal midpoints
    if rand_lat > lat_split: 
        if rand_long > long_split:
            sym = 'gv' # symbology is a green arrow if in NE quadrant
        else:
            sym = 'y^' # symbology is yellow arror if in NW quadrant
    else:
        if rand_long > long_split:
            sym = 'ro' # symbology is red circle if in SE quadrant
        else:
            sym = 'b+' # symbology is blue plus if in SW quadrant

    plt.plot(rand_long, rand_lat, sym)

plt.show()

