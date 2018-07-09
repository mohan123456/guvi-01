a=[]
g=[]
for i in range(0,5):
 b=int(input("numbers"))
 a.append(b)
c=a[4]
d=a[0]
#print(c)  
#print(d)  
for i in range(d,c+1):
  #print(i)
  g.append(i)
#print(g)
print(sum(g)-sum(a))  
