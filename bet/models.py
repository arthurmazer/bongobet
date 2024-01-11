from django.db import models
from user.models import User
from enum import Enum



class StatusBet(Enum):
    AGUARDANDO_PAGAMENTO = 0
    APOSTADO = 1
    VITORIA = 2
    DERROTA = 3
    EXPIRADA = 4

class Game(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"
    
class BetType(models.Model):
    name = models.CharField(max_length=400)
    condicao = models.CharField(max_length=400)
    apostaMax = models.FloatField()
    multiplicador = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")

    def __str__(self):
        return f"{self.name} {self.multiplicador}"


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBet")
    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    betType = models.ForeignKey(BetType, on_delete=models.CASCADE, related_name="betType")
    statusBet = models.IntegerField(choices=[(tag, tag.value) for tag in StatusBet])

    def __str__(self):
        return f"{self.quantity} {self.statusBet}"
    

