from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, EditProfileForm

def index(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('index')

    else:
        form = UserCreationForm()
        profile_form = ProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    
    return render(request, 'registration/register.html', context)

def view_profile(request):
    return render(request, 'authentication/view_profile.html')

def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)

            profile.save()

            return redirect('view_profile')
    else:
        profile_form = EditProfileForm(instance=request.user.profile)

    context = {'profile_form': profile_form}
    
    return render(request, 'authentication/edit_profile.html', context)
