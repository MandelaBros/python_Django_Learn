from django.shortcuts import render

# Create your views here.

def index(request):
    param = {"message": "app2です"}
    return render(request, 'app2/index.html', param)