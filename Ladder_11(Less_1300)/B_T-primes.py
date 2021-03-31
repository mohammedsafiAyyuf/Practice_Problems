import math

def primeSeive():
	n=10**6+2
	array=[True for i in range(n)]
	array[0]=False
	array[1]=False
	idx=2
	while idx**2<n:
		if array[idx]:
			for i in range(idx*2,n,idx):
				array[i]=False
		idx+=1
	#print(array)
	return(array)

sieve=primeSeive()
n=int(input())
array=list(map(int,input().split()))
for i in array:
	x=math.sqrt(i)
	if x==int(x) and sieve[int(x)]:
		print("YES")
	else:
		print("NO")