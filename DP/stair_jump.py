# 1, 3 계단만 오를 시
def jump(n):
    A = [0]*(n+1)
    A[0] = 1
    A[1] = 1
    A[2] = 2

    if n <= 3:
        return A[n-1]

    for i in range(3, n):
        A[i] = A[i-1] + A[i-3]

    return A[n-1]

n = int(input())
print(jump(n))
