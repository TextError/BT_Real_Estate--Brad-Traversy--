from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def register(request):
  # Register User
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if password match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        # Show error
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        # Check email
        if User.objects.filter(email=email).exists():
          # Show error
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          return

    else:
      # Show error
      messages.error(request, 'Password do not match')
      return redirect('register')

  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Login User
    return
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')