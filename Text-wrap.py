import textwrap

def wrap(string, max_width):
    if len(string) < 1000 and max_width < len(string):
        wrapper = textwrap.fill(string, width = max_width)
        return wrapper
    return wrap

if __name__ == '__main__':
    string, max_width = input() , int(input())
    result = wrap(string,max_width)
    print(result)