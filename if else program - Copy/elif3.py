#wap take two  number from from keyboard enter your choice 1.add 2.sub 3.mul invalid choice menu driven program""""

print("enter two numbers")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\1.sub\n2.mul")
ch=int(input())
if ch==1:
	print("sum=",no1+no2)
elif no==2:
	print("sub=",no1-no2)
elif no==3:
	print("mul=",no1*no2)
else:
	print("invalid choice")