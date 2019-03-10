from django.shortcuts import render, get_object_or_404
from .models import Quest

# Create your views here.
def quest_list(request):
    quests = Quest.objects.order_by('level')
    return render(request, 'story/quest_list.html', {'quests' : quests})

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