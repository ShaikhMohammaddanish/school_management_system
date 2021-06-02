from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


@login_required
def home_page(request):
    return render(request, 'index.html')


def signout(request):
    logout(request)
    return redirect('login')



def register(request):
    return HttpResponse('hello')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)
        print(password)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'message':'invalid credentials !'})
    return render(request, 'login.html')



from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Have been Created Successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    page_title = request.user
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your Account Have Been Updated!')
            return redirect('/profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
    context = {
        'p_form': p_form,
        'title': page_title
    }
    return render(request, 'profile.html', context)

# @login_required
# def view_profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'users/user_profile.html', {"user":user})