names=list(input()+input())
jumbled=list(input())
names.sort()
jumbled.sort()
if names==jumbled:
	print("YES")
else:
	print("NO")