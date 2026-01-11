weight=float(input("enter the weight in kilogram:"))
height=float(input("enter the height in meters:"))
BMI=weight/(height**2)
if BMI<18.5:
    category="underweight"
elif BMI<25:
    category=" normal weight"
else:
    category=" overweight"
print("\n--- BMI Result ---")
print(f"BMI Value   : {BMI:}")
print(f"Category    : {category}")