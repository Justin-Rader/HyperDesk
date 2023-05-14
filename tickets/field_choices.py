from django.db import models

class priorityChoices(models.TextChoices):
        URGENT = 'urgent'
        HIGH = 'high'
        MEDIUM = 'medium'
        LOW = 'low'
    
class statusChoices(models.TextChoices):
        NEW = 'new'
        IN_PROGRESS = 'in_progress'
        PENDING = 'pending'
        ON_HOLD = 'on_hold'
        SOLVED = 'solved'
