from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from userauths.models import User, Profile
from userauths.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from core.models import FriendRequest, Post



def RegisterView(request):
    # check whether user already logged in
    if request.user.is_authenticated:
        messages.warning(request, "You are registered")
    # send them back to homepage from urls.py
        return redirect("core:feed")
    
    # if user is not registered, then we create form
    # request.POST is a storage function capture user input then store in form, input from index.html
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    # get info from form then assign to variable
        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)    
    # if everything is checked, then log user in
        login(request, user)        
        messages.success(request, f"Hi {full_name}. Your account has been created successfully")        
    # get profile of the logged in user
        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        # save form
        profile.save() 
        messages.success(request, f"Hi {full_name}. Your account has been created successfully")        
        return redirect("core:feed")
    
    context = {
    # pass in key value "form" to call form
        "form":form 
    }
    return render(request, "userauths/sign-up.html", context)
        
def LoginView(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are registered")
    # send them back to homepage from urls.py
        return redirect("core:feed")
    #if is existing user, get info from database
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try: # check in database if user is authenticated
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("core:feed")
            else: 
                messages.error(request, "Username or Password does not exist")
                return redirect("userauths:sign-up")
        except:
            messages.error(request, "Username does not exist")
            return redirect("userauths:sign-up")
            
    return HttpResponseRedirect("/")

def LogoutView(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect("userauths:sign-up")

@login_required
def my_profile(request):
    profile = request.user.profile
    posts = Post.objects.filter(active=True, user=request.user)

    context = {
        "posts":posts,
        "profile":profile,
    }
    return render(request, "userauths/my-profile.html", context)

@login_required
def friend_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.user.profile == profile:
        return redirect("userauths:my-profile")
    posts = Post.objects.filter(active=True, user=profile.user)
    # Send Friend Request Feature
    bool = False
    bool_friend = False

    sender = request.user #is the logged in user 
    receiver = profile.user
    bool_friend = False
    print("========================  Add or cancel")
    try:
        friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver)
        if friend_request:
            bool = True
        else:
            bool = False
    except:
        bool = False
    # if receiver not in sender.profile.friends.all():
    #     pass
    # else:
    #     print("========================  Unfriend")
    #     bool_friend = False

    # End Send Friend Request Feature
    print("Bool =======================", bool)
    

    context = {
        "posts":posts,
        "bool_friend":bool_friend,
        "bool":bool,
        "profile":profile,
    }
    return render(request, "userauths/friend-profile.html", context)

@login_required
def profile_update(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "Profile Updated Successfully.")
            return redirect('userauths:profile-update')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, 'userauths/profile-update.html', context)