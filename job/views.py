from django.shortcuts import render , redirect
from .models import job 
from django.core.paginator import Paginator
from .forms import apply , add
from django.urls import reverse

# Create your views here.

def job_list (request):
    job_list = job.objects.all()
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs' : page_obj ,
    }
    return render(request, 'job/job_list.html', context)


def job_delail(request, slug):
    job_delail = job.objects.get(slug=slug)
    
    if request.method == 'POST' :
        form = apply(request.POST , request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.job = job_delail
            data.save()
    else :
        form = apply()


    context = {
        'job' : job_delail , 'forms' : form ,
    }
    return render(request, 'job/job_detail.html' , context)

def add_job (request):

    if request.method == 'POST':
        form = add(request.POST , request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            return redirect(reverse('jobs:job_list'))
    else :
        form = add()
    
    context = {
        'form': form 
    }
    return render(request, 'job/add_job.html', context)