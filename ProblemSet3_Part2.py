# Aaron Siegle 
# 10/7/2025

#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readline()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = str(lineList)

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

# Split the headerLineString into a list of header items
headerItems = headerLineString.split( "," )

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
#Split the data into values
    lineDatastring = str(lineString)
    parts = lineDatastring(",")
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = parts[mmsi_idx]
#Extract the fleet value
    fleet = parts[fleet_idx]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
#Printing the length of the vesselDict dictionary 
print(len(vesselDict))

# %% Task 4.4 - Using dictionary to find value 
vesselID = 440196000 

#Initialize key list
keys = []

#Loop through items in date_dict
for key, mmsi in vesselDict.items():
    if mmsi == vesselID:
        keys.append(key)

# Report if no record were found 
if len(keys) == 0: 
    print(f"No records were found on {vesselID}")

#Loop through keys and report locations
# for key in keys: 
    # location = location_dict[key]
    # lat = location[0]
    # lng = location[1]
    # print(f"On {user_date}, Sara the turtle was seen at {lat} Lat, {lng} Lng.")

# %% Question 5 - Loitering events - reading in the data 

# Python file object for loitering dataset 
fileObjLoit = open(file='data/raw/loitering_events_20180723.csv',mode='r')

# Constructing a list of all lines in the csv file 
lineListLoit = fileObjLoit.readlines()

#Release the link to the file objects 
fileObjLoit.close() #Close the file

# %% Question 5 - looping through the variables 
for ships in lineListLoit[1:]: 
# Split the string into a list of data items 
    shipsstring = str(ships)
    lineData = shipsstring.split(",")
# Store relevant values into their own variables 
    transshipment_mmsi = float(ships[0])
    starting_latitude = float(ships[1])
    starting_longitude = float(ships[2])
    ending_latitude = float(ships[3])
    ending_longitude = float(ships[4])
# Examine latitude parameters
    in_range_lat = starting_latitude < 0 and ending_latitude > 0
# Examine longtitude parameters 
    in_range_lon = 145 < starting_longitude < 155
# Determining if the latitude and the longitude constraints are true 
    if in_range_lat and in_range_lon:
        # Look up flag using MMSI
        fleet = vesselDict.get(transshipment_mmsi, "Unknown")
        print("Vessel #", mmsi, "flies the flag of", fleet)
# Bonus print value 
    # else: 
        # print("No vessels met criteria")
# %%
