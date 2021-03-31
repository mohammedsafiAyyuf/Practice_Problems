y,k,n=list(map(int,input().split()))
ans=[]
x=k-(y%k)

if x+y<=n:
	while x+y<=n:
		ans.append(x)
		x+=k
	print(*ans)
else:
	print(-1)
