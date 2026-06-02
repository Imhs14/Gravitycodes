string ='AABCAAADA'
k = 3
mset= set()
for i in range(0, len(string), k):
    chunk = string[i:i+k]
    print(f"chunk:{chunk}")

    mset = set()
    for char in chunk:
        if char not in mset:
            mset.add(char)
    print(f"Result: {''.join(mset)}")
