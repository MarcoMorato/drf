from django.urls import path, include, re_path
from .views import *

from rest_framework import routers
# routers.SimpleRouter
# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')
# print(router.urls)

urlpatterns = [
    path('api/v1/women/', WomenApiList.as_view()),
    path('api/v1/women/<int:pk>/', WomenApiUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenApiDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/', include(router.urls)),

    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update', 'delete': 'destroy'})),

    # path('api/v1/womenlist/', WomenApiList.as_view()),
    # path('api/v1/womenlist/<int:pk>', WomenApiUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>', WomenApiDetailView.as_view()),

]
