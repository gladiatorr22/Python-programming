def isprime(n):
    i=1
    while i*i<= n:
        if n % i == 0:
            return False
        i += 1
    return True

def first_n_primes(n):
    primes = []
    i=1
    while i <= n:
        if isprime(i)== True:
            primes.append(i)
    return primes

n = int(input("Enter a number: "))
print(first_n_primes(n))
