n,k=list(map(int,input().split()))
array=list(map(int,input().split()))
if len(set(array[k-1:]))==1:
	count=0
	for i in range(k-1,-1,-1):
		if array[k-1]==array[i]:
			count+=1
		else:
			break
	print(k-count)
else:
	print(-1)