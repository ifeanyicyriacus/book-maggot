from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_books(request):
    return HttpResponse("Hello, world. You're at the books page.")

def greet(request, name):
    return render(request, template_name='index.html', context={'name':name})