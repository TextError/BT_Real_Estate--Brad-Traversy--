from django.shortcuts import render, redirect
from django.contrib import messages, auth
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
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Login after register
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
          user.save()
          messages.success(request, 'Registered successfull')
          return redirect('login')

    else:
      # Show error
      messages.error(request, 'Password do not match')
      return redirect('register')

  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Login User
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    # Check User
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')