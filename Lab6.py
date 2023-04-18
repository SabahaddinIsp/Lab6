import math

#**************        QUESTION-1     *******************************
n = input("Enter n for the function e^n = 1 + n/1! + n^2/2! + ... + n^x/x!:   ")
x = input("Enter the step size x for the function e^n = 1 + n/1! + n^2/2! + ... + n^x/x!:  ")
result = 1
temp = lambda i,j : int(i)**int(j) / math.factorial(j)
for i in range(1,int(x)+1):
    result = result + temp(n,i)
print(result)


#**************      QUESTION-2          *******************************

sum = 0

def function(n):
    ''' This functions sums up numbers to the given step size'''
    global sum
    while (n > 0):

        temp = lambda j:  (-1) ** (j+1) / j
        sum = sum + temp(n)
        n = n - 1

print(function.__doc__)

x = int(input("Enter the step size of the function"))
function(x)
print(sum)