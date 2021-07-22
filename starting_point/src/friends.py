def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    return food in person["favourites"]["snacks"]
    
def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    running_total = 0
    for person in people:
        running_total += person["monies"]
    return running_total

def l_money(person1, person2, amount):
    person1["monies"] -= amount
    person2['monies'] += amount

def all_favourite_foods(people):
    foods_list = []
    for person in people:
        for food in (person["favourites"]["snacks"]):
            foods_list.append(food)
    return foods_list

def find_no_friendends(people):
    list = []
    for person in people:
        if len(person["friends"]) == 0:
            list.append(person)
    return list