import datetime
import random

from django.shortcuts import render, redirect


def index(request):
    try:
        request.session['ninja_gold']
    except KeyError:
        request.session['ninja_gold'] = 0

    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []

    return render(request, 'index.html')


def process_money(request):
    if request.method == 'POST':
        place = request.POST["place"]

        farm = [10, 20]
        cave = [5, 10]
        house = [2, 5]
        casino = [-50, 50]

        place_lim = []
        if place == "farm":
            place_lim = farm
        elif place == "cave":
            place_lim = cave
        elif place == "house":
            place_lim = house
        elif place == "casino":
            place_lim = casino

        rand_num = random.randint(place_lim[0], place_lim[1])
        request.session['ninja_gold'] += rand_num

        if rand_num >= 0:
            request.session['activities']\
                .append(f"Earned {rand_num} golds from the {place}! ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
        else:
            request.session['activities']\
                .append(f"Entered a {place} and lost {abs(rand_num)} golds... Ouch... ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")

    return redirect("index")


def restart_session(request):
    request.session['ninja_gold'] = 0
    request.session['activities'] = []

    return redirect("index")
