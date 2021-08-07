from django.shortcuts import render
from .models import BasicForm
from .forms import BasicF


# Create your views here.
def home(request):
    form = BasicF()
    context = {
        'form':form
    }
    if request.method=='POST':
        if form.is_valid():
            BasicForm.objects.create(title=request.POST['title'],username=request.POST['username'],realtext=request.POST['realtext'])
        else:
            BasicForm.objects.create(title=request.POST['title'],username=request.POST['username'],realtext=request.POST['realtext'])    
        return render(request,'myeditor/home.html',context)
    return render(request,'myeditor/home.html',context)

def disdata(request):
    data = BasicForm.objects.all()
    return render(request,'myeditor/disdata.html',{'data':data})