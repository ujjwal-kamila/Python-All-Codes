# Character Hashing


s = "azyxyyzaaaa"
q = ["d","a","y","x"]
hash_list = [0] * 27

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val-97
    hash_list[index] +=1
    
print(hash_list)

for ch in q:
    print(f"{ch}",end = ' -- ')
    ascii_val = ord(ch)
    index=ascii_val-97
    print(hash_list[index])