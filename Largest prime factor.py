primes = []
res = 0

for num in range(2, up + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

for k in primes:
    if 600851475143%k==0:
        res+=k

print(res)

