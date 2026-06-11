from django.urls import path
from django_distill import distill_path
from pages.views import home

urlpatterns = [
    distill_path('', home, name='home', distill_file='index.html'),
]
