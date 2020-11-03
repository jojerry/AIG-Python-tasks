# this program is to do the fizzbuzz program where the program has to print Fizz for multiple of 3 and buzz for multiple of 5
def fizzbuzz():
    for i in range(1,100):
        if (i%3 ==0 and i%5==0):
            print("FizzBuzz")
        elif i%3 ==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()