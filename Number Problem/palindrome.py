a = 121
temp = a
ans = 0

while a > 0:
    last = a%10
    a = a//10
    ans = (ans * 10 ) + last
    
if temp == ans :
    print('Palindrome')
else :
    print('Not Palindrome')