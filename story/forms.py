from django import forms

from .models import Player, Quest, Solved

class NewPlayer(forms.ModelForm):

    class Meta:
         model = Player
         fields = ('name', )

class EditPlayer(forms.ModelForm):

    class Meta:
         model = Player
         fields = ('name', 'description')
