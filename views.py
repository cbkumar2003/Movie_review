from django.shortcuts import render,redirect
from .forms import *
from .models import *

def Movies(request): 
    details ={
    'movies_form': Movies_Form
    }
    if request.method == 'POST':
        movies_form = Movies_Form(request.POST) 
        if movies_form.is_valid():
            movies_form.save() 
            return redirect('/movie/')
    else:
        movies_form = Movies_Form
    return render(request, 'home.html',details)


def MoviesList(request):
    movies =  todoitem_movie.objects.all()
    return render(request, 'movielist.html', {'movies': movies})


def deletemovies(request,id):
    selected_movie = todoitem_movie.objects.get(id=id)
    selected_movie.delete()
    return redirect('/movie/')

def updatemovies(request,id):
    
    selected_movie = todoitem_movie.objects.get(id=id)
    context={
        'movies_form' : Movies_Form(instance = selected_movie)
    }
    if request.method == "POST":
        movies_form =  Movies_Form(request.POST,instance = selected_movie)
        if movies_form.is_valid():
           movies_form.save()
        return redirect('/movie/')
    return render(request,'home.html',context)


