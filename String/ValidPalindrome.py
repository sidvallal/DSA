str = "A man, a plan, a canal: Panamaa"

left = 0 
right = len(str)-1

while left <  right :
    while left < right and not str[left].isalnum():
        left +=1
    while left < right and not str[right].isalnum():
        right -=1
    
    if str[left].lower() != str[right].lower():
        print("Not Palindrome")
        break
    left += 1
    right -=1

else:
    print("palindrome")