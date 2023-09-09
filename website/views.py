from flask import Flask, redirect, request, Blueprint, render_template, url_for
import os
import requests
from functools import cache

views = Blueprint('views', __name__)


@cache
@views.route('/players/')
def players():
    response = requests.get("https://vlrgg.cyclic.app/api/players")
    players = response.json()
    return render_template('players_brock.html', content=players)

@views.route("/players/<name>")
def player(name):
    response = requests.get("https://vlrgg.cyclic.app/api/players")
    players = response.json()
    our_player = None
    for player in players["players"]:
        if player["player_name"] == name:
            our_player = player
    return render_template('player_brock.html', player=our_player)