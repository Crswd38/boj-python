import math

def solution(numer1, denom1, numer2, denom2):
    denom = (denom1 * denom2) // math.gcd(denom1, denom2)
    numer = int(numer1 * denom / denom1 + numer2 * denom / denom2)

    g = math.gcd(denom, numer)

    numer //= g
    denom //= g

    return [numer, denom]

print(solution(9, 2, 1, 3))