# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def damage_conv(list):
    new_list = []
    for i in list:
        if i == 'Damages not recorded':
            new_list.append(i)
        else:
            new_list.append(float(i[:-1])*conversion[i[-1]])
    return new_list

# test function by updating damages
damages_updated = damage_conv(damages)
print(damages_updated)
# 2 
# Create a Table
hurricanes_by_name = {}
for i in range(len(names)):
    hurricanes_by_name.update({names[i]: {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages_updated[i], 'Deaths': deaths[i]}})
# Create and view the hurricanes dictionary
print(hurricanes_by_name)
# 3
# Organizing by Year
hurricanes_by_year = {}
# create a new dictionary of hurricanes with year and key
for i in range(len(years)):
    hurricanes_by_year.update({years[i]: []})
for i in range(len(years)):
    hurricanes_by_year[years[i]].append([{'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': damages_updated[i], 'Deaths': deaths[i]}])
print("\n", hurricanes_by_year)
# 4
# Counting Damaged Areas
damaged_areas = {}
def get_damaged_area_count(dam_area):
    dam_area_count = 0
    for list in areas_affected:
        for area in list:
            if area == dam_area:
                dam_area_count += 1
    return dam_area_count
# create dictionary of areas to store the number of hurricanes involved in
for list in areas_affected:
    for area in list:
        damaged_areas.update({area: get_damaged_area_count(area)})
print("\n", damaged_areas)

# 5
# Calculating Maximum Hurricane Count
def get_max_affected_area():
    max_affected = ''
    for i in damaged_areas.keys():
        if damaged_areas[i] > damaged_areas.get(max_affected, 0):
            max_affected = i
    return max_affected, damaged_areas[max_affected]
# find most frequently affected area and the number of hurricanes involved in
a, b = get_max_affected_area()
print("\nMost affected area: {}, hit {} times.".format(a,b))

# 6
# Calculating the Deadliest Hurricane
def get_deadliest_hurricane():
    max_deaths = next(iter(hurricanes_by_name))
    for i in hurricanes_by_name:
        if hurricanes_by_name[i]['Deaths'] > hurricanes_by_name[max_deaths]['Deaths']:
            max_deaths = i
    return max_deaths, hurricanes_by_name[max_deaths]['Deaths']

# find highest mortality hurricane and the number of deaths
a, b = get_deadliest_hurricane()
print("Deadliest hurricane was {} with {} deaths.".format(a, b))
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def get_hurricane_mortality_scale(hurricane_name):
    deaths = hurricanes_by_name[hurricane_name]['Deaths']
    if deaths == 0:
        return 0
    elif deaths <= 100:
        return 1
    elif deaths <= 500:
        return 2
    elif deaths <= 1000:
        return 3
    else:
         return 4

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
for hurricane in hurricanes_by_name:
    hurricanes_by_mortality[get_hurricane_mortality_scale(hurricane)].append(hurricane)
print("\nHurricanes on the mortality scale:", hurricanes_by_mortality)

# 8 Calculating Hurricane Maximum Damage
def get_most_damaging_hurricane():
    max_damage = 0
    most_damaging = ''
    for i in range(len(damages_updated)):
        if type(damages_updated[i]) == float:
            if damages_updated[i] > max_damage:
                most_damaging = names[i]
                max_damage = damages_updated[i]
    return most_damaging
# find highest damage inducing hurricane and its total cost
print("\nMost damaging hurricane:", get_most_damaging_hurricane())

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
hurricanes_by_damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}

def get_hurricane_damage_scale(hurricane_name):
    damage = hurricanes_by_name[hurricane_name]['Damage']
    if damage == 'Damages not recorded':
        return 0
    elif damage <= 100000000:
        return 1
    elif damage <= 1000000000:
        return 2
    elif damage <= 10000000000:
        return 3
    else:
         return 4
# categorize hurricanes in new dictionary with damage severity as key
for hurricane in hurricanes_by_name:
    hurricanes_by_damage_scale[get_hurricane_damage_scale(hurricane)].append(hurricane)
print("\nHurricanes on the damage scale:", hurricanes_by_damage_scale)
