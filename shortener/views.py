from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
import random, string

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        short_url = generate_short_url()
        URL.objects.create(original_url=original_url, short_url=short_url)
        return render(request, 'shortener/home.html', {'short_url': short_url})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
