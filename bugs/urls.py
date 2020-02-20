"""bugs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bugs.models import Ticket
from bugs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.home, name='home'),
    path('', include('authorization.urls')),
    path('ticketadd/', views.ticket_add_view, name="ticketadd"),
    path("user/<str:user>", views.users, name='users'),
    path('complete/<pk>/', views.ticket_complete, name="ticketcomplete"),
    path('ticketedit/<pk>/', views.ticket_edit_view, name="ticketedit"),
    path('completed/<str:user>', views.users_completed, name="assigned"),
    path('assigned/<str:user>', views.users_assigned, name="assigned"),
    path('details/<pk>', views.details, name="details")
]