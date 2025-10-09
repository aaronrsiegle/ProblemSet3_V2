# Aaron Siegle 
# 10/8/2025
# For total commit history, see 'ProblemSet_V2" repo in GitHub. My GitHub username is aaronrsiegle

#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = str(lineList[0])

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
    parts = lineString.split(",")
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = parts[mmsi_idx]
#Extract the fleet value
    fleet = parts[fleet_idx]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
#Printing the length of the vesselDict dictionary 
print(len(vesselDict))

# %% Task 4.4 - Using dictionary to find value 
# Creating keys to make it easier to navigate the VesselDict dictionary 
vessels = []
vesselDict = {v["mmsi"]: v for v in vessels}

# Assigning value to look for 
vesselID = 440196000 

# Searching for a particular vessel
if vesselID in vesselDict: 
    flag = vesselDict[vesselID]["fleet_name"]
    print(f"Vessel # {vesselID} flies the flag of {flag}")
else: 
    print(f"Vessel # {vesselID} not found in vesselDict")


# %% Question 5 - Loitering events - reading in the data 

# Python file object for loitering dataset 
fileObjLoit = open(file='data/raw/loitering_events_20180723.csv',mode='r')

# Constructing a list of all lines in the csv file 
lineListLoit = fileObjLoit.readlines()

#Release the link to the file objects 
fileObjLoit.close() #Close the file

# %% Question 5 - looping through the variables 
# Setting up the bonus points print value 
hits = 0 

for ships in lineListLoit[1:]: 
# Split the string into a list of data items 
    lineData = ships.strip().split(",")
# Store relevant values into their own variables 
# Using float for decimal and integer for whole numbers because all the values we are working are numeric and the string version of the data was returning errors 
    transshipment_mmsi = int(lineData[0])
    starting_latitude = float(lineData[1])
    starting_longitude = float(lineData[2])
    ending_latitude = float(lineData[3])
    ending_longitude = float(lineData[4])
# Examine latitude parameters - does the boat cross the equator? 
    in_range_lat = (starting_latitude < 0) and (ending_latitude > 0)
# Examine longtitude parameters 
    in_range_lon = 145 < starting_longitude < 155
# Determining if the latitude and the longitude constraints are true 
    if in_range_lat and in_range_lon:
        # Look up the fleet name from the vesselDict dictionary 
        fleet = vesselDict.get(fleet, "Unknown")
        print(f"Vessel #{transshipment_mmsi} flies the flag of {fleet}")
        hits += 1 

# If nothing is returned, then the error message below is returned 
if hits == 0:
    print("No vessels met criteria")


# %%
