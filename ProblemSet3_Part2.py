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
for row in lineList[1:]:
#Split the data into values
    parts = row.split(",")
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = parts[mmsi_idx]
#Extract the fleet value
    fleet = parts[fleet_idx]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
#Printing the length of the vesselDict dictionary 
print(len(vesselDict))


# %% Task 4.4 
vesselID = 440196000 

