# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, arunabPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('arunab/', arunabPageView, name='arunab'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
