num = 10

# prev1 = 0
# prev2 = 1

# for i in range(2,num+1):
#     sum = prev1+prev2
#     print(sum)
#     prev1 = prev2
#     prev2 = sum
    
def fun(n):
    if n<=1:
        return n
    return fun(n-1) + fun(n-2)

for i in range(11):
    print(fun(i), end=" ")