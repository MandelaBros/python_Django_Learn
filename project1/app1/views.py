from django.shortcuts import render
from .models import Aozora
import csv
from django.http import HttpResponse

from .modules.forms import aozoraForm
# Create your views here.

def index(request):
    param = {"message": "app1です"}
    return render(request, 'app1/index.html', param)

def list(request):
    data = Aozora.objects.all()
    params = {'message': '青空文庫一覧', 'data': data}
    return render(request, 'app1/list.html', params)

def csvDownLoad(request):
    response = HttpResponse(content_type='text/csv')
    filename = 'aozoraList.csv'
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    writer = csv.writer(response)
    # ヘッダー出力
    header = ['著者名','著書']
    writer.writerow(header)
    # データ出力
    aozoraData = Aozora.objects.all()
    for data in aozoraData:
        writer.writerow([data.author, data.book])
    return response


# 新規登録フォーム
def showCreateAozoraForm(request):
    #フォームを変数にセット
    form = aozoraForm()
 
    context = {
        'aozoraForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'app1/create.html',context)