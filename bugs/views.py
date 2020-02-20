from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from bugs.models import Ticket
from bugs.forms import TicketAddForm, TicketEditForm
from customuser.models import MyCustomUser

@login_required()
def home(request):
    items = Ticket.objects.order_by("-ticket_status")
    return render(request, "home.html", {"data": items})

@login_required
def details(request, pk):
    return render(request, "details.html", {"tickets": Ticket.objects.get(pk=pk)})

@login_required()
def users(request, user):
    users = MyCustomUser.objects.get(username=user)
    tickets = [ticket for ticket in Ticket.objects.all() if ticket.user_assigned == users]
    tickets_assigned = [ticket for ticket in Ticket.objects.all() if ticket.user_assigned == users]
    tickets_completed = [ticket for ticket in Ticket.objects.all() if ticket.user_assigned == users]
    return render(request, "users.html", 
                    {"tickets": tickets,
                    "tickets_assigned": tickets_assigned,
                    "tickets_completed": tickets_completed,
                    "users": users})

@login_required()
def other_users_tickets(request, user):
    users = MyCustomUser.objects.get(username=user)
    tickets = [ticket for ticket in Ticket.objects.all() if ticket.user_assigned == users]
    print(tickets)
    return render(request, "sorted.html", 
                    {"tickets": tickets,
                    "users": users})

@login_required()
def users_completed(request, user):
    users = MyCustomUser.objects.get(username=user)
    tickets = [ticket for ticket in Ticket.objects.all() if ticket.user_assigned == users]
    print(tickets)
    return render(request, "sorted.html", 
                    {"tickets": tickets,
                    "users": users})

@login_required()
def users_assigned(request, user):
    users = MyCustomUser.objects.get(username=user)
    tickets = [ticket for ticket in Ticket.objects.all() if ticket.user_completed == users]
    return render(request, "sorted.html", 
                    {"tickets": tickets,
                    "users": users})

@login_required()
def ticket_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = TicketAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                ticket_status=data['ticket_status'],
                user_assigned=data['user_assigned'],
                user_filled=request.user
            )
            return HttpResponseRedirect(reverse("home"))

    form = TicketAddForm()

    return render(request, html, {'form': form})

@login_required()
def ticket_edit_view(request, pk):
    html = "generic_form.html"

    if request.method == "POST":
        form = TicketEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            ticket = Ticket.objects.get(pk=pk)
            if data['ticket_status'] == "Invalid":
                ticket.ticket_status==data['ticket_status']
                ticket.user_assigned = "NULL"
                ticket.user_completed = "NULL"

            else:
                if data['title']:
                    ticket.title=data['title']
                if data['description']:
                    ticket.description=data['description']
                if data['ticket_status']:
                    print(ticket.ticket_status)
                    ticket.ticket_status=data['ticket_status']
                if data['user_assigned']:
                    ticket.user_assigned=data['user_assigned']

            ticket.save()
            return HttpResponseRedirect(reverse("home"))

    form = TicketEditForm()

    return render(request, html, {'form': form})


@login_required()
def ticket_assign(request, username, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.user_assigned = username
    ticket.save()
    return HttpResponseRedirect(reverse('home'))

@login_required()
def ticket_complete(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.user_completed = ticket.user_assigned
    ticket.ticket_status = "Done"
    ticket.save()
    return HttpResponseRedirect(reverse('home'))

