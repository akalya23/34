st2,st3= input().split()
for i in range(0,len(st2)-len(st3)+1):
  if st2[i:len(st3)+i] == st3:
    print('yes')
    break
else:
  print('no')
