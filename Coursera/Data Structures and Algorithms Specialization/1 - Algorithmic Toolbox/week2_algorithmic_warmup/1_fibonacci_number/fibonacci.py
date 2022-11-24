# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    else :
        fib_list = [1, 1]
        for x in range(2, n):
            fib_list.append(fib_list[x-1] + fib_list[x-2])
    return fib_list[-1]

n = int(input())
print(calc_fib(n))
