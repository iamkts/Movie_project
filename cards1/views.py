from django.shortcuts import render
from cards1.models import Movie
from cards1.forms import movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

'''def home(request):
    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})'''

class MovieList(ListView):       #Listview displays all objects/records retrieving from a model
    model = Movie
    template_name = "home.html"
    context_object_name = "m"

'''def add(request):
    if(request.method=="POST"):
        form=movieform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    form=movieform()
    return render(request,'add.html',{'form':form})'''

class Movieadd(CreateView):   #createview displays a form for adding new object and handles form submission
    model = Movie
    template_name = "add.html"
    fields = '__all__'
    success_url = reverse_lazy('cards1:home')



'''def view(request,p):
    m=Movie.objects.get(id=p)
    return render(request,'view.html',{'m':m})'''

class MovieDetail(DetailView):  #displays particular obj retrieving from a model
    model = Movie
    template_name = 'view.html'
    context_object_name = "m"

'''def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return home(request)'''

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('cards1:home')
    template_name = "delete.html"

'''def update(request,p):
    m = Movie.objects.get(id=p)
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)

    form=movieform(instance=m)

    return render(request,'update.html',{'form':form})'''

class MovieUpdate(UpdateView):
    model = Movie
    template_name = "update.html"
    fields = '__all__'
    success_url = reverse_lazy('cards1:home')


