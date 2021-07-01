print("****Simple Calculator***",sep=" ")
a=int(input("Enter the numbere1"))
b=int(input("Enter the number2"))
c=input("Operators for calculator is + , - , * , / , // , < , > , == , != ")
if(c=="+"):
    print(f"{a+b}")
elif(c=="-"):
    print("{}".format(a-b))
elif(c=="*"):
    print(f"{a*b}")
elif(c=="/"):
    print(f"{a/b}")
elif(c=="//"):
    print(f"{a//b}")
elif(c=="<"):
    if(a<b):
        print(b,"Is greatest")
elif(c==">"):
    if(a>b):
        print(a,"Is Greatest")
elif(c==("==")):
    if(a==b):
        print("Equal Values")
elif(c==("!=")):
    if(a!=b):
        print("Both values are not Equal")
else:
    pass
