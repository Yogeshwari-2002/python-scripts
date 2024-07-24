letter = "Hey , my name is {1}  and I am from {0}"
country = "India"
name = "Yogeshwari"
print(letter.format(country, name))        #formats any string in a given sequence or index we provide to string
print(f"Hey , my name is {name} and I am from {country}")  #f-string

print(f"We use f-string like this : Hey , my name is {{name}} and I am from {{country}}")


print(f"{2*40}")   # we can also use f-string in a single statement .

price = 49.7890
txt = f"for only price {price:.3f} dollars!"    #.3f is used to print only 3 decimal points .
print(txt)
