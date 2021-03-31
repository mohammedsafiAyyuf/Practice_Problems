count=0
for _ in range(int(input())):
	if list(map(int,input().split())).count(1)>=2:
		count+=1
print(count)