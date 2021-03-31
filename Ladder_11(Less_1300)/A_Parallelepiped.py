import math
a,b,c=list(map(int,input().split()))
height=math.sqrt(b*c/a)
breath=b/height
length=a/breath
print(int((height*4+breath*4+length*4)))