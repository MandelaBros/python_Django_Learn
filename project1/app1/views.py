from django.shortcuts import render
from .models import Member
# Create your views here.

def index(request):
    param = {"message": "app1です"}
    return render(request, 'app1/index.html', param)

def list(request):
    data = Member.objects.all()
    params = {'message': 'メンバーの一覧', 'data': data}
    return render(request, 'app1/list.html', params)
