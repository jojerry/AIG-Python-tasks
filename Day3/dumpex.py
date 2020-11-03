import json
dic = {'alpha':1,"beta":2}   # this will convert the dict type to string json type 
x= json.dumps(dic)
print(x)
print(type(x))               # type would be str in this case

#now writing this string in a textfile 
with open("textfile1.txt","w") as f1:
    f1.write(x)
with open("textfile1.txt") as f1:
    print(f1.readline())


y=json.loads(x)               # this will convert the str to dict type
print(y)
print(type(y))                #type would be dict in this case

#now writing this dict in a textfile 
with open("textfile2.txt","w") as f1:
    f1.write(x)
with open("textfile2.txt") as f1:
    print(f1.readline())