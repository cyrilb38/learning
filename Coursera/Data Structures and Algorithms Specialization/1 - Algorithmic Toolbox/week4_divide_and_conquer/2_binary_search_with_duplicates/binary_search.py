def binary_search(keys, query):
    # write your code here
    left, right = 0, len(keys) - 1
    res = -1
    while left <= right:
        mid_index = left + (right - left) // 2
        if keys[mid_index] == query:
            res = mid_index
            right = mid_index - 1
        elif query < keys[mid_index]:
            right = mid_index - 1
        else :
            left = mid_index + 1
    
    return res


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
