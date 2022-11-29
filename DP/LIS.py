def LIS_DP(seq):
    dp = [1 for _ in range(len(seq))]
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i]>seq[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

seq = input()
lis = LIS_DP(seq)
print(lis)

'''
def LIS_DP(seq):
	LIS = [1]*len(seq)
	for i in range(1,len(seq)):
		LIS[i] = 1
		for j in range(i-1, -1 ,-1):
			if seq[j] < seq[i]:
				LIS[i] = max(LIS[i], LIS[j]+1)
	return max(LIS)

seq = input()
lis = LIS_DP(seq)
print(lis)
'''
