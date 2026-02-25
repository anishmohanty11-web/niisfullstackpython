#wap take emp salary from keyboard if sal>=5000 da=30% hra=20% salary<5000 da=20% hra=10% then display basic salary da hra and totalsal....


sal = float(input("Enter basic salary: "))

if sal >= 5000:
    da = sal * 0.30
    hra = sal * 0.20
else: 
    da=sal*20/100
    hra=sal*10/100

total = sal + da + hra

print("Basic Salary =", sal)
print("DA =", da)
print("HRA =", hra)
print("Total Salary =", total)