names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina",
         "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0,
                   14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records = list(zip(insurance_costs, names))
print(medical_records)
num_medical_records = len(medical_records)
print("There are {} medical records.".format(num_medical_records))
first_medical_record = medical_records[0]
print("Here is the first medical record: {}".format(first_medical_record))
print("Here are the medical records sorted by insurance cost: {}".format(
    sorted(medical_records)))
medical_records.sort()
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: {}".format(
    cheapest_three))
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: {}".format(priciest_three))
occurences_paul = names.count("Paul")
print("There are {} individuals with the name Paul in our medical records.".format(
    occurences_paul))
medical_records_names_first = sorted(list(zip(names, insurance_costs)))
print("Alphabetical order: {}".format(medical_records_names_first))
middle_five_records = medical_records_names_first[3:8]
print(middle_five_records)
