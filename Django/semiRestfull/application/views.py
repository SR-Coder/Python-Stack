from django.shortcuts import render, HttpResponse, redirect
from . models import Show
from django.contrib import messages

# Create your views here.
def dispShows(request):
    context = {
        'allShows':Show.objects.all()
    }
    return render(request, 'shows.html', context)

def dispAddShow(request):
    return render(request, 'addshow.html')

def dispOneShow(request, show_id):
    context = {
        'thisShow': Show.objects.get(id=show_id)
    }
    return render(request, 'oneShow.html', context)


def addShow(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    newShow = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc']
    )
    return redirect(f'/shows/{newShow.id}')