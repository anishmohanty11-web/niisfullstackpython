def sical():
	print("enter princple")
	p=float(input())
	print("enter rate of interest")
	r=float(input())
	print("enter time")
	t=float(input())
	si=p*r*t/100
	return sical
res=sical()
print("simple interest=",res)