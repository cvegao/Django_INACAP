from django.db.models import Q, Count
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
		# PARTE 2
		"equiposASC": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"jugadoresBP": Team.objects.get(team_name="Penguins", location="Boston").curr_players.all(),
		"jugadoresICBC": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"jugadoresACAF": Player.objects.filter(last_name="Lopez").filter(
			curr_team__league__name="American Conference of Amateur Football"),
		"jugadoresFutbol": Player.objects.filter(curr_team__league__sport="Football"),
		"equiposSophia": Team.objects.filter(curr_players__first_name="Sophia"),
		"ligasSophia": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"jugadoresFloresNoWR": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders", curr_team__location="Washington"),
		"equiposSamuelE": Player.objects.get(first_name="Samuel", last_name="Evans").all_teams.all(),
		"jugadoresMTC": Team.objects.get(team_name="Tiger-Cats", location="Manitoba").all_players.all(),
		"jugadoresWV": Team.objects.get(team_name="Vikings", location="Wichita").all_players.all().exclude(curr_team__team_name="Vikings"),
		"equiposJacobGray": Player.objects.get(first_name="Jacob", last_name="Gray").all_teams.all().exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),
		"joshuaAFABP": Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players"),
		"equiposSobre12": Team.objects.filter(all_players__gte=12),
		"jugadoresEquipos": Player.objects.annotate(count=Count('all_teams')).order_by('-count'),
	}
	return render(request, "leagues/index.html", context)



def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")