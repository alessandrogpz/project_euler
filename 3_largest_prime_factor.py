# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_it_prime(n):
    """Returns 'True' if 'n' prime, 'False' otherwise"""
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    if n == 1 or n <= 0:
        return False

    for i in range (2, n//2):
        if n % i == 0:
            return False
    return True

def prime_factor_finder(n):

    for i in range(2, n):
        if n % i == 0:
            n = n / i 
        if n == 1:
            break
    return i

print(prime_factor_finder(600851475143))

# --------------------------------------------
# Full list of prime divisors

def max_prime_divisor(number):
    res_list = []
    while number != 1:
        divisor = 2
        while number % divisor != 0:
            divisor += 1
        res_list.append(divisor)
        number /= divisor

    return res_list

print(max_prime_divisor(600851475143))