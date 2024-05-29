
from django.urls import path
from .views import Registration,LoginView

urlpatterns=[ 
        path("registration/", Registration.as_view(), name="registion"),
        path("login/", LoginView.as_view(), name="loginview")

]