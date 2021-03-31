matrix=[list(input()) for _ in range(4)]
for i in range(3):
	flag=0
	for j in range(3):
		temp=0
		temp+= 1 if matrix[i][j]=="#" else 0
		temp+= 1 if matrix[i+1][j]=="#" else 0
		temp+= 1 if matrix[i][j+1]=="#" else 0
		temp+= 1 if matrix[i+1][j+1]=="#" else 0			
		if temp>=3:
			print("YES")
			flag=1
			break
		temp=0
		temp+= 1 if matrix[i][j]=="." else 0
		temp+= 1 if matrix[i+1][j]=="." else 0
		temp+= 1 if matrix[i][j+1]=="." else 0
		temp+= 1 if matrix[i+1][j+1]=="." else 0			
		if temp>=3:
			print("YES")
			flag=1
			break
	if flag:
		break
else:
	print("NO")	