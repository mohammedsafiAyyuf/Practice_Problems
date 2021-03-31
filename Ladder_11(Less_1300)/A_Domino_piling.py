a,b=list(map(int,input().split()))
temp=a//2
ans=b*temp
if a%2!=0:
	ans+=b//2
print(ans)