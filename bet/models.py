from django.db import models
from enum import Enum
from django.contrib.auth.models import User


class StatusBet(Enum):
    APOSTADO = 0
    VITORIA = 1
    DERROTA = 2
    EXPIRADA = 3

class Game(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"
    
class GameType(models.Model):
    name = models.CharField(max_length=400)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")

    def __str__(self):
        return f"{self.name}"
    
class BetType(models.Model):
    name = models.CharField(max_length=400)
    condicao = models.CharField(max_length=400)
    multiplicadorMin = models.FloatField()
    multiplicadorMax = models.FloatField()
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name="gameType")

    def __str__(self):
        return f"{self.name} {self.multiplicadorMin} {self.condicao} {self.gametype}"
    
class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.TextField()
    betType = models.ForeignKey(BetType, on_delete=models.CASCADE, related_name="betType")
    statusBet = models.IntegerField(choices=[(tag, tag.value) for tag in StatusBet])
    idUltimoJogo = models.TextField()

    def __str__(self):
        return f"{self.user} {self.quantity} {self.statusBet} {self.betType} {self.date}"
    

