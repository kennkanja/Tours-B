from django.contrib import admin

from .models import  Tour
from .models import Pack
from .models import Serve
from .models import Gallery
from .models import Book 

admin.site.register(Tour)
admin.site.register(Pack)
admin.site.register(Serve)
admin.site.register(Gallery)
admin.site.register(Book)
