code=input()
idx=0
string=""
while idx<len(code):
	if code[idx]==".":
		string+="0"
	elif code[idx]=="-":
		if code[idx+1]==".":
			string+="1"
		elif code[idx+1]=="-":
			string+="2"
		idx+=1
	idx+=1
print(string)
