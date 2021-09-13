

def bub(arr):
    for i in range(len(arr), 0, -1):
        swapped = False
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(bub([8, 1, 5, 6, 2, 0, 28, 11]))

import os
print(os.getcwd())
