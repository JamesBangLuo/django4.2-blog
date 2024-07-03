from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    password = forms.CharField(label='password', min_length=6,widget=forms.PasswordInput())
    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')
        if username == password:
            raise forms.ValidationError('用户名与密码不能相同')
        return password