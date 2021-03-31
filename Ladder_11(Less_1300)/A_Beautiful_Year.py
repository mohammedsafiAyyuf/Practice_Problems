no=int(input())
no+=1
while(len(set(str(no)))!=len(str(no))):
	no+=1
print(no)