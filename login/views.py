from django.shortcuts import render

# Create your views here.
def render_view_login(request):
    return render(request, 'login.html')


def render_view_register(request):
    return render(request, 'register.html')

def render_view_forgot_password(request):
    return render(request, 'forgot-password.html')