letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_low = []
for l in letters:
    letters_low.append(l.lower())
print(letters_low)
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = dict(zip(letters, points))
letter_to_points.update(dict(zip(letters_low, points)))
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


brownie_points = score_word('BROWNIE')
print(brownie_points)

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': [
    'ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

player_to_points = {}


def update_point_totals():
    for player in player_to_words:
        print(player, player_to_words[player])
        player_points = 0
        for word in player_to_words[player]:
            player_points += score_word(word)
        player_to_points[player] = player_points
    print(player_to_points)


update_point_totals()


def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words.update({player: [word]})


play_word('player1', 'TIGER')
play_word('player2', 'EGGBERT')
play_word('player2', 'cartwheel')

player_to_points = {}

update_point_totals()
