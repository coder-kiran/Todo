from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import TodoModel
# Create your views here.


def index(request):
    formobj = TodoForm()
    modelobject = TodoModel.objects.all()
    if request.method == 'POST':
        variable = TodoForm(request.POST)
        if variable.is_valid():
            variable.save()
            return redirect('home')         

    return render(request,'home.html',{'formkey':formobj,'modelobjectkey':modelobject})

def update(request,commonid):
    