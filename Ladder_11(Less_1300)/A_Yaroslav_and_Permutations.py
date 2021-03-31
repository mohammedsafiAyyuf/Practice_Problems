from collections import defaultdict
from math import ceil
n=int(input())
array=list(map(int,input().split()))
HashTable=defaultdict(int)
for i in array:
	HashTable[i]+=1

maxVal=max(HashTable.values())
if ceil(n/2)>=maxVal:
	print("YES")
else:
	print("NO")