from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.login_url),
    path('home/', v.home_url),
    path("login", v.login_api)
]
