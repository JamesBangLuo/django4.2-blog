from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32)
    password = forms.CharField(label='密码', min_length=6,widget=forms.PasswordInput())