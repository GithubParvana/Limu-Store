from django.shortcuts import render

# Create your views here.

def login_register_page(request):
    return render(request, 'login-register.html')



def profiles(request):
    return render(request, 'user-profile.html')