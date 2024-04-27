from django.urls import path
from iphone.views import iphone

urlpatterns = [
    path('iphone', iphone),
]
