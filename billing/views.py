from django.shortcuts import render,redirect,get_object_or_404
from .models import ModelWala
from .forms import FormWala

def home(request):
    return render(request,'base.html')
def insert(request):
    if request.method=="POST":
        form=FormWala(request.POST)
        if form.is_valid():
            form.save()
            redirect('/display/')
    else:
        form=FormWala()
    return render(request,'insert.html',{'form':form})
def delete(request,emp_no):
    obj=get_object_or_404(ModelWala, emp_no=emp_no)
    obj.delete()
    return redirect('/display/')
def search(request):
    if request.method=="POST":
        eno=int(request.POST.get('emp_no'))
        obj=get_object_or_404(ModelWala,emp_no=eno)
        return render(request,'print.html',{'ob':obj})
    return render(request,'search.html')
def update(request,emp_no):
    if request.method=="POST":
        obj=get_object_or_404(ModelWala,emp_no=emp_no)
        obj.emp_name=request.POST.get('emp_name')
        obj.save()
        return render(request,'print.html',{'ob':obj})
    return render(request,'update.html')
def display(request):
    obj=ModelWala.objects.all()
    return render(request,'display.html',{'obj':obj})
    

        
    
    
