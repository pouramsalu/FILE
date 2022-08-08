# my_file=open("people.txt")
# print(my_file.read())


# f=open("meraki1.txt","r")
# count=0
# for line in f:
#     if line!="":
#         count=+1
#     print(count)
# f.close()


# file=open("abc.txt")
# b=file.read()
# print(b)
# file.close()

# file=open("riamroi.txt","w")
# file.write("Abhishek-Gurgaon\n")
# file.write("Ranveer-Delhi")
# file.close()

file=open("riamroi.txt","r")
b=file.readlines()
print(b)
file.close()