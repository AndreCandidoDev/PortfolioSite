from django.urls import path
from .views import curriculo


urlpatterns = [
    path('curriculo/', curriculo, name='curriculo_dev')
]