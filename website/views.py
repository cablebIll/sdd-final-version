from flask import Blueprint, render_template
import requests
from functools import cache

views = Blueprint('views', __name__)


@cache
@views.route('/players/')
def players():
    response = requests.get("https://vlrgg.cyclic.app/api/players")
    players = response.json()
    return render_template('players.html', content=players)


@views.route("/players/<name>")
def player(name):
    response = requests.get("https://vlrgg.cyclic.app/api/players")
    players = response.json()
    our_player = None
    for player in players["players"]:
        if player["player_name"] == name:
            our_player = player
    return render_template('player.html', player=our_player)


#@views.route('/rankings/<name>')
#def rankings(name):
#    response = requests.get("https://vlrgg.cyclic.app/api/rankings/<name>")
#    rankings = response.json()
#    print(rankings)
#    return render_template('rankings.html', rankings=rankings)


#@views.route('/rankings')
#def rankings_home():
#    regions = ('korea', 'europe', 'north-america', 'brazil', 'asia-pacific',
#               'latin-america', 'oceania', 'mena', 'china', 'japan', 'gc', 'la-s',
#               'la-n')
#    return render_template('rankings_home.html', regions=regions)


@views.route('/events')
def events():
    response = requests.get('https://vlrgg.cyclic.app/api/events')
    events = response.json()
    print(events)
    return render_template('events.html', events=events)


@views.route('/matches/upcoming')
def matches_upcoming():
    response = requests.get('https://vlrgg.cyclic.app/api/matches/upcoming')
    matches = response.json()
    print(matches)
    return render_template('matches_upcoming.html', matches=matches)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/matches/completed')
def matches_completed():
    response = requests.get('https://vlrgg.cyclic.app/api/matches/results')
    matches = response.json()
    return render_template('matches_completed.html', matches=matches)