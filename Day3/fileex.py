#this program is to experiment on read and readlines in files concept

with open("Testfile.txt","w") as f1:
    l=["orange","banana","mango"]
    for x in l:
        f1.write(x)
        f1.write("\n")
        
with open("testfile.txt") as f1:
    print(f1.readline())

with open("testfile.txt") as f1:
    result=f1.readlines()
    print(result)

