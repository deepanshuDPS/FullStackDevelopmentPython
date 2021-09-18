from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# for login and logout
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # setting the password using hashing algorithms we declare in settings.py
            user.set_password(user.password)
            user.save()

            # don't want to commit database yet so commit = False
            profile = profile_form.save(commit = False)
            # after adding user attribute we save to database
            profile.user = user

            # checking for file type with model field then save
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered})
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') # key is the name = '' attribute in input types in html
        password = request.POST.get('password')

        user = authenticate(username=username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index')) # redirect user after login to home
            else:
                return HttpResponse("Account Not Active")
        else:
            print('Someone tried to login and failed!')
            print('Username:{} and password {}'.format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'basic_app/login.html',{})
