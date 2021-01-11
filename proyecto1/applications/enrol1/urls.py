from django.contrib import admin
from django.urls import path
from applications.enrol1 import views

from .import views

urlpatterns = [
    path(
        '',
        views.add_show,
        name="addandshow"),
    path(
        '<int:id>',
        views.update_data,
        name="updatedata"
    ),
    path(
        'delete/<int:id>',
        views.delete_data,
        name="delete"
    ),
]
