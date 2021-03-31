from collections import defaultdict

def validate(sequence):
	a=sequence[0]
	d=sequence[1]-a
	for i in range(2,len(sequence)):
		if sequence[i]!=a+i*d:
			return(None,None)
	return(a,d)

n=int(input())
array=[int(i) for i in input().split()]
HashTable=defaultdict(list)
for idx,val in enumerate(array):
	HashTable[val].append(idx+1)

ans=[]
for i in HashTable.keys():
	if len(HashTable[i])==1:
		ans.append([i,0])
		continue
	a,d=validate(HashTable[i])
	if a!=None:
		ans.append([i,d])

ans.sort()
print(len(ans))
for i in ans:
	print(i[0],i[1])
