"""
URL configuration for bongobet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bet.views import render_view_index
from bet.views import render_view_bet_lol
from bet.views import bet_view
from login.views import render_view_login
from login.views import render_view_register
from login.views import render_view_forgot_password
from django.urls import include
from wallet.views import WalletQuantityAPIView
from wallet.views import render_view_wallet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', render_view_index, name='render_view_index'),
    path('lolbet/', render_view_bet_lol, name='lolbet'),
    path('login/', render_view_login, name='render_view_login'),
    path('register/', render_view_register, name='render_view_register'),
    path('forgot-password/', render_view_forgot_password, name='render_view_forgot_password'),
    path('accounts/', include('allauth.urls')),
    path('api/wallet/<int:user_id>/', WalletQuantityAPIView.as_view(), name='wallet_quantity_api'),
    path('bet/', bet_view, name='bet'),
    path('wallet/', render_view_wallet, name='wallet'),
]

