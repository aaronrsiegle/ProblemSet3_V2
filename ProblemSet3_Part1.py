#%% Task 1 - Edit code to print as requested
# Defining variables 

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = "20322'"

# Creating print statement
print (mountain + ", formerly \nknown as " + nickname + ","
" \nis " + elevation + ' above sea level.' )

#%% Task 2 - Lists and Iteration
# Assigning first variable name 
data_folder = r"W:\859_data\triangle" + "\\"

# Creating a list object 
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

# Creating user item variable 
user_item = "roads.shp"

# Adding user item to data list 
data_list.append(user_item)

# Using a for loop to print the full path of each dataset 
for file_path in data_list: 
    full_path = data_folder + file_path
    print(full_path)

#%% Task 3 - Continuing Lists and Iteration 
# empty list variable 
user_numbers = []
user_input = input("Enter an integer:")

# Creating a for loop with user inputs 
for numbers in range(20): 
    user_numbers.append(user_input)
    print(user_numbers)