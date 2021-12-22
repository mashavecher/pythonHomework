from collections import Counter


def stat(letters):
    def count_letters(sequence):
        return dict(Counter(sequence))
    return count_letters


