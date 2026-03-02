from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

def sign_up(request):
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('Sign_In')
        else:
            return HttpResponse("Error Occur While Registering!!")
    template_name = 'auth_book/sign_up.html'
    context = {'form':form}
    return render(request,template_name,context)

def sign_in(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('View_Book')
        else:
            return redirect('Sign_Up')
    template_name = 'auth_book/sign_in.html'
    context = {}
    return render(request,template_name,context)

def sign_out(request):
    logout(request)
    return redirect('Sign_In')