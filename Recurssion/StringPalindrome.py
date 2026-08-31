def check(s,l,r):

    if l>r:
        return True
    
    if s[l] != s[r]:
        return False

    return check(s,l+1,r-1)



s = "aabaa"
print(check(s,0,4))

