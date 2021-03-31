import math
n,k=list(map(int,input().split()))
if k<=math.ceil(n/2):
	print(k+k-1)
else:
	print((k-math.ceil(n/2))*2)