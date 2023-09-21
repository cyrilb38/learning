import sys

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return a[left:right], number_of_inversions
    ave = (left + right) // 2

    left_part, n_inversion_left = get_number_of_inversions(a, left, ave)
    right_part, n_inversion_right = get_number_of_inversions(a, ave, right)

    number_of_inversions += n_inversion_left + n_inversion_right

    ordered = []
    while left_part or right_part:
        if not left_part :
            ordered += right_part
            right_part = []
        elif not right_part:
            ordered += left_part
            left_part = []
        elif left_part[0] <= right_part[0]:
            ordered.append(left_part.pop(0))
        else:
            ordered.append(right_part.pop(0))
            number_of_inversions += len(left_part)

    return ordered, number_of_inversions

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    _, res = get_number_of_inversions(a, 0, len(a))
    print(res)
