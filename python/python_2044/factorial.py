
n=int(input("Enter the Number to find its factorial : "))
factorial=1
for i in range(1,n):
    factorial=factorial*i
print("The factorial of ",n," is ",factorial)