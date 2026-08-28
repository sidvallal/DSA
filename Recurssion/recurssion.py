cnt = 0

def fun():

    global cnt

    if cnt == 5:
        return
    print(cnt, end=" ")
    cnt += 1

    fun()

def name(i,n):
    
    if i > n:
        return
    print('sid')
    name(i+1,n)

name(1,5)
