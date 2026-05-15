def print_formatted(number):
    if 1 <= number <= 99:
        x = 1
        if 1 <= number <= 99:
            while x <= number:
                d = number
                o = oct(x)
                X = hex(x)
                b = bin(x)
                width = len(bin(number)) - 2  # -2 to strip the '0b' prefix
                txt = f"{x:{width}d} {x:{width}o} {x:{width}X} {x:{width}b}"
                print(txt)
                x += 1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)