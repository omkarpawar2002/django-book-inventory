from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='Sign_In')
def add_book(request):
    form = BookForm()
    if(request.method == 'POST'):
        form = BookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('View_Book')
        else:
            return HttpResponse("Something Wrong While Adding Book!!")
    template_name = 'manage_book/add_book.html'
    context = {'form':form}
    return render(request,template_name,context)

@login_required(login_url='Sign_In')
def view_book(request):
    objs = Book.objects.all()
    template_name = 'manage_book/view_book.html'
    context = {'records':objs}
    return render(request,template_name,context)

def update_book(request,pk):
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if(request.method == 'POST'):
        form = BookForm(request.POST,instance=obj)
        if(form.is_valid):
            form.save()
            return redirect('View_Book')
        else:
            return HttpResponse("Something Wrong While Updating Book!!")
    template_name = 'manage_book/update_book.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_book(request,pk):
    obj = Book.objects.get(id=pk)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('View_Book')
    template_name = 'manage_book/delete_book.html'
    context = {'obj':obj}
    return render(request,template_name,context)

