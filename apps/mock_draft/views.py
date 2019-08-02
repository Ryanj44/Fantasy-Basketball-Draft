from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
import random

# Create your views here.

def index(request):
    context = {
        "all_teams": Team.objects.all(),
    }
    return render(request, "mock_draft/index.html", context)

def create_team(request):
    request.session['original_pick']= random.randint(1,10)
    this_team = Team.objects.create(name=request.POST['name'], pick = request.session['original_pick'])
    other_team = Team.objects.create(name="Drafted Players", pick = 1)
    request.session['team']=this_team.id
    request.session['others']=other_team.id
    request.session['round']=1
    request.session['pick'] = request.session['original_pick']
    for x in range(0, (request.session['pick'] -1)):
        available_players=Player.objects.exclude(teams=other_team)
        other_team.players.add(available_players[0])
    return redirect("/draft")

def draft(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team=Team.objects.get(id=request.session['others'])
    context = {
        "all_players": Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)).order_by("ranking"),
        "user_team":this_team,
        "user_players":this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking"),
    }
    return render(request, "mock_draft/draft.html", context)

def point(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    context = {
        "all_players": Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)|Q(position="SG")|Q(position="SG/SF")|Q(position="SF")|Q(position="SF/PF")|Q(position="PF")|Q(position="PF/C")|Q(position="C")),
        "user_team":this_team,
        "user_players":this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking")
    }
    return render(request, "mock_draft/draft.html", context)

def shooting(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    context = {
        "all_players": Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)|Q(position="PG")|Q(position="SF")|Q(position="SF/PF")|Q(position="PF")|Q(position="PF/C")|Q(position="C")),
        "user_team":this_team,
        "user_players": this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking")
    }
    return render(request, "mock_draft/draft.html", context)

def small(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    context = {
        "all_players": Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)|Q(position="PG")|Q(position="PG/SG")|Q(position="SG")|Q(position="PF")|Q(position="PF/C")|Q(position="C")),
        "user_team":this_team,
        "user_players":this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking")
    }
    return render(request, "mock_draft/draft.html",context)

def power(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    context = {
        "all_players": Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)|Q(position="PG")|Q(position="PG/SG")|Q(position="SG")|Q(position="PF")|Q(position="PF/C")|Q(position="C")),
        "user_team":this_team,
        "user_players":this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking")
    }
    return render(request, "mock_draft/draft.html", context)

def center(request):
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    context={
        "all_players":Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team)|Q(position="PG")|Q(position="PG/SG")|Q(position="SG")|Q(position="SG/SF")|Q(position="SF")|Q(position="SF/PF")|Q(position="PF")),
        "user_team":this_team,
        "user_players":this_team.players.all(),
        "other_players":other_team.players.all().order_by("-ranking")
    }
    return render(request, "mock_draft/draft.html", context)

def add_player(request, player_id):
    this_player = Player.objects.get(id=player_id)
    this_team = Team.objects.get(id=request.session['team'])
    other_team = Team.objects.get(id=request.session['others'])
    this_team.players.add(this_player)
    request.session['pick'] += 1
    available_players = Player.objects.exclude(Q(teams=this_team)|Q(teams=other_team))
    if request.session['round'] % 2 == 1:
        for x in range(0, 2*(10-request.session['original_pick'])):
            other_team.players.add(available_players[0])
            request.session['pick'] += 1
    if request.session['round'] % 2 == 0:
        for x in range(0, 2*(request.session['original_pick'] -1)):
            other_team.players.add(available_players[0])
            request.session['pick'] += 1
    request.session['round'] += 1
    if request.session['round'] == 14:
        return redirect("/results")
    return redirect("/draft")

def results(request):
    this_team = Team.objects.get(id=request.session['team'])
    context = {
        "team": this_team,
        "team_players": this_team.players.all()
    }
    other_team = Team.objects.get(id=request.session['others'])
    other_team.delete()
    return render(request, "mock_draft/results.html", context)

def team(request, team_id):
    this_team = Team.objects.get(id=team_id)
    context = {
        "team": this_team,
        "players": this_team.players.all()
    }
    return render(request, "mock_draft/team.html", context)
