str1 = 'sid'

str = list(str1)
# print(str[::-1])
left = 0
right = len(str)-1

while left < right :
    str[left],str[right] = str[right],str[left]
    left +=1
    right -=1
    
res = "".join(str)
print(res)