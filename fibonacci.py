cube = lambda x: x*x*x, fib_list# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    prev = 0
    cur = 1 
    fib_list = [] 
    for i in range(n):
        fib_list.append(prev)
        prev, cur = cur, prev + cur
        print(cube)
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))