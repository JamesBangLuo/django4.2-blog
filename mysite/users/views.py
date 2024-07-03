from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
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
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
    context = {'form': form}

    return render(request, 'users/login.html',context)