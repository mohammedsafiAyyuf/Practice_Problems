def checker(i,j,ans):
	can_place_one=True
	if i-1<0 and j-1<0:
		return(1)

	if i-1>=0:
		if ans[i-1][j]==1:
			can_place_one=False

	if j-1>=0:
		if ans[i][j-1]==1:
			can_place_one=False

	if can_place_one:
		return(1)
	else:
		return(0)

n,m=list(map(int,input().split()))
boad=[]
for i in range(n):
	boad.append(input())
ans=[["-" for j in range(m)] for i in range(n)]

for i in range(n):
	for j in range(m):
		if boad[i][j]==".":
			if i%2==0:
				if j%2==0:
					ans[i][j]="W"
				else:
					ans[i][j]="B"
			else:
				if j%2!=0:
					ans[i][j]="W"
				else:
					ans[i][j]="B"

		#if boad[i][j]==".":
		#	ans[i][j]=checker(i,j,ans)
		#print(ans)
#for i in range(n):
#	for j in range(m):
#		if ans[i][j]==1:
#			ans[i][j]="B"
#		elif ans[i][j]==0:
#			ans[i][j]="W"

[print(i) for i in ["".join(i) for i in ans]]
