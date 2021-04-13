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


def deletelist(request,commonid):
    if request.method == 'POST':
        TodoModel.objects.get(id=commonid).delete()
        return redirect('home')

def update(request,commonid):
    modelobj = TodoModel.objects.get(id=commonid)
    formobj = TodoForm(instance=modelobj)

    if request.method == 'POST':
        variable=TodoForm(request.POST,instance=modelobj)
        if variable.is_valid():
            variable.save()
            return redirect('home')   
     
    return render(request,'update.html',{'formobj':formobj})
    

    
