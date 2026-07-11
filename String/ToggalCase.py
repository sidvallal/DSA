str = 'Sid'

res = ""

for i in str :
    if i >= 'A' and i<= 'Z':
        res += chr(ord(i)+32)
    elif i >= 'a' and i<= 'z':
        res += chr(ord(i)-32)
    else:
        res += i
        
print(res)

# print(str.swapcase())
