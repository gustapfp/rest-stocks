from django.urls import path
from stocks.views import index

urlpatterns = [
    path('', index, name='index')
]