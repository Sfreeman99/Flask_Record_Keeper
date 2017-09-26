from flask import Flask, render_template, redirect, request
import disk, core
app = Flask(__name__)


@app.route('/')
def root():
    leaderboard = disk.give_roster()
    return render_template('scoreboard.html', leaderboard=leaderboard)


@app.route('/win_or_lose')
def scoreboard():
    return render_template('index.html', leaderboard=disk.give_roster())


@app.route('/scores', methods=['POST'])
def scores():
    player_1 = request.form['username1']
    score_1 = int(request.form['score1'])
    player_2 = request.form['username2']
    score_2 = int(request.form['score2'])
    leaderboard = disk.give_roster()
    roster = core.names(leaderboard, player_1)
    roster = core.names(leaderboard, player_2)
    new_roster = core.update_leaderboard(roster, player_1, score_1, player_2,
                                         score_2)
    disk.dict_to_file(new_roster)
    # for player in team['players']:
    #     if not roster.get(player, False):
    #         roster[player] = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'W/L': 0}
    return redirect('/win_or_lose')


# @app.route('/individual_stats', methods=['POST'])