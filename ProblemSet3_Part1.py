# Aaron Siegle 
# 10/7/2025
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

# Creating a for loop with user inputs 
for i in range(3): 
    user_input = int(input("Enter an integer: "))
    user_numbers.append(user_input)

user_numbers.sort()

# Printing the highest output 
print("The highest number is:", user_numbers[-1])

#%% Task 3 - Continuing Lists and Iteration  - Challenge Question
# empty list variable 
user_numbers = []

# Creating a for loop with user inputs 
for i in range(3): 
    user_input = int(input("Enter an integer: "))
    user_numbers.append(user_input)
    user_numbers.sort(reverse=True)
    print(user_numbers)
# %%
