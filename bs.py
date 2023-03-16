def binary_search(lst, target):

    left_index = 0
    right_index = len(lst) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if lst[mid_index] > target:
            right_index = mid_index - 1

        elif lst[mid_index] < target:
            left_index = mid_index + 1
        else:
            return 'Element is found at index ' + str(mid_index)
    return 'Element does not exist!'


lst = list(range(1, 100))
target = 77
bs = binary_search(lst, target)
print(bs)
