from django.shortcuts import render
from app4.forms import UserInfoForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def  index(request):
    return render(request, 'app4_temp/index.html')

# @login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")
# TO VISIT SPECIAL PAGE EITHER ACCESS FROM ADMIN SITE PAGE(type special after next in place of admin in address bar) OR AFTER LOGGING IN FROM HOME PAGE TYPE /SPECIAL IN ADDRESS BAR OR SWITCH OFF @login_reqiuired


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):
     registered = False

     if request.method == 'POST':
         admi_form = UserInfoForm(data=request.POST)
         profile_form = UserProfileInfoForm(data=request.POST)

         if admi_form.is_valid() and profile_form.is_valid():
             admi = admi_form.save()

            # Hash the password
             admi.set_password(admi.password)

            # Update with Hashed password
             admi.save()


             profile = profile_form.save(commit=False)

             # Set One to One relationship between
             # UserInfoForm and UserProfileInfoForm
             profile.admi = admi

             if 'profile_pic' in request.FILES:
                 profile.profile_pic = request.FILES['profile_pic']

             profile.save()

             registered = True

         else:
             print(admi_form.errors, profile_form.errors)

     else:
         admi_form = UserInfoForm()
         profile_form = UserProfileInfoForm()

     return render(request, 'app4_temp/registration.html',{'admi_form': admi_form, 'profile_form':profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        admi2 = authenticate(username=username, password=password)

        # If we have a user
        if admi2:
            #Check it the account is active
            if admi2.is_active:
                # Log the user in.
                login(request,admi2)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'app4_temp/login.html', {})
