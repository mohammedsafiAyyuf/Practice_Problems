string1=input()
string2=input()
if len(string1)!=len(string2):
	print("NO")
else:
	count=0
	varied=[]
	for i in range(len(string1)):
		if string1[i]!=string2[i]:
			count+=1
			varied.append((string1[i],string2[i]))

	if count==0 or (count==2 and varied[0][0]==varied[1][1] and varied[1][0]==varied[0][1]):
		print("YES")
	else:
		print("NO")


