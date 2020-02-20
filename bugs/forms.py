from django import forms
from customuser.models import MyCustomUser

class TicketAddForm(forms.Form):
    title = forms.CharField(max_length=25)
    description = forms.CharField(max_length=250)
    choices = [
        ('0', 'New'),
        ('1', 'In Progress'),
        ('2', 'Done'),
        ('3', 'Invalid')
    ]
    ticket_status = forms.ChoiceField(
        choices=choices
    )
    user_assigned = forms.ModelChoiceField(queryset=MyCustomUser.objects.all(), required=False)

class TicketEditForm(forms.Form):
    title = forms.CharField(max_length=25, required=False)
    description = forms.CharField(max_length=250, required=False)
    choices = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]
    ticket_status = forms.ChoiceField(
        choices=choices
    )
    user_assigned = forms.ModelChoiceField(queryset=MyCustomUser.objects.all(), required=False)
    