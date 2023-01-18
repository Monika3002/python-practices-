# Palidrome number are 101 ,202,465,564
# Taking a number from user
n = str(input("Enter a number : "))
# Printing the number in reverse order by indexing
rev=n[::-1]
# Checking the condition for palidrome number
if n==rev:
    print(n," is a palidrome number")
else:
    print(n," is a not a palidrome number")

