import math
num = int(input('number : '))
if num < 3:
    print('Nothing to factorize')
elif num > 3:
    def factorize(n):
        while n % 2 == 0:
            print(2),
            n = n / 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                print(i),
                n = n / i
        if n > 2:
            print(n)
    n = num
    factorize(n)
