gamers = []
def add_gamer(gamer, gamers_list):
    if "name" in gamer.keys() and "availability" in gamer.keys():
        gamers_list.append(gamer)
kimberly = {'name': 'Kimberly Warner', 'availability': ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
def build_daily_frequency_table():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" , "Sunday"]
    return {days[x]: 0 for x in range(7) }
count_availability = build_daily_frequency_table()
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        #print(gamer['availability'])
        for day in gamer['availability']:
            available_frequency[day]+=1
    return available_frequency
print(calculate_availability(gamers, count_availability))
def find_best_night(availability_table):
    best_day = 'Monday'
    for day in availability_table.keys():
        if availability_table[day] > availability_table[best_day]:
            best_day = day
    return best_day
game_night = find_best_night(calculate_availability(gamers, count_availability))
print(game_night)
def available_on_night(gamers_list, day):
    attending = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            attending.append(gamer['name'])
    return attending
attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)
def form_email(name, game, day_of_week):
    return "{name}, your {game} will be held on {day_of_week}".format(name=name, game=game, day_of_week=day_of_week)
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email(gamer, game, day))
send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = []
for gamer in gamers:
    if gamer['name'] not in attending_game_night:
        unable_to_attend_best_night.append(gamer)
print(unable_to_attend_best_night)
count_availability = build_daily_frequency_table()
second_night_availability = calculate_availability(unable_to_attend_best_night, count_availability)
print(second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")