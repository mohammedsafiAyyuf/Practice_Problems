from collections import defaultdict
HashTable=defaultdict(int)
s1=input()
s2=input()
for i in s1:
	HashTable[i]+=1
HashTable[" "]=100000
flag=0
for i in s2:
	if HashTable[i]>0:
		HashTable[i]-=1
	else:
		flag=1
		break
if flag==1:
	print("NO")
else:
	print("YES")
