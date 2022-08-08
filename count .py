# f=open("name.txt","r")
# count=0
# for line in f:
#     if line!="":
#         count+=1
# print(count)
# f.close()


# f=open("data.txt","r")
# count=0
# for i in f:
#     count=count+1
# print(count)
# f.close()

f=open("name.txt","r")
m=f.readlines()
i=0
count=0
while i<len(m):
    count=count+1
    i=i+1
print(count)
f.close()