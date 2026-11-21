import numpy as np

a=np.array([[
    1,2,3],[7,8,9],[7,8,9],[1,2,3]])
x,y=a.shape
# print(x)
# print(y)
# x-row
# y-column

for j in range(y):
  for i in range(x):
  # for j in range(3):
      if i==j:

        if a[i][j]==1:
          for k in range(i+1,x):
            t=a[k][j]/a[i][j]
            r=t*a[i]
            a[k]=a[k]-r
        else:
          a[i][j]=a[i][j]/a[i][j]
          for k in range(i+1,x):
            t=a[k][j]/a[i][j]
            r=t*a[i]
            a[k]=a[k]-r
        for s in range (j+1,y):
          t1=a[i][s]/a[i][j]
          c=t1*a[i][j]
          a[i][s]=a[i][s]-c
        print(a)



print(a)
cnt=0
for i in range(x):
  for j in range(y):
    if i==j:
      cnt=cnt+1
print(cnt)


