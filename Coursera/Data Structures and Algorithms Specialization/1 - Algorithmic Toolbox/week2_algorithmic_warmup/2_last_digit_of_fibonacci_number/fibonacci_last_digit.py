# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else :
        fib_list = [1, 1]
        for x in range(2, n):
            fib_list.append(fib_list[x-1] % 10 + fib_list[x-2] %10)
    return fib_list[-1] % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
