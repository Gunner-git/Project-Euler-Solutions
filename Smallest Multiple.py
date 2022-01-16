ans = 0
i = 1

for i in range(2,1000000000000000000000000000000):
    for j in range(2,20):
        if i%j!=0:
            print(i)
            break
        else:
            ans = i
            break

print(ans)
