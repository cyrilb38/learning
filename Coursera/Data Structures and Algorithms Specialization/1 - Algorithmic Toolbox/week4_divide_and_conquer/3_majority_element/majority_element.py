# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    mid = left + (right - left) // 2
    maj_element_left = get_majority_element(a, left, mid - 1)
    maj_element_right = get_majority_element(a, mid, right)
    # if the 2 majority elements are the same, the majority element is easily found
    if (maj_element_left == maj_element_right):
        return maj_element_left
    else:
        # we go through the lists to see if it is still a majority element
        concat_list = a[left:mid] + a[mid:right+1]
        maj_element = [el for el in [maj_element_left, maj_element_right] if el != -1]
        for maj_element_to_check in maj_element:
            count = 0
            for el in concat_list:
                if el == maj_element_to_check:
                    count += 1
            if count > (len(concat_list) / 2):
                return maj_element_to_check
        return -1

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
