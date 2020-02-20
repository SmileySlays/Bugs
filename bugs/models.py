from django.db import models
from django.utils import timezone
from customuser.models import MyCustomUser

class Ticket(models.Model):
    CHOICES = [
    ('0', 'New'),
    ('1', 'In Progress'),
    ('2', 'Done'),
    ('3', 'Invalid'),
    ]
    title = models.CharField(max_length=25)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)
    ticket_status = models.CharField(
        max_length=11,
        choices=CHOICES,
        default="New"
    )
    #unique is false so users can have multiple tickets at once
    user_filled = models.ForeignKey(MyCustomUser, unique=False, on_delete=models.CASCADE, related_name='user_filled')
    user_assigned = models.ForeignKey(MyCustomUser, unique=False, on_delete=models.CASCADE, related_name='user_assigned', null=True, blank=True)
    user_completed = models.ForeignKey(MyCustomUser, unique=False, on_delete=models.CASCADE, related_name='user_completed', null=True, blank=True)