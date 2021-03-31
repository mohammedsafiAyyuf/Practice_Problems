k=int(input())
flowers=list(map(int,input().split()))
flowers.sort(reverse=True)
count=0
for i in flowers:
	if k<=0:
		break
	count+=1
	k-=i
print(count if k<=0 else -1)
