filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    f=open(file,'w')
    f.writelines('Hello')
    f.close()

