#CTL+ / comments out
from typing import TYPE_CHECKING


print ("hello world")
counties = ["Arapahoe", "Denver", "Jeferson"]
print(counties)

dir(list) # shows all different methods

# counties is a list
counties[1]  # print second position, since array/list starts at 0
counties[-1] #print the last item in the list
counties[-2] #print the second last item from the list

len(counties) # get the length of the list

#Slice List - Slicing is used to get specific items from a list. The format for slicing a list is as follows: list[start : end].
counties[0:2] # This will retrieve the first and second item from the list
counties[:2]    # This will run the same as above, first and seond item from list is retrieve
counties.append("El Paso") # Add item to the list
counties.remove("El Paso") # remove an item from the list
counties.insert(2, "El Paso") #Add item at Index 2
counties.pop(3) #remove 4th value
counties.pop(-1) #remove 

#Learning how to create Tuples
counties_tuple=("Arapahoe", "Denver", "Jeferson")
#to get Arphoe and Denver elements we use the syntax below
counties_tuple[:2]
#or
counties_tuple[:-1]

#--------------------------------------------------#
#Intro to Dictionaries aka Key value pairs
#The syntax for a dictionary is the key followed by a colon, which is followed by a value: {key:value}
#If there's more than one element or key-value pair in the dictionary they are separated by commas, like this: {key1:value1, key2:value2}
counties_dict={} # creating a dict
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
#GEt all the keys
counties_dict.keys() # get all the keys
counties_dict.values() # get all the values
#4ways to get number of registered voters in Araphoe county:
print(counties_dict.get("Arapahoe")) # we cqn use single or double quote here and the next three statements
counties_dict['Arapahoe']  
counties_dict.get("Arapahoe")  
print(counties_dict['Arapahoe']) 
#creating voting data:
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.remove({"county":"Arapahoe", "registered_voters": 432438})

#Input Data:
my_votes=int(input("How many votes did you get in the election"))
total_votes=int(input("Total votes in the election"))
percentage_votes=(my_votes/total_votes) *100
print("I got " +str(percentage_votes) + "% in this election")
if my_votes < total_votes:
    print("I lost")
else:
    print("I won the elections")

# If Else Statements
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


# IN and NOT IN
counties = ["Arapahoe", "Denver", "Jeferson"]
if "El Paso" not in counties:
    print("El Paso is not in the county list")
else:
    print("El Paso is found in the county list")    

#Logical and Boolean Operators
x=5
y=5
if x == 5 and y ==65:
    print("True")
else:
    print("False")
counties = ["Arapahoe", "Denver", "Jeferson"]
if "Arapahoe" in counties and "El Paso" in counties:
# we can use or here:     if "Arapahoe" in counties or "El Paso" in counties:
    print("Both are found in county list")
else:
    print("One of the items from counties not found in the county list")
