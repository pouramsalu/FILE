# write a python program to combine each line from 1st line with the corresponding line in second file.

# file1=open("file1.txt","r")
# file2=open("file2.txt","r")
# file3=open("merged.txt","w")
# line1=file1.readlines()
# line2=file2.readlines()
# for i in range(len(line1)):
#     merged=line1[i]+line2[i]
#     file3.write(merged)
# file1.close()
# file2.close()
# file3.close()

# write a python program that takes a text file as input and return the number
# of words of a given text.

# file=open("no of words.txt","r")
# count=0
# for line in file:
#     words=line.split("")
#     count=count+len(words)
# print(count)
# file.close()


# # f=open("on.txt","w")
# # f.write("seminao.salu")
# f=open("on.txt","r")
# d=f.read()
# a=list(d)
# i=0
# while i<len(a):
#     print(a[i],end="")
#     i+=1
#     if a[i]==".":
#         break
# f.close()

# # file=open("upper case.txt","w")
# # file.write("ABCDE")
# # file.close()
# file=open("upper case.txt","r")
# for x in file.read():
#     y=x.upper()
#     file1=open("upper case1.txt","a")
#     file1.write(y)
# file.close()