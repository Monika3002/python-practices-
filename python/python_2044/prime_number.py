# Taking a number from user
n=int(input("Enter a number : "))
if n>1:
    for i in range(2,n):
# checking the conditions for prime number
     if( n % i ==0):
         print (n," is not a prime number.")
         break
    else :
         print(n," is a prime number.")

else:
     print (n," is not a prime number.")