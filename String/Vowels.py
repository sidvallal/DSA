str = 'aeiou'
vowel = 0 
consonent = 0
for i in str:
    if i == 'a' or 'e' or 'i' or 'o' or 'u' :
        vowel += 1
    else:
        consonent += 1

print('Vowels : ', vowel)
print('Consonents : ',consonent)