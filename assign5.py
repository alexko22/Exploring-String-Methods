# Task 1: Slicing and Indexing
var = "Python is amazing!"
# Slicing Operations
var1 = var[0:6]
var2 = var[10:17]
var3 = var[::-1]
# Printing our results...
print(var1)
print(var2)
print(var3)

# Task 2: String Methods
text = " hello, python world! "
text1 = text.strip()
text2 = text1.capitalize()
text3 = text2.replace("world", "universe")
text4 = text3.upper()
# Printing our results...
print(text4)

# Task 3: Checking for Palindromes
user = str(input("Enter your text: "))
# Get the reverse string
user_r = user[::-1]
# Displaying the appropriate message...
if (user == user_r):
    print("Yes", user, "is a palindrome!")
else:
    print("No", user, "is not a palindrome!")
