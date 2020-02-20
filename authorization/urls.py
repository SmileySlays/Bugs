from django.urls import path
import authorization.views

urlpatterns = [
    path("", authorization.views.login_view, name="login")
]