from django.shortcuts import render
from app1.models import Student,Track
from app1.form import StudentForm,TrackForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    all=Student.objects.all()
    data={'all':all}
    return render(request,'app1/home.html',data)

def home(request):
    return HttpResponse("<h1>ddddddddddddd</h1>")
    
def age(request,id):
    s="<h1>ddddddddddddd</h1>= ",id
    return HttpResponse(s)

def showStudent(request,id):
        st=Student.objects.get(id=id)
        data={'st':st}
        return render(request,'app1/show.html',data)

def addStudent(request):

        if request.method =='POST':
                form=StudentForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect("index")
        else:
                form=StudentForm()
                data={'form':form}
                return render(request,'app1/create.html',data)


def editStudent(request,id):
        st= Student.objects.get(id=id)
        if request.method =='POST':
                form=StudentForm(request.POST ,instance = st)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect("/app1/index")
        else:
                form=StudentForm(instance = st)
                data={'form':form}
                return render(request,'app1/create.html',data)
def delStudent(request,id):
        st= Student.objects.get(id=id)
        st.delete()
        return HttpResponseRedirect("/app1/index")
