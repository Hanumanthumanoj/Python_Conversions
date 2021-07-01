print("****Simple Calculator***",sep=" ")
a=int(input("Enter the numbere1"))
b=int(input("Enter the number2"))
c=input("Operators for calculator is + , - , * , / , // ")
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
else:
    pass
