x=int(input())
moves=0
for i in [5,4,3,2,1]:
	moves+=x//i
	x=x%i
print(moves)