# 재귀 T(n) = T(n/2) + C = O(log n)

def bs(A,l,r,k): # A[l], ..., A[r]에서 탐색
  if l > r : return -1
  m = (l+r)//2
  if A[m] < k: return bs(A, l, m-1, k)
  elif A[m] < k : return bs(A,m+1,r, k)
  else: return m


  
# 비재귀
def bs(A,k):
  l, r = 0, len(A)-1
  while l <= r:
    m = (l+r)//2
    if A[m]>k:
      r = m-1
    elif A[m]<k:
      l = m+1
    else:
      return m
  return -1
