from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def paso1(request):
    return render(request, 'paso1.html')
