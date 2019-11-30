from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name=''),
    path('<slug:slug>', views.article, name='article'),
    path('category/<slug:slug>', views.category, name='category')
]
