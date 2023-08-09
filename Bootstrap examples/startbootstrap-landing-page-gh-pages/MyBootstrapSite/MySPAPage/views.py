from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def inicio(request):
    print('Request for index page received')
    return render(request, 'MySPAPage/index.html')