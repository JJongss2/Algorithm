def power(a,n):
  return a**n


# 비재귀 O(n)
def power(a,n):
  x = 1
  for _ in range(n):
    x = x*a
  return x


# 선형재귀 T(n) = T(n-1) + C = O(n) 
def power(a,n):             # a^(n-1) * a
  if n == 1: return a
  return power(a,n-1) * a


# 선형재귀 n/2개씩 쪼갬  / T(n) = T(n/2) + C = C * log n = O(log n)
def power(a,n):        
  if n == 0: return 1
  elf n == 1 : return a
  else: 
    x = power(a, n//2)
    if n%2 == 0:
      return x*x
    else: return x*x*a

# 이중재귀 T(n) = 2*T(n/2) + C
def power(a,n):
  if n==0: return 1
  if n%2==1: return power(a,n//2) * power(a, n//2) * a
  else: return power(a,n//2) * power(a, n//2)
