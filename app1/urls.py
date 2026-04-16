
from django.urls import path
from . import views

urlpatterns = [
    # path('ut/', views.ut, name='ut'),
    path('', views.index, name='home'),
]