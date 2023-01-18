# Taking two values from the user  to swap them later
a=str(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
# for swapping we use another varible and assigned values in each other
c=a
a=b
b=c
print( "Values of a and b after swapping  \na = ", a,"\nb = ", b)
