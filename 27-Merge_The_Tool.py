def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string), k):
        chunk = string[i:i+k]

        seen = set()
        result = "" # building the string order
        for char in chunk:
            if char not in seen:
                seen.add(char)
                result += char # add to string while building 
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)