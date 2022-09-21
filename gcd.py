def gcd_sub(a,b):
  while a!=0 and b!=0:  # 두 수 중 하나가 0이 되기 전까지 빼기 연산 반복
    if a>b: a = a-b
    else: b = b-a
  return a + b


def gcd_mod(a,b):       # 큰 수가 작은 수보다 작을 때까지 작은 수만큼을 줄이게 된다는 것은
                        # 결국 큰수를 작은 수로 나머지를 구하는 과정과 같다.
  while a!=0 and b!=0:
    if a>b: a = a%b
    else: b = b%a
  return a + b
  
  
def gcd_rec(a,b):
  if a == 0 or b == 0:
    return a + b
  elif a>b: return gcd(a%b,b)
  else: return gcd(b%a,a)      # gcd_rec(a%b, b) = gcd_rec(b, a%b)
