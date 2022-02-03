from django.urls import path
from . import views

urlpatterns =[
    path('',views.getRoutes,name="routes"),
    path('notes/',views.getNotes,name="notes"),
    path('notes/create/',views.create,name="create"),
    path('notes/last/',views.getLastObject,name="getlastobject"),
    path('notes/<str:pk>/',views.getNote,name="note"),
    path('notes/<str:pk>/update/',views.update,name="update"),
    path('notes/<str:pk>/delete/',views.delete,name="delete"),

   
]
