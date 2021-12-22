import numpy as np
from math import log

print('What is it you want? \n'
      '1 - addition \n'
      '2 - subtraction \n'
      '3 - multiplication \n'
      '4 - raise to the power \n'
      '5 - extract root \n'
      '6 - extract logarithm\n')
answer = int(input('What is it you want? '))


# create any number of input lists
all_lsts = []
i = 0
while True:
    print('Do you need more input lists?')
    reply = input('y/n: ')
    if reply == 'n':
        break
    elif reply == 'y':
        def additional_lists():
            print('Define values for the', i, 'list (positive numbers only, separated by commas)')
            val_to_l = input('numbers: ')
            all_lsts.append([float(value) for value in val_to_l.split(', ')])
        i = i + 1
        additional_lists()

# find longest list
def maxlen(all_lsts):
    maxlist = max(x for x in all_lsts)
    maxlength = max(len(j) for j in all_lsts)
    return maxlist, maxlength

# how long the longest list is + convert tuple to integer
tolen = maxlen(all_lsts)[1:]
n = int(''.join(map(str, tolen)))

# extend all lists to max length

for k in range(0, i):
    if len(all_lsts[k]) < n:
        if answer == 1 or answer == 2:
            all_lsts[k].extend([0] * n)
        else:
            all_lsts[k].extend([1] * n)
        all_lsts[k] = all_lsts[k][:n]

for g in range(0, i):
    all_lsts[g] = np.array(all_lsts[g])


if answer == 1:
    def addition(all_lsts):
        res = [sum(x) for x in zip(*all_lsts)]
        return res
    print(addition(all_lsts))
elif answer == 2:
    def subtraction(all_lsts):
        z, w = all_lsts[0], all_lsts[1]
        res = z - w
        for f in range(2, i):
            z = res
            w = all_lsts[f]
            res = z - w
        return res
    print(subtraction(all_lsts))
elif answer == 3:
    def multiplication(all_lsts):
        z, w = all_lsts[0], all_lsts[1]
        res = z * w
        for f in range(2, i):
            z = res
            w = all_lsts[f]
            res = z * w
        return res
    print(multiplication(all_lsts))
elif answer == 4:
    def power(all_lsts):
        z, w = all_lsts[0], all_lsts[1]
        res = z ** w
        for f in range(2, i):
            z = res
            w = all_lsts[f]
            res = z ** w
        return res
    print(power(all_lsts))
elif answer == 5:
    def root(all_lsts):
        z, w = all_lsts[0], all_lsts[1]
        d = [1] * len(z)
        res = z ** (d / w)
        for f in range(2, i):
            z = res
            w = all_lsts[f]
            res = z ** (d / w)
        return res
    print(root(all_lsts))
elif answer == 6:
    def logarithm(all_lsts):
        for s in range(0, 2):
            z, w = all_lsts[0], all_lsts[1]
            res = [log(y, z[s]) for y in w]
            for f in range(2, i):
                z = res
                w = all_lsts[f]
                res = [log(y, z[f]) for y in w]
            return res
    print(logarithm(all_lsts))


