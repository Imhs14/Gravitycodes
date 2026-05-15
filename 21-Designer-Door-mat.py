def designer(N, M):
    rows = [('.|.' * (2*i + 1)).center(M, '-') for i in range(N // 2)]
    print('\n'.join(rows + ['WELCOME'.center(M, '-')] + rows[::-1])) # rows  +  [middle]  +  rows[::-1]
#                                                                       ↓           ↓            ↓
#                                                                       top half + welcome + bottom half  →  joined by \n  →  printed

if __name__ == '__main__':
    N, M = map(int, input("").split())
    if (5 < N < 101 and 15 < M < 303) and (N % 2 != 0) and (M == N * 3):
            designer(N, M)