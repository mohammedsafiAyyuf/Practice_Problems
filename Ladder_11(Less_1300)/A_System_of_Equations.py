def check(a,b,n,m):
	if a**2+b==n and a+b**2==m:
		return(1)
	else:
		return(0)

n,m=list(map(int,input().split()))
ans=0
for a in range(100,-1,-1):
	if a**2<=n:
		#print(a)
		ans+=check(a,n-a**2,n,m)
print(ans)