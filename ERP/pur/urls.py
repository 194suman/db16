

from django.urls import path,include
from pur.views import index_view

urlpatterns = [
    path('index/', index_view),
]
