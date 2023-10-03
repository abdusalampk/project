from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . form import Movieform

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def addmovie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        decs = request.POST.get('decs', )
        img = request.FILES['img']
        movie=Movie(name=name,decs=decs,img=img)
        movie.save();
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')