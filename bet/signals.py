# signals.py
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from wallet.models import Wallet

@receiver(user_logged_in, sender=get_user_model())
def create_wallet_entry(sender, request, user, **kwargs):
    try: 
        Wallet.objects.create(user=user, quantity=100.0)

    except Exception as ex:
        print(f"Erro ao criar Wallet: {ex}")
        pass
       
