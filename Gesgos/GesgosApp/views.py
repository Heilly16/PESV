from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def paso3(request):
    return render(request, 'paso3.html')
