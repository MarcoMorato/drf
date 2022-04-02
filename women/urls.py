from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/womenlist/', WomenApiView.as_view())
]
