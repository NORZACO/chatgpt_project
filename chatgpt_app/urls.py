from django.urls import path
from .views.views import home, generate_text_view
from .views.chating import chatingGPT

urlpatterns = [
    path('', home, name='home'),
    path('generate_text/', generate_text_view, name='generate_text'),
    path('chat/', chatingGPT, name='chat'),
]
