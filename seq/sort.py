import seq



a = ['hfdf', 'fdsfd', 'fds', 'f', 'refds', 'fd']

def fing_ref(s):
    return len(s)


def insertionSort(arr, function_sort):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and function_sort(key) < function_sort(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSort(a, fing_ref)
print(a)