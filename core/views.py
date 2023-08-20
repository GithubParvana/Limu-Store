from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

# Create your views here.


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact.html')


def home(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)  -> HttpResponse
    # return redirect(reverse('contact')) -> redirect 
    # return JsonResponse(dict(hello='world'))  -> Json data type ile
    return render(request, 'index.html')



def faqs(request):
    return render(request, 'faq.html')


def not_found(request):
    return render(request, '404.html')