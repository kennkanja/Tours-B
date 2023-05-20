from django.urls import path
from .views import HomePageView,CreateTourView,PackPageView

urlpatterns =[
    path("", HomePageView.as_view(), name="home"),
    path("packages/", PackPageView.as_view(), name="packages"),
    path("post/",CreateTourView.as_view(), name="add_post")
]