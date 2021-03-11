# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0
def insurance_cost(age, sex, bmi, num_of_children, smoker):
  return 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Add insurance estimate formula below
print("This person's insurance cost is {} dollars.".format(insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))
# Age Factor

print("The change in cost of insurance after increasing the age by 4 years is {} dollars.".format(insurance_cost(age=28+4, sex=0, bmi=26.2, num_of_children=3, smoker=0)-insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))

# BMI Factor
print("The change in estimated insurance cost after increasing BMI by 3.1 is {} dollars.".format(insurance_cost(age=28, sex=0, bmi=26.2+3.1, num_of_children=3, smoker=0)-insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))

# Male vs. Female Factor
print("The change in estimated cost for being male instead of female is {} dollars.".format(insurance_cost(age=28, sex=1, bmi=26.2, num_of_children=3, smoker=0)-insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))

# Extra Practice
print("The change in estimated cost for being a smoker instead of a non-smoker is {} dollars.".format(insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=1)-insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))
print("The change in estimated cost for having 3 children instead of none is {} dollars.".format(insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=0, smoker=0)-insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)))