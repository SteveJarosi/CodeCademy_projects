letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0
print(letter_to_points)


def score_word(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_points:
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total
