n=int(input())
if n%2==1:
	print(-1)
else:
	arr=[i for i in range(1,n+1)]
	for idx in range(0,n-1,2):
		arr[idx],arr[idx+1]=arr[idx+1],arr[idx]
	[print(i,end=" ") for i in arr]