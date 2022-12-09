def gcd(a, b): # 크기 고려 안해도됨
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(9, 18))
