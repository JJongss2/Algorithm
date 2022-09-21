# T(n) = sum(n)을 계산하는 시간
# T(1) = C
# T(n) = T(n-1)+C = T(n-2)+C+C = T(1) + C(n-1) = C+ C(n-1) = C*n = O(n)
def sum(n):
  if n == 1:
    return 1
  return sum(n-1)+n



# T(n) = 2*T(n/2) + C, T(1) = C
#      = 2*(2*T(n/2^2 + C) + C = 2^2*T(n/2^2) + C(2+1)     / n=2^k일때 깔끔히 떨어짐, 2^(k-1) < n <= 2^k
#      = C(1+2+....+2^k) = C((2^(k+1)-1)/(2-1)) =  c*2^(k+1) - C = 2*C*n- C = O(n)
def sum(a,b):
  if a == b :
    return a
  m = (a+b)//2
  return sum(a,m) + sum(m+1,b)    # T(n/2)+ T(n/2)
