title = "Frankfurter"
years = 80
expert_status = True

print("Fahad is a proffessional " + title)
print("Exper status: " + str(expert_status)) # coversting expert_status
print(f"Expert Status: {expert_status}") # doesn't have to convert because we are using f stands for formatting

mylist=["Jacob",25,"ahmed",80]
print(mylist)

mylist.append("Matt")
print(mylist)

mylist[3]=85
print(mylist)

print(len(mylist))
mylist.pop(0)