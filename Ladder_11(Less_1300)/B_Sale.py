n,m=list(map(int,input().split()))
array=list(map(int,input().split()))
array.sort()
profit=0
for i in range(m):
	if array[i]>0:
		break
	profit+=array[i]

print(-1*profit)