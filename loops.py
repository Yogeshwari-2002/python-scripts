#for loop

# name = "Yogeshwari"
# for i in name:
#     print(i, end=",")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):  #including 0 but not 5
  print(k)

for k in range(1,9): #adding 1 to starting value
  print(k+1)

for k in range(5,20,4): #this is called as step parameter in which it will the value of k+4
  print(k)


# while loop

i=int(input("Enter the number:"))
while(i>=38):
   i=int(input("Enter the number:"))
   print(i)

print("Done with the loop")


count = 10
while (count > 0):
  print(count)     #increment or decrement the counter variable
  count = count - 1

#Else with While Loop

x=5
while(x<0):
  print(x)
  x=x-1
else:
  print("Conter is 0")
