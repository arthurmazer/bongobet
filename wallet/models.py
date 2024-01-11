from django.db import models

# Create your models here.
class Wallet(models.Model):
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.urlImg}"
    
class AccountTransatcion(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transatcion")
    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    isAddingFunds = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.urlImg}"