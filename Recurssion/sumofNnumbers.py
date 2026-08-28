def tot(i,n):

    if i<1:
        print(n)
        return
    tot(i-1,n+i)

def fun(n):

    if n==0:
        return 0

    return n + fun(n-1)

tot(3,0)
print(fun(3))