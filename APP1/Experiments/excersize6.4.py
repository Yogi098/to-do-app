files=['a.txt','b.txt','c.txt']

for file in files:
    f=open(file,'r')
    content=f.read()
    print(content)