num = 1634

str_num = str(num)
n = len(str_num)
sum = 0

# total = sum(int(digit)**n for digit in str_num)
for i in range(0,n):
    sum += int(str_num[i])**n
    
if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# print(int(str_num[2])**n)