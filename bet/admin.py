from django.contrib import admin

# Register your models here.
from bet.models import Bet, Game, BetType

admin.site.register(Bet)
admin.site.register(Game)
admin.site.register(BetType)