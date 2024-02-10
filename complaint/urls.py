from django.urls import path
from complaint import views


urlpatterns = [
    path("complaint/",views.complaint,name='complaint'),
    path("add_complaint/",views.add_complaint,name='add_complaint'),
    path("complaints/",views.complaints,name='complaints'),
    path("cancel/<int:id>/",views.cancel,name='cancel'),
]