#Default Arguments 
def average (a=4 , b=9):
  print ("The average is ", (a+b)/2)

average(4)    # it will ignore the value of a and take the value from the function call and takes the default value of b
  


def name(fname , mname = "john" , lname = "whatson"):
  print ("Hello,", fname , mname , lname)

name ("elon")

#Required Arguments 

def name(fname , mname ,lname ):
  print ("Hello,", fname , mname , lname)

name ("elon" , "musk" , "quill")

def greet(name , age):
  print("Hello", name , "you are" , age, "years old")

greet("Aliana", "18")  #In this case we have to give the value of the arguments in the same order as the function is defined.

#Keyword arguments

def name(fname , mname ,lname ):
  print("Hello,", fname , mname , lname)

name(mname = "john" , lname = "einstein" , fname = "Peter") #interpreter recognizes the arguments by the parameter name Hence, the the order in which the arguments are passed does not matter.

#Variable length arguments

