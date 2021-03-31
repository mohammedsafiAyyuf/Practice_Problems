n=int(input())
leftOne=0

rightOne=0
for i in range(n):
	left,right=list(map(int,input().split()))
	if left==1:
		leftOne+=1
	if right==1:
		rightOne+=1
work=0
if n-leftOne>leftOne:
	work+=leftOne
else:
	work+=n-leftOne

if n-rightOne>rightOne:
	work+=rightOne
else:
	work+=n-rightOne
print(work)
