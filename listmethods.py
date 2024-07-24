#List methods 

#list.sort
colors = ["violet", "indigo", "blue", "yellow",  "orange"]
colors.sort()
print(colors)
num = [1,2,6,8,9,4,3,6,5]
num.sort()    #gives output in ascending order
print(num)

num.sort(reverse=True)    #gives output in descending order
print(num)

Animals = ["Tiger", "Lion", "Cheetah", "Leopard", "Jaguar"]
Animals.reverse()    #reverse the order of the list
print(Animals)

Birds = ["Peacock", "Parrot", "Dove", "Crow", "Pigeon","Parrot"]
print(Birds.index("Dove"))    #gives the index of the given value
print(Birds.count("Parrot"))  #gives the count of the given value
newlist = Birds.copy()        #copies the list
print(newlist)
Birds.append("Sparrow")       #this appends the given value at the end of the list
print(Birds)               

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

#concatenating two lists
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
