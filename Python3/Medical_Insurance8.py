# Add your code here
medical_costs = {"Marina": 6607.0,
                 "Vinay": 3225.0}
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print(medical_costs)
medical_costs.update({"Vinay": 3325.0})
print(medical_costs)
total_cost = 0
for v in medical_costs.values():
    total_cost += v
average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: {average_cost}".format(
    average_cost=average_cost))
names = [n for n in medical_costs.keys()]
print(names)
ages = [27, 24, 43, 35, 52]
zipped_ages = dict(zip(names, ages))
print(zipped_ages)
names_to_ages = {a: b for a, b in zipped_ages.items()}
print(names_to_ages)
marina_age = names_to_ages.get('Marina', None)
print("Marina's age is {marina_age}".format(marina_age=marina_age))

medical_records = {}
medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9,
                            "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3,
                             "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records['Isaac'] = {"Age": 35, "Sex": "Female", "BMI": 20.6,
                            "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7,
                                "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)
print("Connie's insurance cost is {} dollars.".format(
    medical_records['Connie']['Insurance_cost']))
for i in medical_records.keys():
    print("{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}".format(
        Name=i, Age=medical_records[i]['Age'], Sex=medical_records[i]['Sex'], Smoker=medical_records[i]['Smoker'].lower(), BMI=medical_records[i]['BMI'], Insurance_cost=medical_records[i]['Insurance_cost']))


def update_medical_records(name, age, sex, smoker, bmi, insurance_cost):
    medical_records.update({name: {'Age': age, 'Sex': sex, 'Smoker': smoker,
                                   'BMI': bmi, 'Insurance_cost': insurance_cost}})
    return "Record {} updated".format(name)
