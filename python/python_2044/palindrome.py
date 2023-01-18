# Palidrome number are 101 ,202,465,564
n= str(input("Enter a number : "))
a=n[::-1]
if n==a:
    print(n," is a palidrome number")
else:
    print(n," is a not a palidrome number")

