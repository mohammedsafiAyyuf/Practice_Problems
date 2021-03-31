n,m=list(map(int,input().split()))
array=list(map(int,input().split()))
array.sort()
start=0
ans=array[n-1]-array[0]
for i in range(n-1,m):
	ans=min(ans,array[i]-array[start])
	start+=1
print(ans)