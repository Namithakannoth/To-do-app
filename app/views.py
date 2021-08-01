from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from app.models import Todo

# Create your views here.
@login_required
def CollectTask(request):
    if request.method=="POST":
        mytask=request.POST.get("mytask")
        t=Todo(task=mytask)
        t.save()

    all_todos=Todo.objects.all()
    context={
        'all_todos':all_todos
    }
    return render(request,"todo.html",context)


def DeleteOneTask(request,id):
    onetodo=Todo.objects.get(id=id)
    onetodo.delete()
    return redirect("/task")

def home(request):
    return render(request,"home.html")


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, "signup.html", context)

@login_required
def logout(request):
    return render(request,"logout.html")