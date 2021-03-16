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
