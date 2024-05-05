# converting string to integer

string = "10"
number = 7

sum = number + int(string) #throws an error if the string is not valid integer 
print("The sum of the numbers is : ", sum)

#converting float number to integer 

float_number = 7.9
number = 7

sum = number + int(float_number)
print("The sum of the numbers is : ", sum)

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float as it is a float addition
c = a + int(b)
print(c)
print(type(c))
