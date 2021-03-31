from collections import defaultdict
winner=defaultdict(int)
for _ in range(int(input())):
	winner[input()]+=1
winScore=max(winner.values())
for i in winner:
	if winner[i]==winScore:
		print(i)
