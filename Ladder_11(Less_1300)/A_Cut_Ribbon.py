import sys
sys.setrecursionlimit(100000)
from functools import lru_cache
#overMax=-float('inf')
hashTable={}
def ribbonCutting(n,array,idx,split):
	global hashTable
	if n in hashTable:
		return(hashTable[n])
	if n==0:
		return(split)

	With,WithOut=0,0
	ans=0
	for i in range(idx,len(array)):
		if array[i]<=n:
			With=ribbonCutting(n-array[i],array,i,split+1)
		WithOut=ribbonCutting(n,array,i+1,split)
		#print(With,WithOut,n,idx)
		ans=max(With,WithOut,ans)
	hashTable[n]=ans
	return(ans)

n,a,b,c=list(map(int,input().split()))
array=tuple(sorted([a,b,c]))
print(ribbonCutting(n,array,0,0))
#print(overMax-1 if overMax>1 else 1)

