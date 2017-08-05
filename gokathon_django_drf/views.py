from django.shortcuts import render


def index(request):
    return render(request, 'real/static/views/index.html')