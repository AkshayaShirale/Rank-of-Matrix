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

        # elif a[i][j]==0:
cnt=0
# for i in range(x):
#   a[i]=0
#   cnt=cnt+1
# print(cnt)
for q in range(x):
  if a[q][y-1]==0:
    cnt=cnt+1
# print(cnt)
rank=x-cnt
print("Rank of given matrix is:{}".format(rank))


print(a)
# print(x)
# print(y)