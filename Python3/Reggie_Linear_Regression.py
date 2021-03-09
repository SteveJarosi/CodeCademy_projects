def get_y(m, b, x):
    y = m*x + b
    return y

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

#Write your calculate_error() function here
def calculate_error(m, b, p):
    return abs(get_y(m,b, p[0])-p[1])

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

#Write your calculate_all_error function here
def calculate_all_error(m, b, dps):
    err = 0
    for datapoint in dps:
        err+= calculate_error(m, b, datapoint)
    return err

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

possible_ms = [i/10 for i in range(-100, 100, 1)] #your list comprehension here
possible_bs = [i/10 for i in range(-200, 200, 1)] #your list comprehension here
# the above method gives an error in the range of  0.0000000000000001, but turns out to be significant!!!
#possible_ms = [m * 0.1 for m in range(-100, 101)]
#possible_bs = [b * 0.1 for b in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            print(best_m, best_b, smallest_error)
            smallest_error = round(calculate_all_error(m, b, datapoints), 3)
            best_m = m
            best_b = b
print(best_m, best_b, smallest_error)
print(get_y(best_m, best_b, 6))