n=int(input())
array=list(map(int,input().split()))
idx=0
while n>0:
	if array[idx]>=n:
		print(idx+1)
		break
	n-=array[idx]
	idx+=1
	if idx==7:
		idx=0
