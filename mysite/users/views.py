from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .forms import LoginForm,RegisterForm
# Create your views here.

class Mybackend(ModelBackend):
    #邮箱登录注册
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
def login_view(request):
    # if request.method == 'POST':
    #
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #
    #         return HttpResponse('登录成功')
    #     else:
    #
    #         return HttpResponse('登录失败')
    if request.method != "POST":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponse('登录成功')
                return redirect('/admin')
            else:
                return HttpResponse('登录失败')
    context = {'form': form}

    return render(request, 'users/login.html',context)
def register(request):
    #注册视图
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.username = form.cleaned_data.get('email')
            new_user.save()
            return HttpResponse('注册成功')

    context = {'form': form}
    return render(request, 'users/register.html',context)
