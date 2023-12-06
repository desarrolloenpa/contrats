from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):
    request.session["province_id"] = 3
    return render(request, 'index.html', {'title_page': "INICIO"})