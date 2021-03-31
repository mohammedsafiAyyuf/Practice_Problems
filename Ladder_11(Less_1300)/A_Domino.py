upOdd=0
downOdd=0
odd=0
n=int(input())
for _ in range(n):
	a,b=list(map(int,input().split()))
	a=(a%2==0)
	b=(b%2==0)
	if not a and b:
		upOdd+=1
	elif not b and a:
		downOdd+=1
	elif not a and not b:
		odd+=1

if odd%2!=0:
	if upOdd%2!=0 and downOdd%2!=0:
		print(0)
	elif upOdd%2==0 and downOdd%2==0 and (upOdd>0 or downOdd>0):
		print(1)
	else:
		print(-1)	
elif upOdd%2==0 and downOdd%2==0:
	print(0)
elif  upOdd%2!=0 and downOdd%2!=0:
	print(1)
else:
	print(-1)