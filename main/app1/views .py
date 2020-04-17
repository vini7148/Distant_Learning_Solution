from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import regis
from .models import info

# Create your views here.
def handler400(request, *args, **argv):
    response = render(
        request,
        'app1/400.html',
        {
            'title': "400 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 400
    return response

def handler404(request, *args, **argv):
    response = render(
        request,
        'app1/404.html',
        {
            'title': "404 Not found",
            'year':datetime.now().year,
        }
    )
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(
        request,
        'app1/500.html',
        {
            'title': "500 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 500
    return response

def handler503(request, *args, **argv):
    response = render(
        request,
        'app1/503.html',
        {
            'title': "503 Error",
            'year':datetime.now().year,
        }
    )
    response.status_code = 503
    return response


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app1/index.html',
        {
            'title': "Home Page",
            'year':datetime.now().year,
        }
    )

def register(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = regis(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # login(request, user)
            messages.info(request, f"Login as {username}")
            return redirect("app1:log_page")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(
                request,
                "app1/register.html",
                {
                    'title': "Registeration Page",
                    'year': datetime.now().year,
                    'form': form
                }
            )

    # form = UserCreationForm
    form = regis
    return render(
        request,
        "app1/register.html",
        {
            'title': "Registeration Page",
            'year': datetime.now().year,
            'form': form
        }
    )


def login_re(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request,
        "app1/login.html",
        {
            'title': "Login Page",
            'year': datetime.now().year,
            'form': form
        }
    )

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("app1:Home")

def ur(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        username = request.user.username
        return render(
            request,
            'app1/user.html',
            {
                'title': request.user.first_name + " " + request.user.last_name,
                'usr': username,
                'year': datetime.now().year,
            }
        )

    else:
        return redirect("app1:Home")

def stu(request):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        username = request.user.username
        return render(
            request,
            'app1/study.html',
            {
                'title': "Source",
                'tut': info.objects.all,
                'year': datetime.now().year,
            }
        )

    else:
        return redirect("app1:Home")

def slug(request, single_slug):
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        username = request.user.username
        datas = info.objects.get(id=single_slug)
        print(datas)
        return render(
            request,
            'app1/info.html',
            {
                'title': datas.Course_Name,
                'tut': datas,
                'year': datetime.now().year,
            }
        )

    else:
        return redirect("app1:Home")
