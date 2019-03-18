from django.conf import settings
from django.db import models
from django.utils import timezone


class Quest(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    level = models.IntegerField()
    required = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    task = models.TextField()
    solution = models.CharField(max_length=100)
    key = models.CharField(max_length=200)
    points = models.IntegerField(default=20)
    is_parallel = models.BooleanField(default=False)
    #parallel_quest = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)

    published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title
    
class Player(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING, blank=True, null=True)
    #avatar
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    TITLES = (("Chef","Chef"),("Mitläufer","Mitläufer"),("Novize","Novize"))
    title = models.CharField(choices=TITLES, default="Novize", max_length=100)
    ATTITUDES = (("hell", "hell"), ("dunkel", "dunkel"), ("neutral", "neutral"))
    attitude = models.CharField(choices=ATTITUDES, default="neutral", max_length=100)
    description = models.CharField(max_length=1000, default="uninteressant")

    def new_player(self):
        self.level = 0
        self.save()

    #def level_up(self):


    def __str__(self):
        return self.name

class Solved(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    solved_date = models.DateTimeField(blank=True, null=True)

    def solve(self):
        self.solved_date = timezone.now()
        #if self.quest.is_parallel == True:
        #    if self.quest.parallel_quest in ...
        #       self.player.points = self.player.points
        #    else:
        #       self.player.points = self.player.points + self.quest.points
        self.save()

#class Friends(models.Model):
#    ego = models.ForeignKey(Player, on_delete=models.CASCADE)
#    knows = models.ForeignKey(Player, on_delete=models.CASCADE)
#
#    def knowing(self):
#        self.save()