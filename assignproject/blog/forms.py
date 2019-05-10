from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog #어떤(Blog) 모델을 기반으로 한 입력공간
        fields = ['title', 'body'] # 그 모델 중에서 어떤 항목(title)으로 입력받을건지?