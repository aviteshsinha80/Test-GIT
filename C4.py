'''height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))
BMI = weight/height**2
BMI = round(BMI,0)
print("BMI", BMI)
if BMI<23:
    print("Under weight")
elif BMI>40:
    print("Clinically Obese")
elif BMI>=33:
    print("Obesity")
elif BMI>=28:
    print("Slightly over weight")
elif BMI>=23:
    print("Normal weight")'''

print("Size: 1.Small ($2.50), 2.Medium ($3.00), 3.Large ($3.50)")
size = int(input("Enter coffee size 1/2/3:"))
print("Type: 1.Espresso ($1.50 extra), 2.Latte or Cappuccino ($2.00 extra), 3.Drip or Americano ($1.00 extra)")
type = int(input("Enter type of coffee 1/2/3:"))
print("Milk: 1. Whole ($0.50 extra), 2. Skim ($0.25 extra)")
milk = int(input("Enter milk type 1/2:"))
cost=0
if size==1:
    cost=cost+2.5
elif size==2:
    cost=cost+3
else:
    cost=cost+3.5
if type==1:
    cost=cost+1.5
elif type==2:
    cost=cost+2
else:
    cost=cost+1
if milk==1:
    cost=cost+0.5
else:
    cost=cost+0.25
print(f"Cost of coffee is: ${cost}")









