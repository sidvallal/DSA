s = "aabb"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0)+1
    
for i in freq.values():
    if i == 1:
        print(i-1)
        break
else:
    print("-1")