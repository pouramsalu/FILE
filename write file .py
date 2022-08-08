# f=open("abc.txt","w")
# f.write("hello to all")
# f.close()


# f=open("abc.txt","w")
# s=input("enter string=")
# f.write(s)
# f.close()

# f=open("abc.txt","w")
# n=int(input("how many lines="))
# for i in range(n):
#     s=input("enter string=")
#     f.write(s+"\n")
# f.close()

# f=open("abc.txt","w")
# n=int(input("how many lines="))
# l=[]
# for i in range(n):
#     s=input("enter string=")
#     l.append(s+"\n")
# f.writelines(l)
# f.close

# f=open("abc.txt","w")
# n=int(input("how many lines="))
# l=[]
# for i in range(n):
#     s=input("enter string=")
#     l.append(s+"\n")
#     f.writelines(l)
# f.close

# f=open("abc.txt","r")
# print(f.tell())
# f.close()



file=open("teresa.txt","w")
b=file.read("today is monday")
print(b)
file.close()