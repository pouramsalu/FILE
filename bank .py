# # WRITE METHOD
# banks_list=['kotak','HDFC','RBI','SBI','Bank of Baroda']
# file=open("file_question3.txt","w")
# i=0
# while i<len(banks_list):
#     file.write(banks_list[i]+"\n")
#     i=i+1
# file.close()

# READ METHOD
# a=["HDFC","SBI","RBL"]
# file=open("bank.txt","r")
# d=file.read()
# i=0
# while i<len(a):
#     i+=1
# print(d)
# file.close()




a="this is a cup"
i=0
b=[]
s=""
while i<len(a):
    if a[i]==" ":
        b.append(s)
        s=" "
    else:
        s+=a[i]
    i+=1
if s:
    b.append(s)
    print(b)