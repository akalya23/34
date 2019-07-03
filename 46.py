u2=int(input())
v2=list(map(int,input().split()))
21=0
b2=0
v2.sort(reverse=True)
for i1 in v2:
  v2=a2+i1
  if b2>v2:
    a2=v2
  else:
    a2=b2
    b2=v2
print(a2,b2)
