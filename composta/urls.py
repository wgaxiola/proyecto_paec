from django.urls import path
from . import views

urlpatterns = {
    path('', views.inicio, name='inicio'),
    path('que-es/', views.que_es, name='que_es'),
    path('como-hacer/',views.como_hacer, name='como_hacer'),
}