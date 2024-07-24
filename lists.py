#lists
lst1 = [1,2,3,4,5,6]
lst2 = ["Red" , "Yellow", "Green", "Blue"]
print(lst1)
print(lst2)

#Mixed Data types
details = ["Neha", 18.7, "Female"]
print(details)

#Check whether an item is present in the list?
colors = ["Red", "Yellow","Orange", "Green"]
if "Yellow" in colors:
  print("Yellow is present")

else:
  print("Yellow is absent")
  
#List index 
marks = [1,6,7,8,9,5,4]
print(marks[4])
print(marks[len(marks)-4]) 
print(marks[-4])

#Slicing
Animals = ("Goat" , "Cow" , "Deer", "Buffalo", "Lion", "Tiger")
print(Animals[1:4])
print(Animals[1:])
print(Animals[-3])
print(Animals[1:6:2]) # printing every 3rd consecutive value withing a given range
print(Animals[-1:-2:-1])
