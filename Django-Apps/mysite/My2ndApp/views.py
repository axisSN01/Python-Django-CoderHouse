from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse("Hello, world. You're at My2ndApp index.")

class IndexView(generic.DetailView):
    template_name = "My2ndApp/index.html"