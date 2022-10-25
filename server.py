import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def load_clubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def load_competitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except Exception as error:
        if len(request.form['email']) == 0:
            return f"Please write an email adress."
        else:
            return f"Sorry, that email wasn\'t found."


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    date_competition = datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
    date = datetime.today()

    try:
        if (date > date_competition):
            raise Exception('Competition already passed, choose a competition still open')
        if places_required > 12:
            raise Exception('12 places maximum please')
        if places_required * 3 > int(club['points']):
            raise Exception('not enough points')
        if places_required > int(competition['numberOfPlaces']):
            raise Exception('not enough places')

        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        club['points'] = int(club['points']) - (places_required * 3)
        flash('Success, booking complete!')

    except Exception as error:
        flash(f'{error}')

    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/board')
def board():
    club_infos = [(club['name'], club['points']) for club in clubs]
    return render_template('board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
