

from django.urls import path,include
from sales.views import index_view

urlpatterns = [
    path('index/', index_view),
]
