from django.shortcuts import render,redirect
from django.views import View
from .models import jobnew
from .forms import AddJobForm
# Create your views here.

class Home(View):
    def get(self,request):
        job_data = jobnew.objects.all()
        return render(request, 'core/home.html',{'jobdata':job_data})
    
class Add_job(View):
    def get(self,request):
        fm = AddJobForm()
        return render(request, 'core/add-job.html',{'form':fm})
       

    def post(self,request):
        fm = AddJobForm(request.POST)
        print(fm)
        if fm .is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-job.html',{'form':fm})
class Delete_job(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        jobdata = jobnew.objects.get(id = id)
        jobdata.delete()
        return redirect('/')
    
class EditJob(View):
    def get(self, request, id):
        jo = jobnew.objects.get(id=id)
        fm = AddJobForm(instance=jo)
        return render(request, 'core/edit-job.html',{'form':fm})
    def post(self, request, id):
        jo = jobnew.objects.get(id=id)
        fm = AddJobForm(request.POST, instance=jo)
        if fm.is_valid():
            fm.save()
            return redirect('/')
