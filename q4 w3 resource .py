file=open("question3.txt")
f=file.readlines()
i=-1
while i>-len(f):
    if f[-i]==f[-i]:
        print(f[i])
        break
    i=i-1
file.close()