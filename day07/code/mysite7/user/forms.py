
from django import forms

class MyRegForm(forms.Form):
    #限定username长度必须大于６
    username = forms.CharField(label='用户名：')
    password = forms.CharField(label='密码:')
    password2 = forms.CharField(label='重复密码:')
    #age = forms.IntegerField(label='年龄:')

    def clean_username(self):
        # 限定username长度必须大于６
        uname = self.cleaned_data['username']
        if len(uname) < 6:
            raise forms.ValidationError('用户名太短')
        return uname

    def clean(self):
        #验证密码是否一致，不一致跑出ValidationError异常
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码不一致')
        return self.cleaned_data