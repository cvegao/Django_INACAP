from django.db.models import Q
from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker


def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"ligasBeisbol": League.objects.filter(sport="Baseball"),
		"ligasMujeres": League.objects.filter(name__contains="Women"),
		"ligasHockey": League.objects.filter(name__contains="Hockey"),
		"ligasNoFutbol": League.objects.exclude(name__icontains="football"),
		"ligasConference": League.objects.filter(name__icontains="conference"),
		"ligasAtlantic": League.objects.filter(name__icontains="atlantic"),
		"equiposDallas": Team.objects.filter(location="Dallas"),
		"equiposRaptors": Team.objects.filter(team_name="Raptors"),
		"equiposCity": Team.objects.filter(location__icontains="city"),
		"equiposT": Team.objects.filter(team_name__startswith="T"),
		"equiposSortedByLocation": Team.objects.all().order_by("location"),
		"jugadoresCooper": Player.objects.filter(last_name="Cooper"),
		"jugadoresJoshua": Player.objects.filter(first_name="Joshua"),
		"jugadoresCooperNoJoshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"jugadoresAlexanderWyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")