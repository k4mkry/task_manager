from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):

    ASSIGNED_TO_CHOICE = (
        ('KKrysa', 'KKrysa'),
        ('KMyszkowski', 'KMyszkowski'),
    )

    PRIORITY_CHOICE = (
        ('Wysoki', '1 - Wysoki'),
        ('Normalny', '2 - Normalny'),
        ('Niski', '3 - Niski'),
    )

    STATUS = (
        ('Nierozpoczęte', 'Nierozpoczęte'),
        ('W toku', 'W toku'),
        ('Zakończone', 'Zakończone'),
        ('Odroczone', 'Ddroczone'),
    )

    ordered_by = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=15, choices=ASSIGNED_TO_CHOICE, default='KKrysa')
    description = models.TextField()
    notes = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICE, default='Normalny')
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Nierozpoczęte')


    def deadline(self):
        self.deadline_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Od {self.ordered_by}'