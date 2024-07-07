from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32,widget=forms.TextInput(attrs={'class':'input','placeholder':'Username/mail'}))
    password = forms.CharField(label='password', min_length=6,widget=forms.PasswordInput(attrs={'class':'input','placeholder':'password'}))
    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')
        if username == password:
            raise forms.ValidationError('用户名与密码不能相同')
        return password

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', max_length=32,widget=forms.EmailInput(attrs={'class':'input','placeholder':'邮箱'}))
    password = forms.CharField(label='password', min_length=6,widget=forms.PasswordInput(attrs={'class':'input','placeholder':'password'}))
    repassword = forms.CharField(label='repassword', min_length=6,widget=forms.PasswordInput(attrs={'class':'input','placeholder':'password'}))

    class Meta:
        model = User
        fields = ('email','password')
    def clean_emailname(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已存在')
        return email
    def clean_repassword(self):
        #验证密码是否相等
        if self.cleaned_data.get('password') != self.cleaned_data.get('repassword'):
            raise forms.ValidationError('两次密码输入不一样')
        return self.cleaned_data.get('repassword')

