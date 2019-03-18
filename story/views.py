from django.shortcuts import render, get_object_or_404, redirect
from .models import Quest, Player
from .forms import NewPlayer, EditPlayer

# Create your views here.
def quest_list(request):
    quests = Quest.objects.order_by('level')
    return render(request, 'story/quest_list.html', {'quests' : quests})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'story/player_list.html', {'players' : players})

def welcome(request):
    return render(request, 'story/welcome.html', {})

def quest(request, pk):
    quest = get_object_or_404(Quest, pk=pk)

    solution = request.GET.get('q', '')
    if solution == quest.solution:
        key = ['x']
    else:
        key = []

    return render(request, 'story/quest.html', {'quest': quest, 'key': key, 'solution': solution })

def detail_player(request, pk):
    player = get_object_or_404(Player, pk=pk)

    return render(request, 'story/detail_player.html', {'player': player, 'pk': pk})

def new_player(request):
    if request.method == "POST":
        form = NewPlayer(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.points = 0
            player.level = 0
            player.save()
            return redirect('detail_player', pk=player.pk)
    else:
        form = NewPlayer()
    return render(request, 'story/new_player.html', {'form': form})
    #return redirect('reviews/review_edit.html', {'form': form, 'pk': product})

def edit_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if player.user == request.user:
        if request.method == "POST":
            form = EditPlayer(request.POST, instance=player)
            if form.is_valid():
                player = form.save(commit=False)
                player.save()
                return redirect('detail_player', pk=player.pk)
        else:
            form = EditPlayer(instance=player)
        return render(request, 'story/edit_player.html', {'form': form})
    else:
        return render(request, 'story/forbidden.html', {})
    