fib = [1,2]
ans = 0

while max(fib) < 4000000:
    sum_ = fib[-1] + fib[-2]
    fib.append(sum_)

for i in fib:
    if i%2==0:
        ans += i

print(ans)

