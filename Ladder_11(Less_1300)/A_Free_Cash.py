from collections import defaultdict
hashTable=defaultdict(int)
for _ in range(int(input())):
	time=input()
	hashTable[time]+=1
print(max(hashTable.values()))