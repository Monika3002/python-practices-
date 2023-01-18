file=open(r"C:\Users\aman\Desktop\examplefile.txt",'r')
data=file.readlines()
for line in data:
    print(line,end="")
file.close()