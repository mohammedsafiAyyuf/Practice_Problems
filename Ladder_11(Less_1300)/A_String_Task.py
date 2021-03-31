string=input().lower()
output=""
for i in string:
	if i not in "aeiouy":
		output+="."+i
print(output)
