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

def backtrack(i,n):
    if i<1:
        return

    backtrack(i-1,n)

    print(i)

# name(1,5)
backtrack(5,5)
