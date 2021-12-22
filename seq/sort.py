from seq import DNA, RNA, Protein, Sequence
from randomseq import create_dna_fixed
from random import randint


length = int(input('Input sequence length: '))
REFERENCE = Sequence(1, create_dna_fixed(length))
seq_group = [DNA(randint(2, 100), create_dna_fixed(length)) for i in range(10)]
print(REFERENCE)


def find_difference(element):
    count = 0
    for first, second in zip(REFERENCE, element):
        if first != second:
            count += 1
    return count


for item in seq_group:
    print(REFERENCE, item, find_difference(item))


def insertionSort(arr, function_sort):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and function_sort(key) < function_sort(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(seq_group, find_difference)
print(*seq_group)

