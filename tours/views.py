from django.views.generic import ListView
from .models import Tour

class HomePageView(ListView):
    model = Tour
    template_name = "index.html"