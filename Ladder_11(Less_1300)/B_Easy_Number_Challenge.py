from functools import lru_cache
from math import sqrt,ceil
@lru_cache(None)
def countDevisor(n):
	count=0
	for i in range(int(sqrt(n))):
		if n%(i+1)==0:
			if n/(i+1)==(i+1):
				count+=1
			else:
				count+=2
	return(count)


a,b,c=list(map(int,input().split()))
modulo=2**30
ans=0
for i in range(1,a+1):
	for j in range(1,b+1):
		for k in range(1,c+1):
			ans+=countDevisor(i*j*k)
			#print(i*j*k,countDevisor(i*j*k))
print(ans%modulo)