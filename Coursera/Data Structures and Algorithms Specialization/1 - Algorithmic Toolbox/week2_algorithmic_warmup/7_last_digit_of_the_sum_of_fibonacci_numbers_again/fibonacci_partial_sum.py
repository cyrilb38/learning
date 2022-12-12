# Uses python3
import sys

def calc_fib(n):
    if n <= 1:
        return n
    else :
        fib_list = [1, 1]
        for x in range(2, n):
            fib_list.append(fib_list[x-1] + fib_list[x-2])
    return fib_list[-1]


def pisano_length(m) :
    a,b = 0,1
    for i in range((m*m)+1):
        a,b = b,(a+b)%m
        if a==0 and b==1:
            return i+1

def get_fibonacci_huge_naive(n, m):
    pisano_l = pisano_length(m)
    return calc_fib(n % pisano_l) % m

def fibonacci_partial_sum_naive(from_, to):
    return (get_fibonacci_huge_naive(to+2 ,10) - get_fibonacci_huge_naive(from_+1 ,10)) % 10 


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
