n,k=list(map(int,input().split()))
n=str(n)
for i in range(k):
	if int(n[-1])>0:
		n=n[:-1]+str(int(n[-1])-1)
	else:
		n=n[:-1]
	#print(n)
print(n)
