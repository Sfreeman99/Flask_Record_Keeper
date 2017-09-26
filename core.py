def update_leaderboard(leaderboard, player_1, score_1, player_2, score_2):
    """ str, str, {'name': {'wins': int, 'losses': int}} -> {'name': {'wins': int, 'losses': int}}, str, str """
    if score_1 > score_2:
        # for player in team_1['players']:
        leaderboard[player_1]['Wins'] += 1
        # for player in team_2['players']:
        leaderboard[player_2]['Losses'] += 1
    elif score_1 < score_2:
        # for player in team_1['players']:
        leaderboard[player_1]['Losses'] += 1
        # for player in team_2['players']:
        leaderboard[player_2]['Wins'] += 1
    # elif team_1['score'] == team_2['score']:
    #     for player in team_1['players']:
    #         roster[player]['Ties'] += 1
    #     for player in team_2['players']:
    #         roster[player]['Ties'] += 1
    return leaderboard


def names(roster, player):
    ''' dict of names, Item -> dict of names
    
    Takes in both names and either sends you to the next function
    of adds the name of the player
    
    '''
    # for player in team['players']:
    if not roster.get(player, False):
        roster[player] = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'W/L': 0}
    return roster
