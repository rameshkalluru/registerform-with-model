from django.urls import path
from ramya import views

urlpatterns=[
    path('lovely/',views.lovely,name='lovely'),
]