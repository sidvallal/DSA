def tot(i,n):

    if i<1:
        print(n)
        return
    tot(i-1,n+i)

tot(3,0)