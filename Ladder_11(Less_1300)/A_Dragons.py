s,n=list(map(int,input().split()))
dragon=[]
for i in range(n):
	dragon.append(list(map(int,input().split())))
dragon.sort()
for i in dragon:
	if i[0]>=s:
		print("NO")
		break
	s+=i[1]
else:
	print("YES")