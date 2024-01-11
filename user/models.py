from django.db import models
from wallet.models import Wallet

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=100)
    urlImg = models.CharField(max_length=1000)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    lolPuuid = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.urlImg}"
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userNotification")
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)
    imgIcon = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.message} {self.user} {self.isRead}"