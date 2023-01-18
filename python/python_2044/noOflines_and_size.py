import os
file=open(r"C:\Users\aman\Desktop\examplefile.txt",'r')
data=file.readlines()
count=0
for line  in data:
    count+=1 

print("Numbers of line in file is ",count," lines")
# size=os.path.getsize(r"C:\Users\aman\Desktop\examplefile.txt")
# print("Size of the file is ",size,"bytes")

size_pint=file.seek(0,os.SEEK_END)
print("Size of the file is ",file.tell(),"bytes")
file.close()