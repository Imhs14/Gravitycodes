def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    a = list(sentence.swapcase().split())
    s = a[::-1]
    return " ".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
