

from django.urls import path,include
from accounting.views import index_view

urlpatterns = [
    path('index/', index_view),
]
