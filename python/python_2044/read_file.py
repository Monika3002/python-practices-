# For reading the file we firt open a file in reading mode
file=open(r"C:\Users\aman\Desktop\examplefile.txt",'r')
# Decelare a variable for assigning the method
data=file.readlines()
# Runnning loop for printing the reading lines
for line in data:
    print(line,end="")
# At the end we close by file 
file.close()