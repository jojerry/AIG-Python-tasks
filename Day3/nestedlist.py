#List comprehension examples
# first one shows the matrix transposed example

l=[[1,2,3],[11,22,33],[111,222,333]]

l_transpose=[[a[i] for a in l ] for i in range(3)]
print(l_transpose)


#list comprehension example2
#this will show the list comprehension of multiple lists

a=[1,2,3]
b=["apple","banana","orange"]
c=["India","america","Europe"]

l=[[x,y,z] for x in a for y in b for z in c]
print(l)