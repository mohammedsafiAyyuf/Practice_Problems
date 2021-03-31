n=int(input())
array=list(map(int,input().split()))
hashTable={}
for idx,val in enumerate(array,1):
	hashTable[val]=idx
for i in sorted(hashTable.keys()):
	print(hashTable[i],end=" ")




