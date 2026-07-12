str = 'sky is blue'

# str = str.split()

# print(" ".join(str[::-1]))

stack = str.split()

result = []

while stack:
    result.append(stack.pop())
    
print(" ".join(result))