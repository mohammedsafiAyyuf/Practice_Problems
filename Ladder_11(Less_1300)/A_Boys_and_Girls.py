inputFile=open("input.txt",'r')
outputFile=open("output.txt",'w')


n,m=list(map(int,inputFile.readline().split()))
ans=""
if n>m:
	for i in range(m):
		ans+="BG"
	for i in range(abs(m-n)):
		ans+="B"
else:
	for i in range(n):
		ans+="GB"
	for i in range(abs(m-n)):
		ans+="G"
outputFile.write(ans)