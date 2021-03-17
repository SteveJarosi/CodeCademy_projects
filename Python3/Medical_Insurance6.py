names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0,
                             3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0,
                          3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
i = 0
while i < len(actual_insurance_costs):
    total_cost += actual_insurance_costs[i]
    i += 1
average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: {} dollars.".format(average_cost))
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    insurance_cost_diff = abs(insurance_cost - average_cost)
    print("The insurance cost for {name} is {insurance_cost} dollars.".format(
        name=name, insurance_cost=insurance_cost))
    if insurance_cost > average_cost:
        print("The insurance cost for {} is ${} above average.".format(
            name, insurance_cost_diff))
    elif insurance_cost < average_cost:
        print("The insurance cost for {} is ${} below average.".format(
            name, insurance_cost_diff))
    else:
        print("The insurance cost for {} is equal to the average.".format(name))
updated_estimated_costs = [x*11/10 for x in estimated_insurance_costs]
print(updated_estimated_costs)
