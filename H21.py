n=int(input("Enter N value"))
a=[]
for i in range(n):
  b=int(input("Enter value"))
  a.append(b)
al=a[(len(a)//2):]
ah=a[:(len(a)//2)]
aa=sum(al)/len(al)
ab=sum(ah)/len(ah)
if aa==ab:
  print("yes")
else:
  print("no")
