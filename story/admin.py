from django.contrib import admin
from .models import Quest, Player, Solved

admin.site.register(Quest)
admin.site.register(Player)
admin.site.register(Solved)