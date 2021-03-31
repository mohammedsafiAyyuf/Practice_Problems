matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))

found=None
for i in range(5):
	for j in range(5):
		if matrix[i][j]==1:
			found=(i,j)
			break
	if found!=None:
		break
#print(found)
print(abs(2-found[0])+abs(2-found[1]))