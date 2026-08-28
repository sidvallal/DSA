cnt = 0

def fun():

    global cnt
    
    if cnt == 5:
        return
    print(cnt, end=" ")
    cnt += 1

    fun()

fun()
