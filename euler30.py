def powerSummation(n):
    summ = 0
    number = n
    while(number > 0):
        d = number % 10
        number = int(number / 10)
        summ = summ + d**5
    return summ

suma = 0
# you can calculate the upper limi for the loop in the following manner
"""
the maximum sum in the fifth power of digits will be 
(n)*9**5 where n is the number of digits
for n=7
The max sum value will be  = 413343
This value is smaaler than the smallest of seven digit number  = 1,000,000
As n increases this diference will e even greater.
Thus you can rule out all numbers above 1 milion.
For n=6 the max sum is 354294 which  should be the upper limit in the for loop.
"""
for k in range(2,355000, 1):
    if k == powerSummation(k):
        suma = suma + k

print (suma)
