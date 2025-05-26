from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("create/",views.create,name="create"),
    path("about/",views.about,name="about"),
    path("update/<int:pk>",views.update,name="update"),
    path("delete/<int:pk>",views.delete,name="delete"),
    path("complete/<int:pk>",views.complete,name="complete"),
    path("completed_tasks/",views.completed_list,name='completed_tasks'),
]