def powerSummation(n):
    summ = 0
    number = n
    while(number > 0):
        d = number % 10
        number = int(number / 10)
        summ = summ + d**5
    return summ

suma = 0

#upper limit from the web for the loop
for k in range(2,355000, 1):
    if k == powerSummation(k):
        suma = suma + k

print (suma)