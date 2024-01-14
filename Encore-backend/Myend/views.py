from django.shortcuts import render, http404
def index(request):
    return render(request, "index.html")
# Create your views here.
