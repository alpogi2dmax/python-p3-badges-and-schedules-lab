def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badges = list()
    for i in range(len(names)):
        badges.append(f'Hello, my name is {names[i]}.')
    return badges

def assign_rooms(names):
    badges = list()
    for i in range(len(names)):
        badges.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    return badges

def printer(names):
    for i in range(len(names)):
        print(f"Hello, my name is {names[i]}.")
    for i in range(len(names)):
        print(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
