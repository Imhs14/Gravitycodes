from itertools import product

def product_itertool(A, B):
    combinations = product(A, B)
    b = list(combinations)
    str_comb = [str(c) for c in b ]
    return " ".join(str_comb)

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(product_itertool(a, b))

''' 
i/p : 
1 2
3 4
o/p : (1, 3) (1, 4) (2, 3) (2, 4)'''