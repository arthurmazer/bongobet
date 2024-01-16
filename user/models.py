from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)
    imgIcon = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.message}{self.isRead}"