#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='█')

#Read the entire contents into a list object
lineList = fileObj.█()

#Release the link to the file objects (now that we have all its contents)
fileObj.█() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = █

#Print the contents of the headerLine
print(█)