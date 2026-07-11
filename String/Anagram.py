s = 'silent'
t = 'listen'

# ss = sorted(s)
# tt = sorted(t)

# if ss == tt:
#     print("Anagram")
# else:
#     print("Not Anagram")

if len(s) != len(t):
    print('Not Anagram')
else:
    freq = {}
    
    for i in s:
        freq[i] = freq.get(i,0) + 1
        
    for i in t:
        if i not in freq:
            print('Not anagram')
            break
        
        freq[i] -= 1
        
        if freq[i] < 0:
            print('Not Anagram')
            break
    
    else:
        print('Anagram')