from collections import defaultdict
n,k=list(map(int,input().split()))
hashTable=defaultdict(int)
for i in input():
	hashTable[i]+=1
data=sorted(hashTable.values(),reverse=True)
ans=[]
idx=0
while k:
	if k>=data[idx]:
		ans.append(data[idx])
		k-=data[idx]
	else:
		ans.append(k)
		k=0
	idx+=1
result=0
#print(ans)
#print(data)
for i in ans:
	result+=(i*i)
print(result)

