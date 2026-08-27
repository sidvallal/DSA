s = input()
temp = "aoyeui"
ans = ""

for ch in s:
    if ch.lower() in temp:
        s = s.replace(ch,"")
    else:
        ans = ans + "."
        ans = ans + ch.lower()

print(ans)
