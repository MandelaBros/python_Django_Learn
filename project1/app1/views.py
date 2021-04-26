from django.shortcuts import render
from .models import Aozora
# Create your views here.

def index(request):
    param = {"message": "app1です"}
    return render(request, 'app1/index.html', param)

def list(request):
    data = Aozora.objects.all()
    params = {'message': '青空文庫一覧', 'data': data}
    return render(request, 'app1/list.html', params)
