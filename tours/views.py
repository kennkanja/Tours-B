from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

from .forms import TourForm
from .models import Tour
from .models import Pack
from .models import Serve
from .models import Gallery
from .models import Book

class HomePageView(ListView):
    model = Tour
    template_name = "index.html"

class PackPageView(ListView):
    model = Pack
    template_name = "packages.html"

class ServePageView(ListView):
    model = Serve
    template_name = "services.html"

class BookPageView(ListView):
    model = Book
    template_name = "book.html"

class GalleryPageView(ListView):
    model = Gallery
    template_name = "gallery.html"

class CreateTourView(CreateView):
    model = Tour
    form_class = TourForm
    template_name = "reservation.html"
    success_url = reverse_lazy("home")
