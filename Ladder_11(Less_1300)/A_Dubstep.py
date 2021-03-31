string=input()
string=string.replace("WUB"," ")
word=list(string.strip().split(" "))
print(*word)