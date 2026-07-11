str = 'madaam'

left = 0
right = len(str) - 1
f = 1
while left < right:
    if str[left] != str[right]:
        f = 0
        break
    else :
        left += 1
        right -= 1
if f:
    print('palindrome')
else :
    print('Not Palindrome')