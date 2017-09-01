from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def home(request):
    return render(request,'app1/home.html')


def tips(request):
    tips=models.tips.objects.filter(type=0)
    return render(request, 'app1/tips.html',{'tips':tips})
def tips_done(request):
    tips = models.tips.objects.filter(type=1)
    return render(request, 'app1/tips_done.html',{'tips':tips})
def new(request):
    return render(request,'app1/new.html')

def del_action(request):
    del_id=request.POST.get('del_id')
    tip=models.tips.objects.get(pk=del_id)
    tip.delete()
    tips = models.tips.objects.filter(type=1)
    return render(request,'app1/tips_done.html',{'tips':tips})
def del_action1(request):
    id=request.POST.get('del_id')
    t=models.tips.objects.get(pk=id)
    t.delete()
    tips = models.tips.objects.filter(type=0)
    return render(request, 'app1/tips.html', {'tips': tips})
def done_action(request):
    id=request.POST.get('done_id')
    t=models.tips.objects.get(pk=id)
    t.type=1
    t.save()
    tips = models.tips.objects.filter(type=0)
    return render(request, 'app1/tips.html', {'tips': tips})
def add_action(request):
    title=request.POST.get('title')
    content=request.POST.get('content')
    level=request.POST.get('level')
    type=request.POST.get('type')
    models.tips.objects.create(title=title,content=content,level=level,type=type)

    return render(request, 'app1/new.html')
