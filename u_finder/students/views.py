
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *
from .forms import *
from .filter import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


@login_required(login_url='login')
def home(request):
    user = User.objects.all()
    university = University.objects.all()

    total_users = user.count()
    total_university = university.count()
    context = {
        'total_users': total_users,
        'total_university': total_university,
    }
    return render(request, 'students/home.html', context)


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            em = form.cleaned_data.get('email')

            st = Student(student_id=user, password=password1, email = em)
            st.save()
            messages.success(request, "Account was created for " + user + ".")
            return redirect('login')

    context = {'form': form}
    return render(request, 'students/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect.")

    context = {}
    return render(request, 'students/login.html', context)


def logoutUser(request):
    logout(request)

    return redirect('login')


def userDetail(request, usrn):
    detail = Student.objects.get(student_id=usrn)
    form = DetailsForm(instance=detail)

    if request.method == "POST":
        form = DetailsForm(request.POST, instance=detail)
        if form.is_valid():
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            Email = form.cleaned_data.get('email')
            st_id = form.cleaned_data.get('student_id')
            lvl = form.cleaned_data.get('level')
            deg = form.cleaned_data.get('degree_name')

            Student.objects.filter(student_id=usrn).update(
                first_name=firstName, last_name=lastName, email=Email, student_id=st_id, level=lvl, degree_name=deg)

            return redirect('home')

    context = {'form': form}
    return render(request, 'students/user-detail.html', context)


def finderPage(request):

    university = University.objects.all()

    myFilter = UniversityFilter(request.GET, queryset=university)
    univ = myFilter.qs

    context = {
        'univ': univ,
        'myFilter': myFilter,
    }
    return render(request, 'students/finder.html', context)
