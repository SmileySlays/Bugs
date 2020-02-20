from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from customuser.models import MyCustomUser
from bugs.models import Ticket
