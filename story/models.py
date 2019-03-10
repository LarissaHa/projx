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

    #published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title
    
class Player(models.Model):
    name = models.CharField(max_length=20)
    #avatar
    level = models.IntegerField()
    #add fields

    def new_player(self):
        self.level = 0
        self.save()

    def __str__(self):
        return self.name

class Solved(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    solved_date = models.DateTimeField(blank=True, null=True)

    def solve(self):
        self.solved_date = timezone.now()
        self.save()

#class Friends(models.Model):
#    ego = models.ForeignKey(Player, on_delete=models.CASCADE)
#    knows = models.ForeignKey(Player, on_delete=models.CASCADE)
#
#    def knowing(self):
#        self.save()