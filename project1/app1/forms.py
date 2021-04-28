from django import forms
from . models import Aozora

class aozoraForm(forms.ModelForm):
    class Meta:
        model = Aozora
        fields = ('ind', 'author','book','cmt')
        labels={
           'ind':'インデックス',
           'author':'著者名',
           'book':'著書',
           'cmt':'コメント',
           }