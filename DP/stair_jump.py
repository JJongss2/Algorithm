# 1, 2 계단만 오를 수 있을 떄
def jump(n):
    a = [0]*(n+1)
    a[1] = 0  # 1층부터 시작
    a[2] = 1
    a[3] = 2
    if n <= 3:
        return a[n]
    else:
        for i in range(4, n+1):
            a[i] = a[i-1] + a[i-2]
    print(a)
    return a[n]
n = int(input())
print(jump(n))


# 1, 3 계단만 오를 수 있을 떄
def jump(n):
    a = [0]*(n+1)
    a[1] = 0  # 1층부터 시작
    a[2] = 1
    a[3] = 1
    a[4] = 2
    if n <= 4:
        return a[n]
    else:
        for i in range(5, n+1):
            a[i] = a[i-1] + a[i-3]

    print(a)
    return a[n]
n = int(input())
print(jump(n))
