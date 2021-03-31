
count=0
for _ in range(int(input())):
	a,b=list(map(int,input().split()))
	if a+2<=b:
		count+=1
print(count)