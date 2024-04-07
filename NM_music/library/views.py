from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Artist

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'library/artist_list.html', {'artists': artists})
def home(request):
    return render(request, 'library/home.html')
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'library/artist_detail.html', {'artist': artist})
