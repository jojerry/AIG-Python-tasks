#This program is used to experiment the args functionslity in python 
""" The function Total is used to get a sum of the inputs provided"""


def total(*args):
    sum1=0
    for a in args:
        sum1 = sum1+a
    print (sum1)
total(1,2,3)


