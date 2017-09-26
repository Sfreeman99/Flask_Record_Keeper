def give_roster():
    with open("Roster.txt", "r") as files:
        files.readline()
        contestants = files.readlines()
    roster = {}
    for item in contestants:
        sublist = item.split(' | ')
        roster[sublist[0]] = {
            'Wins':
            int(sublist[1]),
            'Losses':
            int(sublist[2]),
            'Ties':
            int(sublist[3]),
            'W/L':
            '{:2f}'.format(
                float(sublist[1]) /
                (float(float(sublist[1]) + float(sublist[2]))) * 100)
        }
    return roster


def dict_to_file(new_roster):
    message = 'Name, Wins, Losses, Ties\n'
    for name, d in new_roster.items():
        message += '{} | {} | {} | {} | {} \n'.format(
            name, d['Wins'], d['Losses'], d['Ties'], d['W/L'])
    with open("Roster.txt", "w") as files:
        files.write(message)


def read_roster():
    with open("Roster.txt", "r") as files:
        files.readline()
        contestants = files.readlines()
    message = 'Name | Wins | Losses | Ties | Win/Loss%\n'

    return (message + '\n'.join(contestants))
