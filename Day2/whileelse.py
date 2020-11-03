# While loop with else block executed 
n=0
while n<10:
    print("n is lesser than 10 and the current number is :", n)
    n+=1
else:
    print("n is greater than or equal to 10 ", n)    

#while loop without else block execute and break statement execute
n= [1,2,3]
i=0
while i <= len(n):
    print(n[i])
    i+=1
    if i == len(n):
        break
else:
    print("I is equal to length of n")    


