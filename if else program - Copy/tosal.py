#wap take emp salary from keyboard if sal>=5000 da=30% hra=20% salary<5000 da=20% hra=10% then display basic salary da hra and totalsal....

print("enter basic salary")
sal = float(input())

da = sal * 0.30 if sal >= 5000 else sal* 0.20 
hra = sal * 0.20 if sal >= 5000 else sal* 0.10

total = sal + da + hra	


print("Basic Salary =", sal)
print("DA =", da)
print("HRA =", hra)
print("Total Salary =", total)