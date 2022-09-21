# reverse (A = A[::-1])


# reverse1
# T(n) = T(n-1) + C = O(n)
def reverse(A):
  if len(A)==1:
    return A
  return reverse(A[1:]) + A[0]


# reverse2
# T(n) = T(n-2) + C = T(n-4) + C + C = T(1) + c*n/2 = O(n)
def reverse2(A,start,stop):
  if start+1<stop:
    A[start],A[stop-1] = A[stop-1], A[start]
    reverse(A,start+1, stop-1)

