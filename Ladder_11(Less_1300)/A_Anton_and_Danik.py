n=int(input())
string=input()
a=string.count("A")
d=string.count("D")
if a>d:
	print("Anton")
elif a==d:
	print("Friendship")
else:
	print("Danik")