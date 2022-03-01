from django.urls import path
from apphello import views

urlpatterns=[
    path('son/',views.son,name='son'),
]