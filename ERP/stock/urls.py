

from django.urls import path,include
from stock.views import index_view

urlpatterns = [
    path('index/', index_view),
]
