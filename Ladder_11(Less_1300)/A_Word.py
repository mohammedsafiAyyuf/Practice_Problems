string=input()
upperCase=0
lowerCase=0
for i in string:
	if 97<=ord(i)<=122:
		lowerCase+=1
	else:
		upperCase+=1
if upperCase>lowerCase:
	print(string.upper())
else:
	print(string.lower())