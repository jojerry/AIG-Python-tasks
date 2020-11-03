#this program is to calculate the sqaure of the list  [1, 3, 3, 4, 5, 6] only if it is odd
n=[1, 3, 3, 4, 5, 6]
l= [x**2 for x in n if x%2!=0]
print(l)