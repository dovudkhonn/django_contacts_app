from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name='add'),
    path("filter/", views.filter_person, name='filter_person'),
    path("delete/", views. delete_person, name='delete_person'),
    # path('', views.filter_contacts, name='filter_contacts')
    # path("", DeleteUser.as_view(), name="index"),
]
