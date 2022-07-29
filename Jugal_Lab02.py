# Jugal Patel
# Lab 02: City Information Dictionaries 
# Email: jugal.patel@mcgill.ca
# October 11, 2019

# Problem: comparisons of basic city information is tedious; proof-of-concept for Wikipedia/Jimmy Wales
# Solution: automating comparison of city information dictionaries, beta with five cities

# Program will greet the user:
print("Welcome to the Wikipedia City Information - currently in Beta") # WELCOME MESSAGE
city_list = ["Montreal", "Singapore", "Johannesburg", "Lima", "Arviat"] # LIST OF CITIES

print("Beta currently consists of the following cities:", city_list)
city = raw_input("Please select one of the above cities to explore").lower().capitalize() # RAW INPUT FROM USER; SELECT CITY # .lower() & capitalize() USED TO REMOVE K SENSITIVITY

# Create parent dictionary; consisting of five child dictionaries 
city_dict = {'Montreal': {'population': 1780000, 'category': 'reside in', 'fact': 'Montreal is verifiably the best city on Earth.', 'coordinates': (45.50, -73.56)}
             , 'Singapore': {'population': 5612000, 'category': 'want to visit', 'fact': 'Singapore is a major global transport and trade hub.', 'coordinates': (1.35, 103.82)}
             , 'Johannesburg': {'population': 957441, 'category': 'want to visit', 'fact': 'The Soweto township of Johannesburg was once home to Nelson Mendela.', 'coordinates': (-26.20, 28.04)}
             , 'Lima': {'population': 268352, 'category': 'have visited', 'fact': 'Places associated with Lima were once known as Limaq, named by Peruvian natives.', 'coordinates': (-12.04, -77.04)}
             , 'Arviat': {'population': 2657, 'category': 'want to visit', 'fact': 'Arviat, once known as Eskimo Point, is home to different forcibly relocated Inuit groups.', 'coordinates': (61.10, -94.06)}}

# Use keys function to return a list of city_dict keys
cd_list = list(city_dict.keys())

# Conditional statement to determine which key is associated with the selected city
city_out = [] # CREATE A NEW EMPTY LIST FOR USE IN IF STATEMENT
if city in cd_list: # IF USER SELECTED CITY IS IN OUR LIST OF CITIES, MAKE THEIR SELECTED CITY THE OUTPUT CITY
    city_out = city
else: 
    print("Sorry, for the Beta to work you must pick one of the following cities:", city_list)  # OTHERWISE FAIL
    exit()

name = str(city_out) # VAR FOR NAME OF CITY
population = int(city_dict[city_out]['population']) # VAR FOR POPULATION OF THE CITY
fact = str(city_dict[city_out]['fact']) # VAR FOR INTERESTING FACT

for coordinates in city_dict:  # EXTRACT ELEMENTS IN TUPLE TO ASSIGN TO LAT AND LONG
    latitude, longitude = city_dict[city_out]['coordinates']

# Formatted output
print("City Name:\t{0}\nPopulation:\t{1}\nInteresting Fact:\t{2}\nLatitude:\t{3}\nLongitude:\t {4}".format(name, population, fact, latitude, longitude))

# PART TWO:
# Comparing city size (population)
for city in city_dict:
    for compcity in city_dict:
        multiplier = (float(city_dict[city]['population'])/(city_dict[compcity]['population']))
        print('{0} is {1} x the size of {2}'.format(city, multiplier, compcity))
