str = 'Siddharth'

freq = {}

for i in str :
    freq[i] = freq.get(i,0) + 1
    
print(freq)