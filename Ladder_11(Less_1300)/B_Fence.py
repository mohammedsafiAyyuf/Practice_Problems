n,k=list(map(int,input().split()))
array=list(map(int,input().split()))
minIdx=0
minVal=sum(array[:k])
curVal=minVal
idx=0
for i in range(k,n):
	curVal-=array[idx]
	curVal+=array[i]
	idx+=1
	if curVal<minVal:
		minVal=curVal
		minIdx=idx
	#print(minIdx,minVal,curVal,idx,i)
print(minIdx+1)
