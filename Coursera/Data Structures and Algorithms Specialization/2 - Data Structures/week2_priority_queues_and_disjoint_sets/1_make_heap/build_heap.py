# python3


def bubble_down(data, indice):
    indice_min = None
    if (indice * 2 + 2) < len(data) :
        indice_min = (indice * 2 + 1) if (data[(indice * 2) + 1] < data[(indice * 2) + 2]) else (indice * 2 + 2)
    elif (indice * 2 + 1) < len(data) :
        indice_min = (indice * 2 + 1)

    if indice_min is not None and data[indice_min] < data[indice]:     
        swap = [(indice, indice_min)]
        data[indice], data[indice_min] = data[indice_min], data[indice]
        swap += bubble_down(data, indice_min)
    else :
        return []
    
    return swap

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)//2, -1, -1):
        swaps += bubble_down(data, i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
