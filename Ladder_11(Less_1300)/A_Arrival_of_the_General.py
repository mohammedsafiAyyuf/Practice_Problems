n=int(input())
array=list(map(int,input().split()))
maxNum=max(array)
minNum=min(array)
maxIdx=None
minIdx=None
time=0
for idx in range(n):
	if array[idx]==maxNum:
		time+=idx
		maxIdx=idx
		break
#print(time)

for idx,val in enumerate(array[::-1]):
	if val==minNum:
		time+=idx
		minIdx=n-idx-1
		break
#print(time,minIdx,maxIdx)
if minIdx<maxIdx:
	time-=1
print(time)