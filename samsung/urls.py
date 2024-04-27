from django.urls import path
from samsung.views import samsung

urlpatterns = [
    path('samsung', samsung)
]
