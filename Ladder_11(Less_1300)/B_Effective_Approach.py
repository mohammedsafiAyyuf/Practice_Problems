from collections import defaultdict
n=int(input())
array=list(map(int,input().split()))
hashTable=defaultdict(list)
for idx,val in enumerate(array):
	hashTable[val]=[idx+1,n-idx]

input()
query=list(map(int,input().split()))

leftComp=0
rightComp=0
for i in query:
	temp=hashTable[i]
	leftComp+=temp[0]
	rightComp+=temp[1]

print(leftComp,rightComp)

