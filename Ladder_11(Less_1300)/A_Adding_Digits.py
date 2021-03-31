a,b,n=list(map(int,input().split()))
flag=0
a=str(a)
for j in range(10):
	temp=str(a)+str(j)
	if int(temp)%b==0:
		a=temp
		break
else:
	flag=1

if flag:
	print(-1)
else:
	print(a+"0"*(n-1))