from django.urls import path
from . import views


app_name = "contact"

urlpatterns = [

    path("", views.contact_view, name="contact_view"),
    path("message/", views.message_view, name="message_view"),

]