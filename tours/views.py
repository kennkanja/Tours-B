from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

from .forms import ReservationForm
from .models import Reservation, Tour
from .models import Pack
from .models import Serve
from .models import Serv
from .models import Gallery
from .models import Book
from .models import Site
from .models import  Term

class HomePageView(ListView):
    model = Tour
    template_name = "index.html"

class PackPageView(ListView):
    model = Pack
    template_name = "packages.html"

class ServePageView(ListView):
    model = Serve
    template_name = "services.html"

class ServPageView(ListView):
    model = Serv
    template_name = "services.html"

class BookPageView(ListView):
    model = Book
    template_name = "book.html"

class SitePageView(ListView):
    model = Site
    template_name = "index.html"

class GalleryPageView(ListView):
    model = Gallery
    template_name = "gallery.html"

class ReservationPageView(ListView):
    model = Reservation
    template_name = "reservations.html"

class TermPageView(ListView):
    model = Term
    template_name = "term.html"

class CreateTourView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation_form.html"
    success_url = reverse_lazy("home")
