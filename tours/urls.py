from django.urls import path
from .views import BookPageView, HomePageView,CreateTourView,PackPageView, ReservationPageView, ServPageView,ServePageView,GalleryPageView, SitePageView

urlpatterns =[
    path("", HomePageView.as_view(), name="home"),
    path("packages/", PackPageView.as_view(), name="packages"),
    path("services/", ServePageView.as_view(), name="services"),
    path("gallery/", GalleryPageView.as_view(), name="gallery"),
    path("book/", BookPageView.as_view(), name="book"),
    path("sites/", SitePageView.as_view(), name="sites"),
    path("reservation/", ReservationPageView.as_view(), name="reservation"),
    path("term/", ReservationPageView.as_view(), name="term"),
    path("post/",CreateTourView.as_view(), name="add_post")
]