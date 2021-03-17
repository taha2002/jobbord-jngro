
from django.shortcuts import redirect, render
from .forms import Singup_form , pro_edit , us_edit
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
# Create your views here.

def signup(request):
    if request.method=="POST":
        form = Singup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = Singup_form()
    return render(request,'registration/signup.html',{'form':form})



def profile_h(request):

    profile_data = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile':profile_data })


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    msg = ''
    if request.method == 'POST':
        form_profile = pro_edit(request.POST , request.FILES ,instance=profile)
        form_user = us_edit(request.POST , instance=request.user)
        if form_profile.is_valid() and form_user.is_valid():
            form_user.save()
            form_data = form_profile.save(commit=False)
            form_data.user = request.user
            form_data.save()
        return redirect(reverse('account:profile'))

    else:
        form_profile = pro_edit(instance=profile)
        form_user = us_edit(instance=request.user)
    return render(request, 'accounts/profile_edit.html', { 'form_u':form_user , 'form_p':form_profile,'msg':msg} )
