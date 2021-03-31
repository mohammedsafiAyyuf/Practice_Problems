n,m,d=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
change=matrix[0][0]%d
flag=0
count=0
for i in range(n):
	for j in range(m):
		if change!=matrix[i][j]%d:
			flag=1
			break

if flag:
	print(-1)
else:
	matrixArray=[]
	for i in matrix:
		matrixArray+=i
	matrixArray.sort()
	median=matrixArray[(n*m//2)]
	for i in matrixArray:
		if i<median:
			count+=(median-i)//d
		else:
			count+=(i-median)//d

	print(count)
