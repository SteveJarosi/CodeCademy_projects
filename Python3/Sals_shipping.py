weight = 41.8
# Ground shipping
if weight <= 2:
    cost = 1.50 * weight + 20
elif weight > 2 and weight <= 6:
    cost = 3 * weight + 20
elif weight > 6 and weight <= 10:
    cost = 4 * weight + 20
else:
    cost = 4.75 * weight + 20
print("Ground shipping: $ " + str(cost))

premium_ground_shipping = 125

print("Premium ground shipping: $ " + str(premium_ground_shipping))

# Drone shipping
if weight <= 2:
    cost = 4.50 * weight
elif weight > 2 and weight <= 6:
    cost = 9 * weight
elif weight > 6 and weight <= 10:
    cost = 12 * weight
else:
    cost = 14.25 * weight

print("Drone shipping: $ " + str(cost))
