a,b=list(map(int,input().split()))
count=0
while True:
	count+=1
	a*=3
	b*=2

	if a>b:
		break
print(count)