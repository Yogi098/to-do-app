import glob

myfiles=glob.glob("APP1/Bonus/files/*.txt")

for filepath in myfiles:
    with open(filepath,'r') as file:
        print(file.read().upper())


# print(myfiles)
