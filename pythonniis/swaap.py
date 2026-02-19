#swapping 2 number using 3rd variable.

a=10
b=12
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)



#without using 3rd variable.
a=10
b=12
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)

#xor(^) oper.

a=10
b=12
print("before swapping a=",a,"b=",b)
a=a^b
b=a^b
a=a^b
print("after swapping a=",a,"b=",b)

##

a,b,c=10,2.5,"hi"
print(a,b,c)


a=10
b=29
a,b=b,a
print(a,b)


#swapping three number L to R usnig 4th variable.

a=1
b=2
c=3

print("before swapping a=",a,"b=",b,"c=",c)
d=c
c=b
b=a
a=d
print("after swapping a=",a,"b=",b,"c=",c)
