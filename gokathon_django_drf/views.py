from django.shortcuts import render


def index(request):
    return render(request, 'ClassRecode_Web2/static/views/index.html')