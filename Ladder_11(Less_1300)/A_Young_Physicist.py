forceX=0
forceY=0
forceZ=0

for _ in range(int(input())):
    force=list(map(int,input().split()))
    forceX+=force[0]
    forceY+=force[1]
    forceZ+=force[2]
if forceX==0 and forceY==0 and forceZ==0:
    print("YES")
else:
    print("NO")