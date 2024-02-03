from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    mycontext = {
            'movies':['Top Gun','Spirited Away',' Spider Man'],
            'pageTitle':"Movie App"
    }
    return render(request, 'movie_app/index.html',mycontext)

def about(request):
    aboutContext ={
        'pageTitle':'About Me'
    }
    return render(request, 'movie_app/about.html',aboutContext)

# how templates work:
# app/templates/app/index.html