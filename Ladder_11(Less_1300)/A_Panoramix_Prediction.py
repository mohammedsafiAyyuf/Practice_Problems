import math
def isPrime(x):
	for i in range(2,round(math.sqrt(x))+1):
		if x%i==0:
			return(False)
	return(True)

n,m=list(map(int,input().split()))
for i in range(n+1,m+1):
	if isPrime(i):
		if i==m:
			print("YES")
		else:
			print("NO")
		break
else:
	print("NO")