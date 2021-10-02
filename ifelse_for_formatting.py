#What is the score?
score = float(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#Loops - Conditional and Count Controlled
# A condition-controlled loop uses a true or false condition to control the number of times that it repeats, like asking a user if they want to continue with their online shopping after they add something to their "basket." This type of loop is also called a while loop.
# A count-controlled loop repeats a specific number of times depending on the conditions, such as getting all the items in a list. This type of loop is also called a for loop.

x=0
while x <=5:
    print(x)
    x=x-1

for num in range(5):
    print(num*5)

counties = ["Arapahoe", "Denver", "Jeferson"]
for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")
for i in len(counties_tuples):

    print(counties_tuples[i])

for county in counties_tuples:

    print(counties)

#Iterate thru Dictionaries
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for i in counties_dict:
    print(i)

# we can also use the key method to get the above
for i in counties_dict.keys():
    print(i)
#similarly we can also get the values
for i in counties_dict.values():
    print(i)

for county in counties_dict:
    print(counties_dict[county])

#to print key, value pair on each line use the stmt below
for key, value in counties_dict.items():
    print(key, value)

print(counties_dict)

for county, voters in counties_dict.items():
    print(county, voters)
#or same can be written as:
for i, j in counties_dict.items():
    print(i,j) #i,j,county,voters they all are just references to the key-value pairs. we can call them anything
#skill DRILL
for i, j in counties_dict.items():
    print(i + " county has " + str(j) + " registered voters.")

#---------------------------------------------------------------#
#Formatting with F #
#print("I received " + str(percentage_votes)+"% of the total votes.") can be written as print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# print(county + " county has " + str(voters) + " registered voters.") can be written as print(f"{county} county has {voters} registered voters.")
# With F format no need to use + or convert variables. just use variables in {} brackets
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. " 
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)