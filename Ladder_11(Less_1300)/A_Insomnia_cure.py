arr=[]
for _ in range(4):
	arr.append(int(input()))
totalDrag=int(input())
hashset=[True for i in range(1,totalDrag+1)]
for i in arr:
	for idx,value in enumerate(hashset,1):
		if idx%i==0:
			hashset[idx-1]=False
count=0
for i in hashset:
	if i==False:
		count+=1
print(count)