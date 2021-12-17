import math
num = int(input('number : '))
if num < 2:
    print('the task is to make fibonacci out of primes, and there are no prime numbers smaller than two')
elif num >= 2:
    primes = []
    primes.insert(0, 2)
    def sundaram():
        nm = int(math.sqrt(num))
        marked = [0] * (int(num / 2 + 500))
        for i in range(1, int((nm - 1) / 2) + 1):
            for j in range(((i * (i + 1)) << 1),        #https://en.wikipedia.org/wiki/Bitwise_operation
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
                return primes[mid - 1], primes[mid - 2]
            if mid == 0 or mid == len(primes) - 1:
                return primes[mid], primes[mid - 1]
            if primes[mid] < n and primes[mid + 1] > n:
                return primes[mid], primes[mid - 1]
            if n < primes[mid]:
                return search(left, mid - 1, n)
            else:
                return search(mid + 1, right, n)
        return 0
    sundaram()
    fibobase = (search(0, len(primes) - 1, num))
    ltwo = (3, 2)
    if fibobase == ltwo:
        fib1 = 2
        fib2 = 2
    else:
        fib1 = fibobase[0]
        fib2 = fibobase[1]
    fibseq = [fib1, fib2]
    i = 0
    k = 1
    while len(fibseq) < 17:
        def fibonacci(n, nm):
            n = fibseq[i]
            nm = fibseq[k]
            fibn = n + nm
            fibseq.append(fibn)
        fibonacci(fib1, fib2)
        i = i + 1
        k = k + 1
        z = 2
    print(fibseq[z:])
