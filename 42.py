v1,k1=map(int,input().split())
s=list(map(int,input().split()))
if k==1:
    print(min(s))
elif k==2:
    print(max(s[0],s[v-1]))
else:
    print(max(s))
