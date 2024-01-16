from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet

class WalletQuantityAPIView(APIView):
    def get(self, request, user_id):
        try:
            wallet = Wallet.objects.get(user_id=user_id)
            return Response({'quantity': wallet.quantity})
        except Wallet.DoesNotExist:
            return Response({'error': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)

def render_view_wallet(request):
    #Wallet details
    return render(request, 'wallet.html')