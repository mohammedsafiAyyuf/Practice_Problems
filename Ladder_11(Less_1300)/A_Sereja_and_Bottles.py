from collections import defaultdict
n=int(input())
isOpened=defaultdict(bool)
count=defaultdict(int)
whoCanWe=defaultdict(list)
for _ in range(n):
	a,b=list(map(int,input().split()))
	count[a]+=1
	isOpened[a]=False#[opened? , total , who can we open?]
	whoCanWe[a].append(b)
opend=0
flag=0
for i in whoCanWe:
	for j in whoCanWe[i]:
		if i!=j:
			if count[j]:
				opend+=count[j]
				count[j]=0
				isOpened[j]=True
		elif i==j and count[i]>1:
			opend+=count[j]-1
			count[j]=1
			flag=1

		elif i==j and count[i]==1:
			if flag==1:
				flag=0
				count[j]=0
				opend+=1


print(n-opend)




