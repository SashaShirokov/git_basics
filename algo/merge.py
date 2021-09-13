def merge(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    med = len(arr) // 2
    left = merge_sort(arr[:med])
    right = merge_sort(arr[med:])
    return merge(left, right)


print(merge_sort([8, 1, 11, 9, 5, 7]))
