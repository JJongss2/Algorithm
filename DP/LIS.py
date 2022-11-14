def LIS_DP(seq):
    dp = [1 for _ in range(len(seq))]
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i]>seq[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return dp[-1]

seq = input()
lis = LIS_DP(seq)
print(lis)
