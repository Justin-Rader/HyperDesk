import uuid
from django.db import models
from tickets.field_choices import statusChoices, priorityChoices
from django.contrib.auth.models import User

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    profile_link = models.URLField(blank=True)

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='organizations')
    labels = models.CharField(max_length=200, blank=True)

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')
    labels = models.CharField(max_length=200, blank=True)

class AssignedUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name='assigned_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets')
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    role = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='assigned_users')
    labels = models.CharField(max_length=200, blank=True)

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=statusChoices.choices, default='new')
    priority = models.CharField(max_length=20, choices=priorityChoices.choices, default='low')
    submitter = models.ForeignKey(AssignedUser, on_delete=models.CASCADE, related_name='submitted_tickets')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tickets')
    labels = models.CharField(max_length=200, blank=True)

class TicketComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_comments')
    created_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    labels = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_date']
