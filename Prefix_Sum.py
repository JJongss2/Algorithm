# O(n^2)

A = [int(x) for x in input().split()]
p = []
for x in A:
	if not p:
		p.append(A[0])
	else:
		p.append(p[-1]+x)
max = -99999999999
for i in range(len(A)):
	for j in range(i, len(A)):
		if i == 0 :
			if max<p[j]:
				max = p[j]
		else:
			if max < (p[j] - p[i-1]):
				max = p[j]-p[i-1]
print(max)
