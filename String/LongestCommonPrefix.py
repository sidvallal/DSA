str = ["flower", "flow", "flight"]

prefix = str[0]

for word in str[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        
        if prefix == "":
            break
        
print(prefix)