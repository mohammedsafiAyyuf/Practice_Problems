string=input()
ans="hello"
idx=0
for i in string:
	if i==ans[idx]:
		idx+=1
	if idx==5:
		print("YES")
		break
else:
	if idx==5:
		print("YES")
	else:
		print("NO")
