# Strings are immutable
str1 = "Hi I am Yogeshwari !!!"
print(str1.upper())
print(str1.lower())

str2 = "    a beautiful lady!!!   " #removes any white spaces before and after the string
print(str2.strip())

str3 = "Hello !!!@" #removes any trailing characters
print(str3.rstrip("!,@"))

print(str1.replace("Yogeshwari", "Pooja"))

print(str1.split(" ")) #splits the strings at the whitespaces

str4 = "introduction to python" #capitalize the first letter
print(str4.capitalize())

print(str1.center(40))
print(str1.center(40, "*"))

print(str2.count("a"))

str5 = "Welcome to the Console !!!"
print(str5.endswith("to", 4, 10))

print(str1.find("Yogeshwari"))
print(str1.find("Ishwari")) #if the string is not found it gives -1
str6 = "YogeshwariHaveSomeConciousnessIssues"
print(str6.isalnum())

str7 = "welcome"
print(str7.isalpha())
print(str2.islower())

print(str2.isprintable())

str8 = "   "         #using spacebar
print(str8.isspace())
str9 = "        "       #using Tab
print(str9.isspace())

str10 = "World Health Organization"
print(str10.istitle())

str11 = "world health organization"
print(str11.istitle())

str12 = "YOGESHWARI"
print(str12.isupper())

print(str10.startswith("World"))

print(str10.swapcase()) #changes the case of striong i.e. upper to lower and lower to upper case

print(str11.title())

