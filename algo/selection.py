
def sel(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]
    return arr


print(sel([8, 3, 1, 29, 0, 5]))
