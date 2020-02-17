from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# def indexView(request):
#     # return HttpResponse("<h1>login pagce</h1>") 
#     return redirect("home")
# def loginView(request):
#     # return HttpResponse("<h1>login pagce</h1>") 
#     return redirect("login")


def indexView(request):
    return render(request,'dashbord/index.html')

@login_required
def dashView(request):
    return render(request,'dashbord/dash.html')

def regesterView(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=UserCreationForm()

    return render (request,'registration/register.html',{'form':form})