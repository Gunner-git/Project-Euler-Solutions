for i in range(100,1000):
    for j in range(100,1000):
        s = str(i*j)
        if len(s)%2==1:    
            compare = s.split(s[(len(s)//2)])
            print(compare)
            rev = [str(i) for i in compare[1]]
            print(rev)
            l = [str(i) for i in compare[1]]
            print(l)
            rev.reverse()
            print(rev)
            temp = "".join(rev)
            if compare[0] == temp:
                print(s)
        else:
            l = [str(i) for i in s]
            l.insert(len(s)//2, ",")
            y = "".join(l)
            x = y.split(",")
            rev = [str(k) for k in x[1]]
            rev.reverse()
            rev = "".join(rev)
            if x[0] == rev:
                print(s)
