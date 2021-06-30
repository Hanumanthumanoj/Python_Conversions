a=int(input("Enter an integer value"))
b=float(input("Enter an Float Value"))
c=input("Enter an String value")
d=bool(input("Enter the boolean Value"))

#Type of given User
print("User Type" , type(a))
print("User Type" , type(b))
print("User Type" , type(c))
print("User Type" , type(d))

#Type Conversion for integer
a1=float(a)
print("Converted integer to float : ", a1 , type(a1))
a2=str(a)
print("Converted integer to String : " , a2 , type(a2))
a3=bool(a)
print("Converted integer to Bool : " , a3 , type(a3))

#Type Conversion for float

b1=int(b)
print("Converted Float to Integer",b1,type(b1))
b2=str(b)
print("Converted float to String " , b2 , type(b2))
b3= bool(b)
print("Converted float to Boolean " ,b3 , type(b3))

#Type Conversion for String
c1=int(c)
print("Converted String to integer " , c1 , type(c1))
c2=float(c)
print("Converted String to float " , c2 , type(c2))
c3=bool(c)
print("Converted String to Boolean" , c3 , type(c3))

#Type conversion for Boolean
d1=int(d)
print("Converted to Boolean to Integer " , d1 , type(d1))
d2=float(d)
print("Converted to Boolean to float " , d2 , type(d2))
d3=str(d)
print("Converted to boolean to String " , d3 , type(d3))






