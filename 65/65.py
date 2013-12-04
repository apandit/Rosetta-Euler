#!/usr/bin/python

import math

# Prime sieve code I got off stackoverflow
def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

# Reduce fraction using sieve
def ReduceFraction( sieve, frac ):
    upper = frac[0]
    lower = frac[1]
    for p in sieve:
        # We use floor of sqrt(lower) since lower will always be smaller than upper
        while upper % p == 0 and lower % p == 0 and math.floor(math.sqrt(lower)) > p:
            upper = upper / p
            lower = lower / p
    return (upper, lower)

# Convert whole + num/den into an improper fraction
# den is a fraction tuple
def Calculate( whole, num, den ):
    tmpTop = num * den[1]
    tmpDen = den[0]

    tmpAdd = whole * tmpDen
    tmpNum = tmpAdd + tmpTop
    
    return (tmpNum, tmpDen)

# Using the pattern: (1, 2, 1, 1, 4, 1, ... 1, 2k, 1...)
def GenerateLower( index ):
    if index % 3 == 2:
        return (index / 3) * 2 + 2
    else:
        return 1

# First denominator is the final term denominator over 1
# Then, just calculate using denominator, reduce the fraction and repeat
# Have to do the final one with the startingWhole number so xrange stops at 1 from term
def SolveFor( primes, startingWhole, termToConvergeOn ):
    den = (GenerateLower(termToConvergeOn), 1)
    for term in xrange(termToConvergeOn, 1, -1):
        den = Calculate( GenerateLower(term - 1), 1, den )
        den = ReduceFraction( primes, den )

    den = Calculate( startingWhole, 1, den )
    return den

# Simple modulo + division accumulator
def SumDigits(number):
    acc = 0
    while number > 0:
        acc = acc + number % 10
        number = number / 10
    return acc

# Use sieve to primes less than 1 million (might not even need that high)
primes = sieve_for_primes_to(1000000)

# Get the reduced fraction for this iteration
# Thank god for infinite precision integers in python
numDenPair = SolveFor(primes, 2, 99)
print( numDenPair )

# Print the sum of the digits
print( "Sum is " + `SumDigits(numDenPair[0])` )
