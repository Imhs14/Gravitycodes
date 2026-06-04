def average(array):
    # your code goes here
    my_set = set(array)
    n = len(my_set)
    avg = float((sum(my_set))/n)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)