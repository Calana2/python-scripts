def primefact(n):
    # division by test
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor 
            print(n)
        divisor += 1
    return factors

#print(primefact(2342343253463454))

