def max_pairwise_product(numbers):
    n = len(numbers)
    max_1 = {"val" : 0, "index" : 0}
    max_2 = {"val" : 0, "index" : 0}

    for i in range(n):
        if numbers[i] >= max_1['val']:
            max_2["val"] = max_1['val']
            max_2["index"] = max_2["index"]
            
            max_1['val'] = numbers[i]
            max_1['index'] = i
        elif numbers[i] >= max_2['val']:
            max_2["val"] = numbers[i]
            max_2["index"] = i

    return max_1["val"] * max_2["val"]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
