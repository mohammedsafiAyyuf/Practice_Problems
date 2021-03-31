n=int(input())
apple=list(map(int,input().split()))
one=0
two=0
for i in apple:
	if i==100:
		one+=1
	else:
		two+=1

if one%2==1:
	print("NO")
elif one==0 and two%2==1:
	print("NO")
else:
	print("YES")


