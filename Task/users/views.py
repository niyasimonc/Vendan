from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            custom_user = CustomUser.objects.create(user=user)
            custom_user.save()
            login(request, user)
            return HttpResponseRedirect(reverse
                                        ('home'))
    else:
        form = UserCreationForm()
    return render(request, 'users/sign_up.html', {'form': form})
