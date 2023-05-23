from django.contrib import admin

from .models import  Tour
from .models import Pack
from .models import Serve
from .models import Gallery
from .models import Book 
from .models import Site
from .models import Serv
from .models import Reservation

admin.site.register(Tour)
admin.site.register(Pack)
admin.site.register(Serve)
admin.site.register(Gallery)
admin.site.register(Book)
admin.site.register(Site)
admin.site.register(Serv)
admin.site.register(Reservation)

