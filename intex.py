#28
n=int(input("size"))
l=[]
for i in range(0,n):
  b=int(input())
  l.append(b)
for x in l:
    print(x,l.index(x))
