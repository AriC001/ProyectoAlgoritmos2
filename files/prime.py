def isPrime(n):

    if n < 2:
        return False

    if n < 4:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**(1/2))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True


def nextPrime(n):

    prime = n+1

    while not isPrime(prime):
        prime += 1

    return prime


def prevPrime(n):

    prime = n-1

    while not isPrime(prime):
        prime -= 1

    return prime
