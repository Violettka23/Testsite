from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('about_us', views.about_us)

]
