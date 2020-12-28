from django.urls import path
from . import views

app_name = 'summary'

urlpatterns = [
    # path('design/', views.design, name='design'),
    path('', views.base, name='base'),
]
