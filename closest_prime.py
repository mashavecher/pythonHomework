import math
num = int(input('number : '))
if num < 2:
    print('there are no prime numbers smaller than two')
elif num == 2:
    print('two is the smallest prime number')
elif num > 2:
    primes = []
    primes.insert(0, 2)
    def sundaram():
        nm = int(math.sqrt(num))
        marked = [0] * (int(num / 2 + 500))
        for i in range(1, int((nm - 1) / 2) + 1):
            for j in range(((i * (i + 1)) << 1),
                           (int(num / 2) + 1), (2 * i + 1)):
                marked[j] = 1
        for i in range(1, int(num / 2) + 1):
            if marked[i] == 0:
                primes.append(2 * i + 1)
    def search(left, right, n):
        n = num
        if left <= right:
            mid = int((left + right) / 2)
            if primes[mid] == num:
                return primes[mid - 1]
            if mid == 0 or mid == len(primes) - 1:
                return primes[mid]
            if primes[mid] < n and primes[mid + 1] > n:
                return primes[mid]
            if n < primes[mid]:
                return search(left, mid - 1, n)
            else:
                return search(mid + 1, right, n)
        return 0
    sundaram()
    print(search(0, len(primes) - 1, num))
